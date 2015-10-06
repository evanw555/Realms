from django.db import models
from django.contrib.auth.models import User


# Model util functions


def get_useraccount(u):
    """Get the UserAccount associated with a User.
    Returns None if none exists.
    :param user: User whose UserAccount to search for
    :return: UserAccount associated with User.
    :rtype: UserAccount
    """
    try:
        return UserAccount.objects.get(user=u)
    except:
        return None


# Models


class UserAccount(models.Model):
    user = models.OneToOneField(User)
    cash = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        managed = True
        app_label = 'game'


class Realm(models.Model):
    name = models.CharField(max_length=32, default='Default')

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        app_label = 'game'

