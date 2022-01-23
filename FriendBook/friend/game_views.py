import random

from django.shortcuts import render
from friend.models import *  # models
from django.shortcuts import render, get_object_or_404 # communication with the data base
from django.db.models import Q # advanced query conditions
from django.http import HttpResponse, HttpResponseRedirect
from friend.forms import *
from django.conf.urls.static import static

from django.urls import reverse

#for login
from django.contrib.auth.decorators import login_required

@login_required
def attack_friend(request, defender_id):
    defender = get_object_or_404(Friend, pk=defender_id)
    attacker = request.user.friend

    comments = Friend_Page_Comment.objects.filter(commented_on=defender) # Gets all comments related to the friend
    form = CommentForm()


    if request.method == 'GET':

        if attacker.energy < 5: #send them back
            context = {
                'friend': defender,
                'image': defender.profile_image,
                'comments': comments,
                'is_users_page': False,
                'form': form,
                'show_info': defender.show_info,

                'out_of_energy': True, # and give them this
                 }
            return render(request, 'friend_page.html', context)

        # this is like a whole pie made from both attack and defense
        # the attacker is the first portion of the pie, and the defender
        # is the added on peice of the pie. The randomNum is a routlette thing
        # the defender zone is the last half of the pie while the attacker zone
        # is the first half of the pie and depending on where the random number falls
        # determines the winner.

        total = defender.defense + attacker.attack


        randNum = random.randint(1,total)

        # a bit over complicated for now, but i think im gonna add on
        # some things to it or something, so it may stay as is!
        if randNum >= attacker.attack: # the defender has won
            attack_success = False
            diamonds_stolen = 0

        else: # the attacker has won
            attack_success = True
            diamonds_stolen = int((defender.diamonds / 100) * 10)

            defender.diamonds -= diamonds_stolen
            defender.save()

            attacker.diamonds += diamonds_stolen



        # create a new attack objects to record this attacking
        attacker.energy -= 5
        attacker.save()

        newAttack = Attack(attack_success=attack_success,
                           attacker=attacker,
                           defender=defender,
                           diamonds_stolen=diamonds_stolen)
        newAttack.save()


    context = {
        'newAttack': newAttack,

        'friend': defender,
        'image': defender.profile_image,
        'comments': comments,
        'is_users_page': False,
        'form': form,
        'show_info': defender.show_info,
         }

    return render(request, 'friend_page.html', context)

@login_required
def market(request):


    items = Item.objects.all()

    context = {
        'items': items,
        }

    return render(request, 'market.html', context)

@login_required
def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    friend = request.user.friend

    friend.diamonds -= item.cost

    if friend.diamonds < 0:
        items = Item.objects.all()
        cannot_buy = True

        friend.diamonds += item.cost

        context = {
            'items': items,
            'cannot_buy': cannot_buy,
            }

        return render(request, 'market.html', context)

    if item.attack_boost != None:
        friend.attack += item.attack_boost
    if item.defense_boost != None:
        friend.defense += item.defense_boost
    if item.energy_boost != None:
        friend.energy += item.energy_boost
    if item.diamond_gen_boost != None:
        friend.diamond_gen += item.diamond_gen_boost

    if friend.energy > 100:
        friend.energy = 100

    if friend.diamonds < 0:
        items = Item.objects.all()
        cannot_buy = True

        context = {
            'items': items,
            'cannot_buy': cannot_buy,
            }
        cannot_buy = True

        return render(request, 'market.html', context)

    friend.save()

    return HttpResponseRedirect(reverse('market'))
