# Generated by Django 2.2.6 on 2019-10-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saludar', '0002_auto_20191016_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greet',
            name='name_set',
        ),
        migrations.RemoveField(
            model_name='greet',
            name='title',
        ),
        migrations.AddField(
            model_name='greet',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='greet',
            name='greet',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
