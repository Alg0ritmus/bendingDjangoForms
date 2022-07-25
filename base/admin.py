from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(Secret)
admin.site.register(FriendShip)
admin.site.register(Article)
admin.site.register(Archive)
admin.site.register(Comment)
admin.site.register(Pinned)
admin.site.register(UploadFile)
