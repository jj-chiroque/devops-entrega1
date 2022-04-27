# devops-entrega1

## for local enviroment
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 application.py

## for testing enviroment
pip3 install pytest

## for deployment aws elastic beansltalk
update SQLALCHEMY_DATABASE_URI