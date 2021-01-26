import requests
from ..models import Company, CustomUser


users_data = requests.get('http://jsonplaceholder.typicode.com/users')
response_users_data = users_data.json()

posts_data = requests.get('http://jsonplaceholder.typicode.com/posts')
response_posts_data = posts_data.json()


def run():
    for user_data in response_users_data:
        if not Company.objects.filter(name=user_data['company']['name']).exists():
            test_save_customer = Company(name=user_data['company']['name'],
                                         catchPhrase=user_data['company']['catchPhrase'],
                                         bs=user_data['company']['bs'])
            test_save_customer.save()

        if not CustomUser.objects.filter(username=user_data['name']).exists():
            save_data_user = CustomUser(username=user_data['name'],
                                        phone=user_data['phone'],
                                        website=user_data['website'])
            save_data_user.save()

        test = CustomUser.objects.get(username=user_data['name'])
        test2 = Company.objects.get(name=user_data['company']['name'])
        test.company = test2
        test.save()
