# Generated by Django 4.1.1 on 2022-10-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0002_alter_dosen_nip_alter_dosen_tanggal_lahir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='NIP',
            field=models.IntegerField(null=True),
        ),
    ]