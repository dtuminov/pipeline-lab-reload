from airflow.decorators import task


@task
def waiting_task():
    print("Ожидание завершения.")