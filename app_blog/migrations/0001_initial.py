# Generated by Django 4.2 on 2023-06-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('preview', models.ImageField(default='posts/default.jpg', upload_to='posts/', verbose_name='Изображение (превью)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'posts',
                'ordering': ['created_at'],
            },
        ),
    ]