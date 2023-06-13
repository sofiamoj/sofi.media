# Generated by Django 4.2.1 on 2023-05-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('published_year', models.IntegerField(default=1400)),
                ('exists', models.BooleanField(default=True)),
                ('book_type', models.CharField(choices=[('EL', 'electronic'), ('LO', 'physical book')], max_length=2)),
            ],
        ),
    ]
