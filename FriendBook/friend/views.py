from django.shortcuts import render
from friend.models import *  # models
from django.shortcuts import render, get_object_or_404 # communication with the data base
from django.db.models import Q # advanced query conditions
from django.http import HttpResponse, HttpResponseRedirect
from friend.forms import *
from django.conf.urls.static import static

#for login
from django.contrib.auth.decorators import login_required

from django.urls import reverse

# Create your views here.
# ^~~ thank you django, i shall!


##### index #####
# no place like home. :> #
def index(request): # homepage
    context = {
        }

    return render(request, 'index.html', context)




##### friend_page #####
@login_required
def friend_page(request, friend_id):

    friend = get_object_or_404(Friend, pk=friend_id)

    is_users_page = False

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            newComment = Friend_Page_Comment(commenter=request.user.friend,
                                             comment=form.cleaned_data['comment'],
                                             commented_on=friend,)
            newComment.comment = newComment.comment.strip()
            newComment.save()

    # Check to see if this is the logged in
    # users friend page.
    if request.user.friend.id == friend.id:
        is_users_page = True

    comments = Friend_Page_Comment.objects.filter(commented_on=friend) # Gets all comments related to the friend
    form = CommentForm()

    context = {
        'friend': friend,
        'image': friend.profile_image,
        'comments': comments,
        'is_users_page': is_users_page,
        'form': form,
        'show_info': friend.show_info,
        }
    return render(request, 'friend_page.html', context)

##### topic page #####
@login_required
def topic_page(request, topic_id):

    topic = get_object_or_404(Topic, pk=topic_id)

    # if they clicked the submit button and are making a comment
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            newComment = Topic_Page_Comment(commenter=request.user.friend,
                                             comment=form.cleaned_data['comment'],
                                             commented_on=topic,)
            newComment.comment = newComment.comment.strip()
            newComment.save()


    comments = Topic_Page_Comment.objects.filter(commented_on=topic) # Gets all comments related to the topic

    form = TopicCommentForm()

    context = {
        'topic': topic,
        'comments': comments,
        'form': form,
        }
    return render(request, 'topic_page.html', context)

def topic_search(request):
    if 'search_string' in request.GET:
        search = request.GET['search_string']
        search = search.strip()
        topics = Topic.objects.filter(title__icontains=search)
    else:
        topics = Topic.objects.order_by('title')
        search = None

    context = {
        'topics': topics,
        'search': search,
        }


    return render(request, 'topic_search.html', context)

##### add topic page #####
@login_required
def add_topic(request):

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            newTopic = Topic(creator=request.user.friend,
                             title=form.cleaned_data['topic'])
            newTopic.save()

            return HttpResponseRedirect(reverse('topic_page',
                                                    kwargs={ 'topic_id': newTopic.id }))

    else:
        form = TopicForm()

    context = {
        'form': form,
        }

    return render(request, 'add_topic.html', context)

##### comment page #####
@login_required
def comment_page(request):

    if request.method == 'POST':
        # create another comment
        # and go back to the comment page
        form = CommentForm(request.POST)
        if form.is_valid():
            newComment = Comment_Page_Comment(comment=form.cleaned_data['comment'],
                                              commenter=request.user.friend,)
            newComment.comment = newComment.comment.strip()
            newComment.save()

    comments = Comment_Page_Comment.objects.all()

    form = CommentForm()
    context = {
        'comments': comments,
        'form': form,
        }

    return render(request, 'comment_page.html', context)

##### ladder #####
# the ladder page displays all of the friends #
# sorted by their level and diamonds          #
# the first friend should be the person in    #
# first place with the last person being in   #
# last place                                  #
@login_required
def ladder(request):
    # should be in acending order by attack defense diamond_gen and diamonds
    friends = Friend.objects.order_by('attack', 'defense', 'diamond_gen', 'diamonds')

    friends = friends.reverse()

    context = {
        'friends': friends
        }
    return render(request, 'ladder.html', context)

### edit_friend_picture ###
# for uploading images
@login_required
def edit_friend_picture(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)

    if request.method == 'POST':
        form = FriendPictureForm(request.POST, request.FILES)
        if form.is_valid():
              friend.profile_image = form.instance.profile_image
              friend.save()

        return HttpResponseRedirect(reverse('friend_page',
                                                    kwargs={ 'friend_id': friend.id }))
    else:
        # display the form
         form = FriendPictureForm()

         context = {
             'friend': friend,
             'form': form,
             }

    return render(request, 'edit_friend_picture.html', context)


def edit_user_info(request, friend_id):  ############### WORK IN PROGRESS ############
    friend = get_object_or_404(Friend, pk=friend_id)

    edited = False;

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            friend.user.username = form.cleaned_data['username'];
            friend.user.email = form.cleaned_data['email'];
            friend.user.set_password(form.cleaned_data['password']);
            friend.user.first_name = form.cleaned_data['first_name'];
            friend.user.last_name = form.cleaned_data['last_name'];
            friend.user.save()
            edited = True;

    else:
        form = UserForm()

    context = {
        'form': form,
        'edited': edited,
        }
    return render(request, 'edit_user_info.html', context)



def login(request):
    context = {
        }

    return HttpResponseRedirect(request, 'registration\login.html', context)

def add_user(request):
    registered = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            newUser = User.objects.create_user(username=form.cleaned_data['username'],
                           email=form.cleaned_data['email'],
                           password=form.cleaned_data['password'],
                           first_name=form.cleaned_data['first_name'],
                           last_name=form.cleaned_data['last_name'])
            newUser.save()

            # create a friend to associate with the user
            userFriend = Friend(user=newUser,
                                level=1,
                                diamonds=100,
                                energy=100,
                                attack=10,
                                defense=10)
            userFriend.save()
            registered = True



    else:
        form = UserForm()

    context = {
        'form': form,
        'registered': registered,
        }
    return render(request, 'add_user.html', context)

# for the logged in users specific page for them
@login_required
def active_friend_page(request):

    friend = get_object_or_404(Friend, pk=request.user.friend.id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            newComment = Friend_Page_Comment(commenter=request.user.friend,
                                             comment=form.cleaned_data['comment'],
                                             commented_on=friend,)
            newComment.comment = newComment.comment.strip()
            newComment.save()



    form = CommentForm()
    comments = Friend_Page_Comment.objects.filter(commented_on=friend)

    context = {
        'friend': friend,
        'image': friend.profile_image,
        'comments': comments,
        'is_users_page': True,
        'form': form,
        'show_info': friend.show_info,
        }

    return render(request, 'friend_page.html', context)


# is_users_page will be true if
# the comment is deleted on the users specific page
def del_fp_comment(request):

    # post parameters should contain:
    # comment_id, is_users_page, friend_id - of the current friends page.
    if request.method == 'POST':
        comment_id = request.POST['comment_id']
        is_users_page = request.POST['is_users_page']
        friend_id = request.POST['friend_id']

        comment = get_object_or_404(Friend_Page_Comment, pk=comment_id)
        comment.delete()

        if is_users_page:
            return HttpResponseRedirect(reverse('active_friend_page'))
        else:
            return HttpResponseRedirect(reverse('friend_page',
                                        kwargs={ 'friend_id': friend_id }))
    else:
        return HttpResponseRedirect(reverse('friend_page',
                                        kwargs={ 'friend_id': friend_id }))

# delete topic page comment
def del_tp_comment(request):

    # post parameters should contain:
    # comment_id, is_users_page, friend_id - of the current friends page.
    if request.method == 'POST':
        comment_id = request.POST['comment_id']
        topic_id = request.POST['topic_id']

        comment = get_object_or_404(Topic_Page_Comment, pk=comment_id)
        comment.delete()

        return HttpResponseRedirect(reverse('topic_page',
                                        kwargs={ 'topic_id': topic_id }))

def del_cp_comment(request):
    if request.method == 'POST':
        comment_id = request.POST['comment_id']
        comment = get_object_or_404(Comment_Page_Comment, pk=comment_id)
        comment.delete()

        return HttpResponseRedirect(reverse('comment_page'))
    else:
        return HttpResponseRedirect(reverse('comment_page'))

def friend_search(request):
    if 'search_string' in request.GET:
        search = request.GET['search_string']
        search = search.strip()
        users = User.objects.filter(Q(username__icontains=search) | Q(first_name__icontains=search) | Q(last_name__icontains=search)).order_by('first_name', 'last_name', 'username')

    else:
        users = User.objects.order_by('first_name','username')
        search = None

    context = {
        'users': users,
        'search': search,
        }


    return render(request, 'friend_search.html', context)

# reverses the current status of show_info on the friend
def show_info(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)

    friend.show_info = not(friend.show_info)
    friend.save()

    return HttpResponseRedirect(reverse('friend_page',
                                         kwargs={ 'friend_id': friend_id }))
