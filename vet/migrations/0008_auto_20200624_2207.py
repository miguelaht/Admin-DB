# Generated by Django 3.0.6 on 2020-06-24 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0007_auto_20200624_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='surgery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vet.Surgery'),
        ),
    ]