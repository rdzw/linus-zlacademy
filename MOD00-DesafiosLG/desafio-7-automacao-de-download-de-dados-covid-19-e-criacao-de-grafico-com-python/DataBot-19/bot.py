from botcity.web import WebBot
from botcity.maestro import *
from botcity.plugins.googlesheets import BotGoogleSheetsPlugin
from owid import catalog
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

BotMaestroSDK.RAISE_NOT_CONNECTED = False

class bot(WebBot):

    def action(self, execution = None):
        try:
            maestro = BotMaestroSDK.from_sys_args()
            execution = maestro.get_execution()

            print(f"Task ID is: {execution.task_id}")
            print(f"Task Parameters are: {execution.parameters}")
            
            maestro.alert(
                task_id=execution.task_id,
                title="DataBot-19",
                message="Iniciando o processo",
                alert_type=AlertType.INFO
            )

            df_filtered, linhas = self.load_data()
            self.add_to_google_sheets(df_filtered)
            self.generate_plot(df_filtered)

            status = AutomationTaskFinishStatus.SUCCESS
            message = "Execução finalizada com sucesso"
                    
        except Exception as erro:
            bot.save_screenshot("erro.png")

            maestro.error(
                task_id=execution.task_id,
                exception=erro,
                screenshot="erro.png",
            )

            status = AutomationTaskFinishStatus.FAILED
            message = "Execução finalizada com falha"

        finally:
            maestro.new_log_entry(
                activity_label="databot19",
                values={
                    "data_hora": datetime.now().strftime("%Y-%m-%d_%H-%M"),
                    "linhas_filtradas": linhas,
                    "google_sheets": "conectado"
                }
            )

            maestro.post_artifact(
                task_id=execution.task_id,
                artifact_name= 'result.png',
                filepath= 'grafico_covid_brasil.png'
            )

            maestro.finish_task(
                task_id=execution.task_id,
                status=status,
                message=message
            )
    
    def load_data(self):
        """Carrega e filtra os dados do catálogo OWID."""
        rc = catalog.RemoteCatalog()
        uri = 'garden/covid/latest/cases_deaths/cases_deaths'
        df = rc[uri].reset_index()

        # Seleciona as colunas desejadas
        selected_columns = [
            "country",
            "date",
            "days_since_100_total_cases",
            "days_since_5_total_deaths",
            "days_since_1_total_cases_per_million",
            "days_since_0_1_total_deaths_per_million",
            "days_since_100_total_cases_and_5m_pop"
        ]
        df_filtered = df[selected_columns].copy()

        # Filtra para o mês atual e para o Brasil
        current_month = datetime.now().month
        current_year = datetime.now().year
        df_filtered['date'] = pd.to_datetime(df_filtered['date'])
        df_filtered = df_filtered[
            (df_filtered['date'].dt.month == current_month) & 
            (df_filtered['date'].dt.year == current_year) & 
            (df_filtered['country'] == 'Brazil')
        ]

        linhas = (f"{len(df_filtered)} linhas filtradas do catalogo da owid.")
        return df_filtered, linhas

    def add_to_google_sheets(self, df_filtered):
        """Adiciona os dados filtrados ao Google Sheets."""
        bot_planilha = BotGoogleSheetsPlugin('credential.json', '1Co2Yuuj23NDZ78GClNFlMebSm5Mcn7x4V5zDBWsbIeM')
        bot_planilha.clear_range(F'A2:G{len(df_filtered)+1}')
        for _, row in df_filtered.iterrows():
            bot_planilha.add_rows([[
                row['country'],
                row['date'].strftime('%Y-%m-%d'),
                row['days_since_100_total_cases'],
                row['days_since_5_total_deaths'],
                row['days_since_1_total_cases_per_million'],
                row['days_since_0_1_total_deaths_per_million'],
                row['days_since_100_total_cases_and_5m_pop']
            ]])
        sheet = bot_planilha.get_column('B')
        return sheet

    def generate_plot(self, df_filtered):
        """Gera o gráfico com os dados filtrados."""
        plt.figure(figsize=(12, 8))
        plt.plot(df_filtered['date'], df_filtered['days_since_100_total_cases'], label="Days since 100 total cases")
        plt.plot(df_filtered['date'], df_filtered['days_since_5_total_deaths'], label="Days since 5 total deaths")
        plt.plot(df_filtered['date'], df_filtered['days_since_1_total_cases_per_million'], label="Days since 1 case per million")
        plt.plot(df_filtered['date'], df_filtered['days_since_0_1_total_deaths_per_million'], label="Days since 0.1 deaths per million")
        plt.plot(df_filtered['date'], df_filtered['days_since_100_total_cases_and_5m_pop'], label="Days since 100 total cases and 5M pop")

        # Personalizando o gráfico
        plt.xlabel("Date")
        plt.ylabel("Days Since Milestone")
        plt.title("Daily Evolution of COVID-19 Cases and Deaths in Brazil (Current Month)")
        plt.legend()

        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Exibe todas as datas
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Formato da data
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Salva o gráfico como uma imagem
        plt.savefig('grafico_covid_brasil.png')
        plt.close()

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    bot.main()