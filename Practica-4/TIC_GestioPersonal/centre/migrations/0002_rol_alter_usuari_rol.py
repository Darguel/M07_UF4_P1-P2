# Generated by Django 4.2.11 on 2024-05-07 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usuari',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.rol'),
        ),
    ]
