# Generated by Django 4.1.2 on 2022-12-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_delete_imagemessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
