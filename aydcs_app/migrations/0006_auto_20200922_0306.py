# Generated by Django 3.1.1 on 2020-09-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aydcs_app', '0005_auto_20200922_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursVa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursValid', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='essai',
            name='coursValid',
        ),
    ]
