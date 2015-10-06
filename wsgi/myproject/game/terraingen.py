#
# from .models import Realm
#
#
# def build_realm_terrain_random(realm, height, width):
#     # if realm already has terrain, delete all
#     realm.zone_set.all().delete()
#     # build realm terrain randomly
#     for r in range(height):
#         for c in range(width):
#             realm.zone_set.create(row=r, column=c, type=0)
#     realm.save()

