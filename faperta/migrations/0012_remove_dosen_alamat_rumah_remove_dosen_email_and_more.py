# Generated by Django 4.1.1 on 2022-10-05 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0011_remove_dosen_mahasiswa_id_remove_dosen_tendik_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='alamat_rumah',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='fakultas',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='prodi',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='tanggal_lahir',
        ),
    ]
