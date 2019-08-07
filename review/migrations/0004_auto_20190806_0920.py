# Generated by Django 2.1.1 on 2019-08-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time',
            field=models.CharField(choices=[('★★★★', '★★★★'), ('★★', '★★'), ('★', '★'), ('★★★', '★★★'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.CharField(choices=[('★★★★', '★★★★'), ('★★', '★★'), ('★', '★'), ('★★★', '★★★'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
    ]
