# Generated by Django 4.0.1 on 2022-02-18 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blood', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donatedDate', models.DateField(auto_now=True)),
                ('expiryDate', models.DateField()),
                ('bloodgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.bloodgroup')),
                ('dondatetBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
