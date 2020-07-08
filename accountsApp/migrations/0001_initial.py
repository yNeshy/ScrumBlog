# Generated by Django 2.2.11 on 2020-03-20 20:53

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]