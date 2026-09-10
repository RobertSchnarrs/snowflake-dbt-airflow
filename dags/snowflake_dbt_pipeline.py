from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
DBT_PROJECT_DIR = "/opt/airflow/dbt"
DBT_PROFILES_DIR = "/opt/airflow/dbt"
with DAG(
    dag_id="snowflake_dbt_pipeline",
    description="Load seed data and build dbt models in Snowflake",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
    tags=["snowflake", "dbt", "learning"],
) as dag:
    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt debug --profiles-dir {DBT_PROFILES_DIR}",
    )
    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt seed --profiles-dir {DBT_PROFILES_DIR}",
    )
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --profiles-dir {DBT_PROFILES_DIR}",
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --profiles-dir {DBT_PROFILES_DIR}",
    )
    dbt_debug >> dbt_seed >> dbt_run >> dbt_test