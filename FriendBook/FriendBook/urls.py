from django.conf.urls import include, url
from django.contrib import admin

### for image upload ###
from django.conf.urls.static import static

import friend.views
import friend.ajax_views
import friend.game_views
from FriendBook import settings
########################

urlpatterns = [
    # Examples:
    # url(r'^$', 'FriendBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # regular view.py urls
    url(r'^admin/', admin.site.urls),
    url(r'^$', friend.views.index, name='index'),
    url(r'^friend_page/(?P<friend_id>\d+)$', friend.views.friend_page, name='friend_page'),
    url(r'^topic_page/(?P<topic_id>\d+)$', friend.views.topic_page, name='topic_page'),
    url(r'^add_topic$', friend.views.add_topic, name='add_topic'),
    url(r'ladder$', friend.views.ladder, name='ladder'),
    url(r'comment_page$', friend.views.comment_page, name='comment_page'),
    url(r'^edit_friend_picture/(?P<friend_id>\d+)$', friend.views.edit_friend_picture, name='edit_friend_picture'),
    url(r'^edit_user_info/(?P<friend_id>\d+)$', friend.views.edit_user_info, name='edit_user_info'), ######## WORK IN PROGRESS ####
    url(r'^login$', friend.views.login, name='login'),
    url(r'^add_user$', friend.views.add_user, name='add_user'),
    url(r'^active_friend_page$', friend.views.active_friend_page, name='active_friend_page'),
    url(r'^del_fp_comment$', friend.views.del_fp_comment, name='del_fp_comment'),
    url(r'^del_cp_comment$', friend.views.del_cp_comment, name='del_cp_comment'),
    url(r'^del_tp_comment$', friend.views.del_tp_comment, name='del_tp_comment'),
    url(r'^friend_search$', friend.views.friend_search, name='friend_search'),
    url(r'^topic_search$', friend.views.topic_search, name='topic_search'),
    url(r'^show_info/(?P<friend_id>\d+)$', friend.views.show_info, name='show_info'),

    # ajax urls
    url(r'^ajax_comments_status$', friend.ajax_views.ajax_comments_status, name='ajax_comments_status'),
    url(r'ajax_energy_status$', friend.ajax_views.ajax_energy_status, name='ajax_energy_status'),
    url(r'^ajax_diamond_status$', friend.ajax_views.ajax_diamond_status, name='ajax_diamond_status'),

    # gameplay urls
    url(r'^attack_friend/(?P<defender_id>\d+)$', friend.game_views.attack_friend, name='attack_friend'),
    url(r'^market$', friend.game_views.market, name='market'),
    url(r'^buy_item/(?P<item_id>\d+)$', friend.game_views.buy_item, name='buy_item'),


    # login page
    url('^', include('django.contrib.auth.urls')),

]


# for image upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
