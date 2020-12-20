import requests
import json


response_data = requests.get('http://jsonplaceholder.typicode.com/users')
response_data2 = response_data.json()

list_address = []
list_user = []
list_company = []
for i in response_data2:
    for_company = {
        'pk': i['id'],
        'model': 'groupapp.company',
        'fields': {
            'name': i['company']['name'],
            'catchPhrase': i['company']['catchPhrase'],
            'bs': i['company']['catchPhrase'],
        }
    }

    for_user = {
        'pk': i['id'],
        'model': 'groupapp.user',
        'fields':
            {
            'name': i['name'],
            'username': i['username'],
            'email': i['email'],
            'phone': i['phone'],
            'website': i['website'],
            'company': i['id']
            }
        }

    for_address = {
        'pk': i['id'],
        'model': 'groupapp.address',
        'fields': {
            'street': i['address']['street'],
            'suite': i['address']['suite'],
            'city': i['address']['city'],
            'zipcode': i['address']['zipcode'],
            'latitude': i['address']['geo']['lat'],
            'longitude': i['address']['geo']['lng'],
            'user_id': i['id']
        }
    }
    list_address.append(for_address)
    list_user.append(for_user)
    list_company.append(for_company)

with open('fixt1.json', 'w') as fixt_write:
    json.dump(list_company, fixt_write)

with open('fixt2.json', 'w') as fixt_write2:
    json.dump(list_user, fixt_write2)

with open('fixt3.json', 'w') as fixt_write3:
    json.dump(list_address, fixt_write3)

response_post = requests.get('http://jsonplaceholder.typicode.com/posts')
response_post2 = response_post.json()

list_post = []
for q in response_post2:

    for_post = {
        'pk': q['id'],
        'model': 'groupapp.post',
        'fields': {
            'userId': q['userId'],
            'title': q['title'],
            'body': q['body']
        }
    }
    list_post.append(for_post)

with open('fixt4.json', 'w') as fixt_write4:
    json.dump(list_post, fixt_write4)

del list_post, list_address, list_user, list_company

