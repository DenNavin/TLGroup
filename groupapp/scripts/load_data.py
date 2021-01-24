import requests
from ..models import Company


users_data = requests.get('http://jsonplaceholder.typicode.com/users')
response_users_data = users_data.json()

posts_data = requests.get('http://jsonplaceholder.typicode.com/posts')
response_posts_data = posts_data.json()


def run():
    if not Company.objects.filter(name=response_users_data[0]['company']['name']).exists():
        test_save_customer = Company(name=response_users_data[0]['company']['name'],
                                     catchPhrase=response_users_data[0]['company']['catchPhrase'],
                                     bs=response_users_data[0]['company']['bs'])
        test_save_customer.save()


#save_data_user = CustomUser(name=response_users_data[0]['name'],
#                            phone=response_users_data[0]['phone'],
#                            website=response_users_data[0]['website'])
#save_data_user.save()

#test = CustomUser.objects.get(pk=15)
#test2 = Company.objects.get(name=response_users_data[0]['company']['name'])
#test.company = test2
#test.save()



#============================================
#for user_data in response_users_data:
#    save_data_company = Company(name=user_data['company']['name'],
#                             catchPhrase=user_data['company']['catchPhrase'],
#                             bs=user_data['company']['catchPhrase'])
#    save_data_company.save()
#
#    save_data_user = CustomUser(name=user_data['name'],
#                                phone=user_data['phone'],
#                                website=user_data['website'],
#                                company=)
#    save_data_user.save()
