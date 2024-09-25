from airflow.decorators import task


@task
def rec_embedder() -> None:
    print('hello')
