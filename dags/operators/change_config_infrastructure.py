from airflow.decorators import task


@task
def change_config_infrastructure() -> None:
    print('hello')
