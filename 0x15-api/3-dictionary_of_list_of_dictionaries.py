#!/usr/bin/python3
""" export data in the JSON format """


if __name__ == "__main__":
    import requests as req
    from sys import argv
    import json

    todos = req.get('https://jsonplaceholder.typicode.com/todos').json()
    users = req.get('https://jsonplaceholder.typicode.com/users').json()
    todo_users = {}

    for user in users:
        user_todos = []
        for task in todos:
            try:
                if task['userId'] == user['id']:
                    del task['userId']
                    del task['id']
                    task['username'] = user['username']
                    task['task'] = task.pop('title')
                    user_todos.append(task)
            except Exception:
                pass
        todo_users[user['id']] = user_todos
    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_users, f)
