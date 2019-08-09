# Generated by Django 2.1.1 on 2019-08-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20190806_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fun',
            field=models.CharField(choices=[('3', '★★★'), ('4', '★★★★'), ('2', '★★'), ('5', '★★★★★'), ('1', '★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='runningtime',
            field=models.CharField(choices=[('3', '★★★'), ('4', '★★★★'), ('2', '★★'), ('5', '★★★★★'), ('1', '★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='volume',
            field=models.CharField(choices=[('3', '★★★'), ('4', '★★★★'), ('2', '★★'), ('5', '★★★★★'), ('1', '★')], default='★', max_length=5),
        ),
    ]
