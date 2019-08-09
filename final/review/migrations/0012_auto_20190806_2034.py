# Generated by Django 2.1.1 on 2019-08-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0011_auto_20190806_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='result',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='cnt',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='fun',
            field=models.CharField(choices=[('★★★★', '★★★★'), ('★★', '★★'), ('★', '★'), ('★★★', '★★★'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='runningtime',
            field=models.CharField(choices=[('★★★★', '★★★★'), ('★★', '★★'), ('★', '★'), ('★★★', '★★★'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='sum',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='volume',
            field=models.CharField(choices=[('★★★★', '★★★★'), ('★★', '★★'), ('★', '★'), ('★★★', '★★★'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
    ]