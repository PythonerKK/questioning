# Generated by Django 2.1.9 on 2019-09-01 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uid')),
                ('message', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('unread', models.BooleanField(db_index=True, default=True, verbose_name='是否未读')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='接受者')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='发送者')),
            ],
            options={
                'verbose_name': '私信',
                'verbose_name_plural': '私信',
                'ordering': ('-created_at',),
            },
        ),
    ]