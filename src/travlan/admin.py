from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(MemberInfo)
admin.site.register(MemberNote)
admin.site.register(MemberNotify)
admin.site.register(MemberScrap)
admin.site.register(Post)
admin.site.register(Report)