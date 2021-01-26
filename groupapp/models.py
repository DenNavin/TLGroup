from django.db import models
from django.contrib.auth.models import AbstractUser
#from tlgroup.scripts.load_data import response_users_data


class Company(models.Model):
    name = models.CharField(max_length=150)
    catchPhrase = models.CharField(max_length=500)
    bs = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class CustomUser(AbstractUser):
    # name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=300)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

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