# Generated by Django 3.0.6 on 2020-06-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0002_auto_20200624_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='administration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shift',
            name='name',
            field=models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=50),
        ),
    ]