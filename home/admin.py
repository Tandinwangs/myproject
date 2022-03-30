

# Register your models here.
# from .models import Room, Topic, Message 

# admin.site.register(Room)
# admin.site.register(Topic)
# admin.site.register(Message)
# admin.site.register(Book_QueueNo)

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Session, User, Background, Equipments, Footer, Video
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Session)
admin.site.register(Background)
admin.site.register(Equipments)
admin.site.register(Footer)
admin.site.register(Video, AdminVideo)
admin.site.unregister(Group)
