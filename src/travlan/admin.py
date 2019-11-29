from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MemberInfo)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['num', 'send_user', 'receive_user', 'content', 'created_date']

@admin.register(MemberNotify)
class NotifyAdmin(admin.ModelAdmin):
    list_display = ['num', 'member_num', 'content', 'is_read', 'created_date']

@admin.register(MemberNote)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['num', 'send_user', 'revice_user', 'is_read', 'created_date']

@admin.register(Location)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['num', 'region']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['num', 'post_num', 'member_num', 'title', 'score', 'created_date']
    list_filter = ['member_num']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['num', 'id', 'nickname', 'email', 'grade', 'created_date']
    list_filter = ['grade']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_num', 'member_num', 'title', 'created_date']
    list_display_links = ['post_num', 'title']
    list_filter = ['member_num']

@admin.register(MemberScrap)
class ScarpAdmin(admin.ModelAdmin):
    list_display = ['num', 'member_num', 'post_num', 'created_date']
    list_filter = ['member_num']