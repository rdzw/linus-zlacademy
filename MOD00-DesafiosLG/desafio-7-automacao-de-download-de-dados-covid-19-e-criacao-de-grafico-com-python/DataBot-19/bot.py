from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from owid import catalog
from datetime import datetime

import pandas as pd

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    
    rc = catalog.RemoteCatalog()
    uri = 'garden/covid/latest/cases_deaths/cases_deaths'
    df = rc[uri]

    # Resetar o índice para trazer a data como uma coluna
    df = df.reset_index()

    # Verificar o nome da coluna de data
    print(df.columns)  # Confirme o nome correto da coluna de data aqui

    # Filtrar para o mês atual
    current_month = datetime.now().month
    current_year = datetime.now().year
    df['date'] = pd.to_datetime(df['date'])  # Substitua 'date' pelo nome correto, caso seja diferente
    df_filtered = df[(df['date'].dt.month == current_month) & (df['date'].dt.year == current_year)]

    # Salvar em um arquivo Excel
    df_filtered.to_excel("relatorio_covid_mes_atual.xlsx", index=False)
    print("Relatório salvo como 'relatorio_covid_mes_atual.xlsx'.")


    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
