# Generated by Django 3.1.7 on 2021-04-09 08:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import qx_base.qx_core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('account', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='账号')),
                ('mobile', models.CharField(blank=True, db_index=True, max_length=25, null=True, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('last_access_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最近访问时间')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('type', models.CharField(db_index=True, max_length=10, verbose_name='类型')),
                ('object_id', models.PositiveIntegerField(db_index=True, null=True, verbose_name='对象Id')),
                ('name', models.CharField(default='', max_length=50, verbose_name='名称')),
                ('user_id', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='用户Id')),
            ],
            options={
                'verbose_name': 'Baby',
                'verbose_name_plural': 'Baby',
            },
        ),
        migrations.CreateModel(
            name='GPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('star_count', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Post',
            },
            bases=(models.Model, qx_base.qx_core.models.ModelCountMixin),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user', verbose_name='用户')),
                ('name', models.CharField(default='', max_length=50, verbose_name='用户名称')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='TGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('perms', models.ManyToManyField(to='user.GPermission', verbose_name='权限')),
            ],
        ),
        migrations.AddField(
            model_name='gpermission',
            name='groups',
            field=models.ManyToManyField(to='user.TGroup', verbose_name='组'),
        ),
    ]
