# Generated by Django 4.1 on 2022-08-10 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('no_calle', models.IntegerField()),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.domicilio'),
        ),
    ]
