# Generated by Django 3.2.18 on 2023-03-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='item_image',
            field=models.CharField(default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg?compress=1&resize=400x300&vertical=top', max_length=1000),
        ),
    ]
