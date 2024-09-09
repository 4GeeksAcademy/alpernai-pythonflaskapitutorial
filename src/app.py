from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todo():
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_todo_list = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_todo_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_todo_list = jsonify(todos)
    return json_todo_list

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)