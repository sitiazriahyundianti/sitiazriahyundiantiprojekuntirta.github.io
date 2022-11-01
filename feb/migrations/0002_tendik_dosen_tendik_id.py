# Generated by Django 4.1.1 on 2022-10-05 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.IntegerField(null=True)),
                ('nama', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('alamat_rumah', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='dosen',
            name='tendik_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.tendik'),
        ),
    ]
