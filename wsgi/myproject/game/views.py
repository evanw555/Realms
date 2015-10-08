from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserAccount, Realm, get_useraccount, delete_realm
from . import maputil
import random


def homepage(request):
    return render(request,
                  'game/home.html',
                  {'user': request.user,
                   'logged_in': request.user.is_authenticated()})


def about(request):
    return render(request, 'game/about.html')


def login_attempt(request):
    # when user manually enters url without POST data
    if request.method != "POST":
        return HttpResponseRedirect(reverse('game:home'))
    # when user links to page with valid POST data
    user_in = authenticate(username=request.POST['username'].lower(), password=request.POST['password'])
    # authentication FAIL
    if user_in is None:
        return render(request,
                      'game/home.html',
                      {'error_message': "Error: invalid login",
                       'user': request.user,
                       'logged_in': request.user.is_authenticated()})
    # authentication SUCCESS
    else:
        # check for missing fields
        # field_changes = {}
        # changes_present = False
        # # check for missing first name
        # field_changes['firstname'] = False
        # if user_in.first_name == '':
        #     field_changes['firstname'] = True
        #     changes_present = True
        # # check for missing last name
        # field_changes['lastname'] = False
        # if user_in.last_name == '':
        #     field_changes['lastname'] = True
        #     changes_present = True
        # if user has fields that now need to be updated
        if False:  # changes_present:
            pass
            # return render(request,
            #               'login/fields_missing.html',
            #               {'firstname_missing': field_changes['firstname'],
            #                'lastname_missing': field_changes['lastname'],
            #                'user': user_in})
        # if user's fields are all updated
        else:
            # LOG IN USER
            login(request, user_in)
            # if user has no user_account, create one
            if get_useraccount(request.user) is None:
                user_account = UserAccount(user=request.user)
                user_account.save()
            # render login_success page
            return render(request,
                          'game/login_success.html',
                          {'user': request.user,
                           'useraccount': get_useraccount(request.user)})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('game:home'))


def sign_up(request):
    was_logged_in = request.user.is_authenticated()
    logout(request)
    return render(request,
                  'game/sign_up.html',
                  {'was_logged_in': was_logged_in})


def sign_up_attempt(request):
    # when user manually enters url without POST data
    if request.method != "POST":
        return HttpResponseRedirect(reverse('game:sign_up'))
    # if missing a required field
    if request.POST['username'] == '' or request.POST['password1'] == '' \
            or request.POST['password2'] == '' or request.POST['firstname'] == '' \
            or request.POST['lastname'] == '':
        return render(request,
                      'game/sign_up.html',
                      {'was_logged_in': False,
                       'error_message': "Error: missing required fields"})
    # if passwords don't match
    elif request.POST['password1'] != request.POST['password2']:
        return render(request,
                      'game/sign_up.html',
                      {'was_logged_in': False,
                       'error_message': "Error: you're pretty bad at typing the same password twice"})
    # if sign up form valid
    else:
        try:
            # CREATE USER
            new_user = User.objects.create_user(username=request.POST['username'].lower(),
                                                password=request.POST['password1'],
                                                email=request.POST['email'])
            new_user.first_name = request.POST['firstname'].capitalize()
            new_user.last_name = request.POST['lastname'].capitalize()
            new_user.save()
            # CREATE USER ACCOUNT
            new_user_account = UserAccount(user=new_user)
            new_user_account.save()
        # if username already taken by another user
        except IntegrityError:
            return render(request,
                          'game/sign_up.html',
                          {'was_logged_in': False,
                           'error_message': "Error: username already taken, but I bet you'd like \'{0}{1}\'".format(
                               request.POST['username'].lower(), random.randrange(20, 10000))})
        # if could not create new user for some reason
        except:
            return render(request,
                          'game/sign_up.html',
                          {'was_logged_in': False,
                           'error_message': "Error: unknown signup error, ask Evan"})
        # if user creation successful
        else:
            return render(request,
                          'game/sign_up_success.html',
                          {'user': new_user})


# def update_attempt(request):
#     # when user manually enters url without POST data
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse('login:main_login'))
#     # when user links to page with valid POST data
#     user = authenticate(username=request.POST['username'].lower(), password=request.POST['password'])
#     # if unable to authenticate user, render page with error_message
#     if user is None:
#         return render(request,
#                       'login/fields_missing.html',
#                       {'firstname_missing': True if request.POST['firstname_missing'] == "True" else False,
#                        'lastname_missing': True if request.POST['lastname_missing'] == "True" else False,
#                        'error_message': "Error: invalid login"})
#     # if missing required fields on the form
#     elif ((user.first_name == '') and (request.POST['firstname_update'] == '')) \
#             or ((user.last_name == '') and (request.POST['lastname_update'] == '')):
#         return render(request,
#                       'login/fields_missing.html',
#                       {'firstname_missing': (user.first_name == ''),
#                        'lastname_missing': (user.last_name == ''),
#                        'user': user,
#                        'error_message': "Error: missing required fields"})
#     # if all fields filled out correctly
#     else:
#         # UPDATE USER
#         login(request, user)
#         if request.user.first_name == '':
#             request.user.first_name = request.POST['firstname_update'].capitalize()
#         if request.user.last_name == '':
#             request.user.last_name = request.POST['lastname_update'].capitalize()
#         request.user.save()
#         return render(request,
#                       'login/login_success.html',
#                       {'user': request.user,
#                        'current_app': 'login'})
#


@login_required
def realm_select(request):
    # DEBUG
    if random.randint(0, 1) == 0:
        new_realm = Realm(name='Realm {}'.format(random.randint(0, 1000)))
        new_realm.save()
        maputil.generate_random(new_realm)
    elif Realm.objects.all().count() > 0:
        delete_realm(Realm.objects.all()[0])
    # END DEBUG
    return render(request,
                  'game/realm_select.html',
                  {'available_realms': Realm.objects.all()})


@login_required
def realm_view(request):
    realm = Realm.objects.get(pk=request.GET['r'])
    return render(request,
                  'game/realm.html',
                  {'realm': realm,
                   'zone_types': [[realm.get_zone(r, c).type for c in range(maputil.REALM_WIDTH)] for r in range(maputil.REALM_HEIGHT)],
                   'canvas_width': maputil.REALM_WIDTH * maputil.TILE_SIZE,
                   'canvas_height': maputil.REALM_HEIGHT * maputil.TILE_SIZE,
                   'tile_size': maputil.TILE_SIZE})

