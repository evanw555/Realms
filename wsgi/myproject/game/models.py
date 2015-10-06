from django.db import models
from django.contrib.auth.models import User


# Model util functions


def get_useraccount(u):
    """Get the UserAccount associated with a User.
    Returns None if none exists.
    :param u: User whose UserAccount to search for
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

    def __getitem__(self, item):
        try:
            return self.zone_set.filter(row=item)
        except:
            return None

    def get_zone(self, r, c):
        try:
            return self.zone_set.get(row=r, column=c)
        except:
            return None

    class Meta:
        managed = True
        app_label = 'game'


class Zone(models.Model):
    realm = models.ForeignKey(Realm)
    row = models.PositiveSmallIntegerField(default=0)
    column = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return '<{}@{},{}: {}>'.format(str(self.realm), str(self.row), str(self.column), self.str_type())

    def str_type(self):
        return {
            0: 'sea',
            1: 'plains',
        }[int(self.type)]

    class Meta:
        managed = True
        app_label = 'game'
