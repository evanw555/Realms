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


def delete_realm(realm):
    """Deletes a realm safely by deleting
    the zones from its zone set as well.
    :param realm: Realm model to delete.
    """
    realm.zone_set.all().delete()
    realm.delete()


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

    def get_zone(self, r, c):
        try:
            return self.zone_set.get(row=r, column=c)
        except:
            return None

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        app_label = 'game'


class Zone(models.Model):
    realm = models.ForeignKey(Realm)
    row = models.PositiveSmallIntegerField(default=0)
    column = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '<Zone {},{}@{} [{}]>'.format(str(self.realm), str(self.row), str(self.column), str(self.type))

    class Meta:
        managed = True
        app_label = 'game'

