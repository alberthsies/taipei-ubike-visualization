# Generated by Django 2.2.2 on 2019-07-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vis', '0003_auto_20190719_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoraindata',
            name='elementName',
        ),
        migrations.AddField(
            model_name='autoraindata',
            name='num',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autoweatherdata',
            name='num',
            field=models.BigIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bureauweatherdata',
            name='num',
            field=models.BigIntegerField(default=None),
            preserve_default=False,
        ),
    ]
