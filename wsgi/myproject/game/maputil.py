
from .models import Realm, Zone
import random

# Global Variables

REALM_HEIGHT = 10
REALM_WIDTH = 16

# Util Functions


def generate_random(realm):
    # if realm already has zones, delete them
    if realm.zone_set.all().count() != 0:
        realm.zone_set.all().delete()
    # randomly generate realm
    for r in range(REALM_HEIGHT):
        for c in range(REALM_WIDTH):
            if r == 0 or c == 0:
                realm.zone_set.create(row=r, column=c, type=random.randint(0, 1))
            else:
                realm.zone_set.create(row=r, column=c,
                                      type=random.choice([
                                          realm.get_zone(row=r-1, column=c).type,
                                          realm.get_zone(row=r, column=c-1).type,
                                          realm.get_zone(row=r-1, column=c-1).type,
                                          random.randint(0, 1)
                                      ]))
    realm.save()