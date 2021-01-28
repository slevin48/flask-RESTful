# Flask-RESTful
https://flask-restful.readthedocs.io/en/latest/quickstart.html

Test Flask-RESTful extension for Flask that adds support for quickly building REST APIs

## Hello World
```
$ python hello.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
$ curl http://127.0.0.1:5000/
{"hello": "world"}
```

## Full example
```
$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```
GET the list
```
$ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
```
GET a single task
```
$ curl http://localhost:5000/todos/todo3
{"task": "profit!"}
```
DELETE a task

```
$ curl http://localhost:5000/todos/todo2 -X DELETE -v
```
Add a new task
```
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v
```
