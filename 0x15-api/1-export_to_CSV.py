#!/usr/bin/python3
""" EXPORT CSV FORMAT """


if __name__ == "__main__":
    import requests as req
    from sys import argv
    import csv
    todos = req.get('https://jsonplaceholder.typicode.com/todos').json()
    users = req.get('https://jsonplaceholder.typicode.com/users').json()
    user = {}
    
    for elem in users:
        if elem["id"] == int(argv[1]):
            user = dict(elem)
            break
    user_todos = []
    
    for elem in todos:
        if elem["userId"] == int(argv[1]):
            user_todos.append(dict(elem))
    csv_export = []
    
    for elem in user_todos:
        strg = []
        strg.append(argv[1])
        strg.append(user["username"])
        if elem["completed"]:
            strg.append(True)
        else:
            strg.append(False)
        strg.append(elem["title"])
        csv_export.append(strg)
    
    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for strg in csv_export:
            writer.writerow(strg)
