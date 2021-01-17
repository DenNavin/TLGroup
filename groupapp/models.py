from django.db import models
from django.contrib.auth.models import AbstractUser
from . load_data import response_users_data, response_posts_data


class Company(models.Model):
    name = models.CharField(max_length=150)
    catchPhrase = models.CharField(max_length=500)
    bs = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=300)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} {2}'.format(self.suite, self.street, self.city)


class Post(models.Model):
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    credit = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


if not Company.objects.filter(name=response_users_data[0]['company']['name']).exists():
    test_save_customer = Company(name=response_users_data[0]['company']['name'],
                                 catchPhrase=response_users_data[0]['company']['catchPhrase'],
                                 bs=response_users_data[0]['company']['bs'])
    test_save_customer.save()


#save_data_user = CustomUser(name=response_users_data[0]['name'],
#                            phone=response_users_data[0]['phone'],
#                            website=response_users_data[0]['website'])
#save_data_user.save()

test = CustomUser.objects.get(pk=15)
test2 = Company.objects.get(name=response_users_data[0]['company']['name'])
test.company = test2
test.save()



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