from airflow.decorators import task


@task
def load() -> None:
    print('hello')
