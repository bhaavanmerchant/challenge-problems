This is a module and a server to manipulate the json, as stated in the problem.

https://docs.google.com/document/d/1CJep3ZD3K3ixX53E44yQlQujGG2YziZdav28XslnT5E/edit

To run this module, please run:
```
cat sample/input.json | python nest.py currency country city
```
or
```
make run
```

To run the tests, please run:
```
make test
```

To run the server, you will need to:
(This runs a basic flash uwsgi server, and is aimed as a proof of concept. This server model would probably be not suited for production workloads, and I would prefer using a pre-forked server instead + TODO: security stuff to block unwanted access using garbage content-type header).


```
pip install -r requirements.txt
export FLASK_APP=server/app.py
python -m flask run
```

If you wish to run this in a sandbox you have 2 options:

Inside venv:
```
python -m venv venv
source venv/bin/activate
```

As a AUFS container in docker:
```
sudo docker build -t revolut-interview-app .
```


You can test the server by running the following curl command:
```
curl -X POST 127.0.0.1:5000/nest/currency,country,city --user admin:42 -d "@sample/input.json" -H "Content-Type: application/json"
```


SQL:

The SQL problems are solves in the `sql-problems` folder, and the sql runs inside sqlfiddle.