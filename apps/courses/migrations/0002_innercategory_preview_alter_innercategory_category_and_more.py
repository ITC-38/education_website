# Generated by Django 4.2.4 on 2023-08-22 10:20

from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='innercategory',
            name='preview',
            field=models.ImageField(default=pathlib.PurePosixPath('/home/singlet0n/PycharmProjects/education_platform/staticfiles/global/img/default_photo_bg.png'), upload_to='photos/inner_categories'),
        ),
        migrations.AlterField(
            model_name='innercategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inner_categories', to='courses.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Language name'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='native',
            field=models.BooleanField(default=True, verbose_name='Native'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Level name'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='objectivefeatures',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Objective Feature name'),
        ),
    ]
