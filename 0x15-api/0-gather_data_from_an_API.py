#!/usr/bin/python3
""" REST API JSONPlaceholder (USERS) """
import requests as req
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])

    def req_user():
        """ Request the user from the JSONPlaceholder  """
        userjs = req.get('https://jsonplaceholder.typicode.com/users').json()
        user = {}
        for elem in userjs:
            if elem["id"] == user_id:
                user = dict(elem)
                break
        return user

    def req_todos():
        """ Request task completed of employe """
        user = req_user()
        todos = req.get('https://jsonplaceholder.typicode.com/todos').json()
        user_tuto = []
        user_tutos_complete = []
        tasks_complete = 0
        for elem in todos:
            if elem["userId"] == user_id:
                user_tuto.append(dict(elem))
                if elem["completed"]:
                    tasks_complete = tasks_complete + 1
                    user_tutos_complete.append(dict(elem))
        total_tasks = len(user_tuto)
        print("Employee {} is done with tasks({}/{}):"
              .format(user["name"], tasks_complete, total_tasks))
        for task in user_tutos_complete:
            print("\t {}".format(task["title"]))

    req_todos()
