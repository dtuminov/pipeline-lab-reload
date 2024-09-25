from airflow import DAG
import datetime as dt


from operators import (check_config, load, choose_branch,
                       rec_embedder, search_embedder,
                       upload_to_milvus,change_config_infrastructure,join)

with DAG(
    dag_id='name_of_pipeline',
    start_date=dt.datetime(2021, 3, 1),
    schedule='@once'
) as dag:


    task1 = check_config.check_config()
    task2 = load.load()
    task3 = choose_branch.choose_branch()
    task4 = rec_embedder.rec_embedder()
    task5 = search_embedder.search_embedder()
    task6_1 = upload_to_milvus.upload_to_milvus()
    task6_2 = upload_to_milvus.upload_to_milvus()
    task7 = change_config_infrastructure.change_config_infrastructure()
    waiting_task = join.waiting_task()
    task1>>task2>>task3>>[task4, task5]

    [task4 >> task6_1 >>waiting_task, task5 >> task6_2>>waiting_task] >> task7


