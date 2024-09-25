from airflow.decorators import task

@task.branch
def choose_branch():
    import random
    return 'rec_embedder' if random.choice([True, False]) else 'search_embedder'