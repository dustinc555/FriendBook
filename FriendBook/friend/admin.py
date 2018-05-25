from django.contrib import admin
from friend.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Friend)
admin.site.register(Topic)
admin.site.register(Friend_Page_Comment)
admin.site.register(Topic_Page_Comment)
admin.site.register(Comment_Page_Comment)
admin.site.register(Item)
admin.site.register(Purchase)
