import os
# cmd = 'ls -l'
# cmd= "curl -X GET http://example.com"
# cmd= "curl -X GET https://jsonplaceholder.typicode.com/posts/1"
# # Pour voir les en-têtes, nous pouvons ajouter l’argument -i à la commande :
# cmd = "curl -X GET -i https://jsonplaceholder.typicode.com/posts/1"

# #  il faut précéder vos en-têtes de l’argument -H et le corps de l’argument -d.
# cmd="curl -X PUT -i\
#  -H "Content-Type: application/json"\
#  -d '{"id": 1, "content": "hello world"}'\
#  https://jsonplaceholder.typicode.com/posts/1"

# os.system(cmd)

# pip3 install requests
# or conda install requests
import requests

# creating a GET request
r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(r)

# getting the response elements
response_dict = r.json()
print(response_dict)
response_header = r.headers
print(response_header)
status_code = r.status_code
print("status_code",status_code)

p=requests.put(url='https://jsonplaceholder.typicode.com/posts/1',
    data={"id": 1, "content": "hello world"},
    headers={"Content-Type": "application/json"}
    )
print("status_p",p.status_code)

# Une autre librairie populaire est la librairie Urllib installée nativement avec Python mais plus difficile à utiliser.

