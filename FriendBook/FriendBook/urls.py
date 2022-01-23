from django.urls import include, re_path
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
    # re_path(r'^$', 'FriendBook.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    # regular view.py urls
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', friend.views.index, name='index'),
    re_path(r'^friend_page/(?P<friend_id>\d+)$', friend.views.friend_page, name='friend_page'),
    re_path(r'^topic_page/(?P<topic_id>\d+)$', friend.views.topic_page, name='topic_page'),
    re_path(r'^add_topic$', friend.views.add_topic, name='add_topic'),
    re_path(r'ladder$', friend.views.ladder, name='ladder'),
    re_path(r'comment_page$', friend.views.comment_page, name='comment_page'),
    re_path(r'^edit_friend_picture/(?P<friend_id>\d+)$', friend.views.edit_friend_picture, name='edit_friend_picture'),
    re_path(r'^edit_user_info/(?P<friend_id>\d+)$', friend.views.edit_user_info, name='edit_user_info'), ######## WORK IN PROGRESS ####
    re_path(r'^login$', friend.views.login, name='login'),
    re_path(r'^add_user$', friend.views.add_user, name='add_user'),
    re_path(r'^active_friend_page$', friend.views.active_friend_page, name='active_friend_page'),
    re_path(r'^del_fp_comment$', friend.views.del_fp_comment, name='del_fp_comment'),
    re_path(r'^del_cp_comment$', friend.views.del_cp_comment, name='del_cp_comment'),
    re_path(r'^del_tp_comment$', friend.views.del_tp_comment, name='del_tp_comment'),
    re_path(r'^friend_search$', friend.views.friend_search, name='friend_search'),
    re_path(r'^topic_search$', friend.views.topic_search, name='topic_search'),
    re_path(r'^show_info/(?P<friend_id>\d+)$', friend.views.show_info, name='show_info'),

    # ajax urls
    re_path(r'^ajax_comments_status$', friend.ajax_views.ajax_comments_status, name='ajax_comments_status'),
    re_path(r'ajax_energy_status$', friend.ajax_views.ajax_energy_status, name='ajax_energy_status'),
    re_path(r'^ajax_diamond_status$', friend.ajax_views.ajax_diamond_status, name='ajax_diamond_status'),

    # gameplay urls
    re_path(r'^attack_friend/(?P<defender_id>\d+)$', friend.game_views.attack_friend, name='attack_friend'),
    re_path(r'^market$', friend.game_views.market, name='market'),
    re_path(r'^buy_item/(?P<item_id>\d+)$', friend.game_views.buy_item, name='buy_item'),


    # login page
    re_path('^', include('django.contrib.auth.urls')),

]


# for image upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
