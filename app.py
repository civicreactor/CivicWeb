from flask import Flask, request, render_template
from flask_restful import reqparse, abort, Api, Resource
from py2neo import Graph
from civicFlask.mypyfile import cypherQry


app = Flask(__name__)
api = Api(app)

gdb = Graph("http://CivicBase:NhrBKsP5ULtZopafC7a9@civicbase.sb04.stations.graphenedb.com:24789/db/data/")


@app.route('/')
def landing():
    return render_template("landing.html",
                        title = 'Home')

@app.route('/project')
def proj():
    qry = cypherQry.getAllNodes("PROJECT")
    res = gdb.cypher.execute(qry)
    for i in res:
        print (i[0])
    return render_template("project.html",
                        title = 'Projects',
                        result = res)

@app.route('/skill')
def skill():
    qry = "match (s:SKILL) return s"
    res = gdb.cypher.execute(qry)
    for i in res:
        print (i[0])
    return render_template("skill.html",
                        title = 'Skills',
                        result = res)

@app.route('/user')
def users():
    qry = "match (s:PERSON) return s"
    res = gdb.cypher.execute(qry)
    for i in res:
        print (i[0])
    return render_template("user.html",
                        title = 'Users',
                        result = res)




@app.route('/topic')
def topic():
    qry = "match (s:TOPIC) return s"
    res = gdb.cypher.execute(qry)
    for i in res:
        print (i[0])
    return render_template("topic.html",
                        title = 'Topic',
                        result = res)





######### API SECTION ##################

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)

