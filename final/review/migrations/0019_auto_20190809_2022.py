# Generated by Django 2.2.4 on 2019-08-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0018_auto_20190809_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fun',
            field=models.CharField(choices=[('★★', '★★'), ('★★★★★', '★★★★★'), ('★★★★', '★★★★'), ('★★★', '★★★'), ('★', '★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='runningtime',
            field=models.CharField(choices=[('★★', '★★'), ('★★★★★', '★★★★★'), ('★★★★', '★★★★'), ('★★★', '★★★'), ('★', '★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='total',
            field=models.CharField(choices=[('★★', '★★'), ('★★★★★', '★★★★★'), ('★★★★', '★★★★'), ('★★★', '★★★'), ('★', '★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='volume',
            field=models.CharField(choices=[('★★', '★★'), ('★★★★★', '★★★★★'), ('★★★★', '★★★★'), ('★★★', '★★★'), ('★', '★')], default='★', max_length=5),
        ),
    ]