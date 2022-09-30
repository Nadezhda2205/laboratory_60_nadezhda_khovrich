# Generated by Django 4.1.1 on 2022-09-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(max_length=2000, null=True, verbose_name='Описание')),
                ('photo', models.TextField(max_length=2000, null=True, verbose_name='Фото')),
                ('category', models.CharField(choices=[('milk', 'Молочные'), ('meat', 'Мясные'), ('bread', 'Хлебобулочные'), ('juice', 'Соки'), ('other', 'Разное')], default='other', max_length=10, verbose_name='Категория')),
                ('balance', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
        ),
    ]