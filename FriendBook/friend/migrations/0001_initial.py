# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_success', models.BooleanField(default=False)),
                ('diamonds_stolen', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Page_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_info', models.BooleanField(default=False)),
                ('level', models.IntegerField()),
                ('diamonds', models.IntegerField()),
                ('energy', models.PositiveIntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('diamond_gen', models.IntegerField(default=1)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend_Page_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=300)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('attack_boost', models.IntegerField(blank=True, null=True)),
                ('defense_boost', models.IntegerField(blank=True, null=True)),
                ('energy_boost', models.IntegerField(blank=True, null=True)),
                ('diamond_gen_boost', models.IntegerField(blank=True, null=True)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_bought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friend.Item')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friend.Friend')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend')),
            ],
        ),
        migrations.CreateModel(
            name='Topic_Page_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Topic')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend')),
            ],
        ),
        migrations.AddField(
            model_name='comment_page_comment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friend.Friend'),
        ),
        migrations.AddField(
            model_name='attack',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend'),
        ),
        migrations.AddField(
            model_name='attack',
            name='defender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='friend.Friend'),
        ),
    ]