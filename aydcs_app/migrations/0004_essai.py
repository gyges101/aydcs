# Generated by Django 3.1.1 on 2020-09-21 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aydcs_app', '0003_auto_20200921_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='essai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=50)),
                ('cours', models.CharField(choices=[('Francais', 'Francais'), ('Arabe', 'Arabe'), ('Englais', 'Englais'), ('Philosophie', 'Philosophie'), ('Math', 'Math'), ('Physique', 'Physique'), ('SVT', 'SVT'), ('Histoire-Geo', 'Histoire-Geo'), ('Compta', 'Compta'), ('Economie', 'Economie')], max_length=20)),
            ],
        ),
    ]
