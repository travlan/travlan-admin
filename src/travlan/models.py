# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    num = models.AutoField(primary_key=True)
    post_num = models.ForeignKey('Post', models.DO_NOTHING, db_column='post_num', blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    score = models.CharField(max_length=1, blank=True, null=True)
    member_num = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_num', blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

    def __str__(self):
        return self.title


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    num = models.AutoField(primary_key=True)
    region = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'
    
    def __str__(self):
        return self.region


class Member(models.Model):
    num = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=4, blank=True, null=True)
    created_date = models.DateField()
    id = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=16)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'member'
        unique_together = (('id', 'nickname', 'email'),)
    
    def __str__(self):
        return self.id


class MemberInfo(models.Model):
    num = models.OneToOneField(Member, db_column='num', primary_key=True, on_delete=models.CASCADE)
    age = models.CharField(max_length=2, blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    region_num = models.ForeignKey(Location, db_column='region_num', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'member_info'
    
    def __str__(self):
        return self.num.id


class MemberNote(models.Model):
    num = models.AutoField(primary_key=True)
    send_user = models.ForeignKey(Member,db_column='send_user', related_name='note_send_user', blank=True, null=True, on_delete=models.SET_NULL)
    revice_user = models.ForeignKey(Member, db_column='revice_user', related_name='note_revice_user', blank=True, null=True, on_delete=models.SET_NULL)
    created_date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    is_read = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_note'
    
    def __str__(self):
        return self.content


class MemberNotify(models.Model):
    num = models.AutoField(primary_key=True)
    member_num = models.ForeignKey(Member, db_column='member_num', blank=True, null=True, on_delete=models.SET_NULL)
    post_num = models.ForeignKey('Post', db_column='post_num', blank=True, null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    is_read = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_notify'
    
    def __str__(self):
        return self.content


class MemberScrap(models.Model):
    num = models.AutoField(primary_key=True)
    member_num = models.ForeignKey(Member, db_column='member_num', blank=True, null=True, on_delete=models.SET_NULL)
    post_num = models.ForeignKey('Post', db_column='post_num', blank=True, null=True, on_delete=models.SET_NULL)
    memo = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_scrap'
    
    def __str__(self):
        return self.memo


class Post(models.Model):
    post_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    region_num = models.ForeignKey(Location, db_column='region_num', blank=True, null=True, on_delete=models.SET_NULL)
    season = models.CharField(max_length=1, blank=True, null=True)
    time = models.CharField(max_length=1, blank=True, null=True)
    cost = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    thumbnail = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    member_num = models.ForeignKey(Member, db_column='member_num', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'post'

    def __str__(self):
        return self.title

class Report(models.Model):
    num = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    send_user = models.ForeignKey(Member, db_column='send_user', related_name='send_user', blank=True, null=True, on_delete=models.SET_NULL)
    receive_user = models.ForeignKey(Member, db_column='receive_user', related_name='receive_user', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'report'

    def __str__(self):
        return self.receive_user