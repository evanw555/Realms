from django.db import models
from django.contrib.auth.models import User


# Model util functions


def get_useraccount(user):
    """Get the UserAccount associated with a User.
    Returns None if none exists.
    :param user: User whose UserAccount to search for
    :return: UserAccount associated with User.
    :rtype: UserAccount
    """
    try:
        return UserAccount.objects.get(username=user.username)
    except:
        return None


# Models


class UserAccount(models.Model):
    user = models.OneToOneField(User)
    cash = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.user.username)

