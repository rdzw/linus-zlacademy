from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.googlesheets import BotGoogleSheetsPlugin
from webdriver_manager.chrome import ChromeDriverManager
from owid import catalog
from datetime import datetime
import pandas as pd

BotMaestroSDK.RAISE_NOT_CONNECTED = False


class bot(WebBot):

    def configura_bot(self) -> None:
        self.headless = False
        self.browser = Browser.CHROME
        self.driver_path = ChromeDriverManager().install()

    def action(self, execution = None):
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        try:
            # Carrega o catálogo de dados
            rc = catalog.RemoteCatalog()
            uri = 'garden/covid/latest/cases_deaths/cases_deaths'
            df = rc[uri]

            df = df.reset_index()

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
            print('teste')

            # Filtra para o mês atual e para o Brasil
            current_month = datetime.now().month
            current_year = datetime.now().year
            df_filtered['date'] = pd.to_datetime(df_filtered['date'])
            df_filtered = df_filtered[
                (df_filtered['date'].dt.month == current_month) & 
                (df_filtered['date'].dt.year == current_year) & 
                (df_filtered['country'] == 'Brazil')
            ]

            print(df_filtered)

            # Inicializa o plugin do Google Sheets
            bot_planilha = BotGoogleSheetsPlugin('credential.json', '1Co2Yuuj23NDZ78GClNFlMebSm5Mcn7x4V5zDBWsbIeM')

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
        
        except Exception as erro:
            print('Erro: ', erro)
            self.save_screenshot('erro.png')

        finally:
            self.wait(3000)
            self.stop_browser()


            # maestro.finish_task(
            #     task_id=execution.task_id,
            #     status=AutomationTaskFinishStatus.SUCCESS,
            #     message="Task Finished OK."
            # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    bot.main()
