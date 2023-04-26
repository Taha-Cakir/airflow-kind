from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'my_dag12',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='my_task',
    bash_command='echo "Hello World!"',
    dag=dag,
)

t2 = BashOperator(
    task_id='my_task2',
    bash_command='echo "Hello World2!"',
    dag=dag,
)

t1 >> t2