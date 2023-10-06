# Generated by Django 4.2.5 on 2023-10-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
                ('content3', models.TextField()),
                ('item1', models.TextField()),
                ('item2', models.TextField()),
                ('item3', models.TextField()),
                ('image', models.ImageField(default='service.jpg', upload_to='service')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='root.category')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]
