
from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime

with    DAG('quarta_dag', description= "Nossa quarta DAG", schedule_interval=None,
          start_date=datetime(2024,1,15),catchup=False) as dag:


    task1 = BashOperator(task_id="tsk1",bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2",bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3",bash_command="sleep 5")

# Sequencia de execução das tasks

    task1.set_upstream(task2)
    task2.set_upstream(task3)