# Generated by Django 3.2.18 on 2023-03-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=240)),
                ('item_description', models.CharField(max_length=240)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
