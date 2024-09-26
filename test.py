# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:07:28 2024

@author: Navuru.Prasad
"""


from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2024, 9, 23),
}


def load_data_into_gcs(**context):
    print(f"Data to insert into : {10}")
    
def sample_Task(**context):
      print(f"Data tsample_Task: {10}")  
    
    

with DAG('data_pipeline', default_args=default_args, schedule_interval='*/5 * * * *', catchup=False) as dag:
    
    sample_Task = PythonOperator(
        task_id='sample_Task',
        python_callable=sample_Task
    )
    
    load_data_task = PythonOperator(
        task_id='load_data_into_gcs',
        python_callable=load_data_into_gcs,
        provide_context=True
    )

    sample_Task >> load_data_task
