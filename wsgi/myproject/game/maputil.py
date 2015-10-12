
from .models import Realm, Zone
import random

# Global Variables

REALM_HEIGHT = 20
REALM_WIDTH = 32
VIEW_HEIGHT = 10
VIEW_WIDTH = 16
TILE_SIZE = 32

# Util Functions


def generate_random(realm):
    # if realm already has zones, delete them
    if realm.zone_set.all().count() != 0:
        realm.zone_set.all().delete()
    # make tenative grid of zone types
    map = []
    for r in range(REALM_HEIGHT):
        temp_row = []
        for c in range(REALM_WIDTH):
            temp_row.append(0)
        map.append(temp_row)
    # randomly generate water and land
    for r in range(REALM_HEIGHT):
        for c in range(REALM_WIDTH):
            if r == 0 or c == 0:
                map[r][c] = random.randint(0, 1)
            else:
                map[r][c] = random.choice([
                    map[r-1][c],
                    map[r][c-1],
                    map[r-1][c-1],
                    0, 1, 1,
                ])
    # randomly generate forests and mountains

    def recursive_set(row, column, type, chance, reduction):
        if row < 0 or row >= REALM_HEIGHT or column < 0 or column >= REALM_WIDTH:
            return
        if random.randint(0, 100) <= chance:
            map[row][column] = type
            recursive_set(row-1, column, type, chance // reduction, reduction)
            recursive_set(row, column-1, type, chance // reduction, reduction)
            recursive_set(row+1, column, type, chance // reduction, reduction)
            recursive_set(row, column+1, type, chance // reduction, reduction)

    r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    while map[r][c] != 0:
        r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    recursive_set(r, c, 2, 100, 1.6)

    r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    while map[r][c] != 0:
        r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    recursive_set(r, c, 3, 100, 2.0)

    # save map to realm model
    for r in range(REALM_HEIGHT):
        for c in range(REALM_WIDTH):
            realm.zone_set.create(row=r, column=c, type=map[r][c])
    realm.save()
