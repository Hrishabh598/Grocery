# Generated by Django 4.2.1 on 2023-07-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
