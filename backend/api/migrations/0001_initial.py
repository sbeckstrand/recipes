# Generated by Django 4.0.1 on 2022-01-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ingredients', models.CharField(max_length=800)),
                ('picture', models.FileField(upload_to='')),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=10)),
                ('prep_time', models.PositiveIntegerField()),
                ('cook_time', models.PositiveIntegerField()),
                ('guide', models.TextField()),
            ],
        ),
    ]
