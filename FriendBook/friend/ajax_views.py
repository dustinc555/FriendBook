from django.shortcuts import render
from friend.models import *  # models
from django.shortcuts import render, get_object_or_404 # communication with the data base
from django.db.models import Q # advanced query conditions
from django.http import HttpResponse, HttpResponseRedirect
from friend.forms import *
from django.conf.urls.static import static

#for login
from django.contrib.auth.decorators import login_required



@login_required
def ajax_comments_status(request):
    comments = Comment_Page_Comment.objects.all()

    context = {
        'comments': comments,
        }

    return render(request, 'ajax/comments_status.txt', context)

@login_required
def ajax_energy_status(request):
    friend = request.user.friend
    if friend.energy < 100:
        friend.energy += 1
    friend.save()
    context = {
        'friend': friend,
        }

    return render(request, 'ajax/energy_status.txt', context)

@login_required
def ajax_diamond_status(request):
    friend = request.user.friend
    friend.diamonds += friend.diamond_gen
    friend.save()

    diamonds = friend.diamonds


    context = {
        'diamonds': diamonds,
        }

    return render(request, 'ajax/diamond_status.txt', context)
