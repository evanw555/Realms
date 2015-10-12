
from .models import Realm, Zone
import random

# Global Variables

REALM_HEIGHT = 20
REALM_WIDTH = 32
VIEW_HEIGHT = 10
VIEW_WIDTH = 16
TILE_SIZE = 32

# Util Functions


def generate_terrain(realm, method):
    # if realm already has zones, delete them
    if realm.zone_set.all().count() != 0:
        realm.zone_set.all().delete()
    # make dummy grid of zone types
    type_map = []
    for r in range(REALM_HEIGHT):
        temp_row = []
        for c in range(REALM_WIDTH):
            temp_row.append(0)
        type_map.append(temp_row)
    # apply generation method to this map
    method(type_map)
    # save map to realm model
    for r in range(REALM_HEIGHT):
        for c in range(REALM_WIDTH):
            realm.zone_set.create(row=r, column=c, type=type_map[r][c])
    realm.save()


def random_generation(type_map):
    # randomly generate water and land
    for r in range(REALM_HEIGHT):
        for c in range(REALM_WIDTH):
            if r == 0 or c == 0:
                type_map[r][c] = random.randint(0, 1)
            else:
                type_map[r][c] = random.choice([
                    type_map[r-1][c],
                    type_map[r][c-1],
                    type_map[r-1][c-1],
                    0, 1, 1,
                ])
    # randomly generate forests and mountains

    def recursive_set(row, column, zone_type, chance, reduction):
        if row < 0 or row >= REALM_HEIGHT or column < 0 or column >= REALM_WIDTH:
            return
        if random.randint(0, 100) <= chance:
            type_map[row][column] = zone_type
            recursive_set(row-1, column, zone_type, chance // reduction, reduction)
            recursive_set(row, column-1, zone_type, chance // reduction, reduction)
            recursive_set(row+1, column, zone_type, chance // reduction, reduction)
            recursive_set(row, column+1, zone_type, chance // reduction, reduction)

    r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    while type_map[r][c] != 0:
        r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    recursive_set(r, c, 2, 100, 1.6)

    r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    while type_map[r][c] != 0:
        r, c = random.randint(0, REALM_HEIGHT-1), random.randint(0, REALM_WIDTH-1)
    recursive_set(r, c, 3, 100, 2.0)


