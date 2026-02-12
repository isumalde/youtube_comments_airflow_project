sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev -y

python3.11 -m venv airflow_venv
source airflow_venv/bin/activate
pip install --upgrade pip setuptools wheel

AIRFLOW_VERSION=2.8.1
PYTHON_VERSION=3.11
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip install pandas boto3 s3fs google-api-python-client

airflow standalone
