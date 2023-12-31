# Generated by Django 4.2.7 on 2023-11-30 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Death date')),
                ('biography', models.TextField(verbose_name='Biography')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], verbose_name='Rating')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True, verbose_name='Borrow date')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='Return date')),
                ('returned', models.BooleanField(default=False, verbose_name='Is returned')),
            ],
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='department',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='department',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='book',
            name='Availability',
            field=models.BooleanField(default=True, verbose_name='availability'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=123456789, max_length=13, unique=True, verbose_name='ISBN Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='xd', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='who_is',
            field=models.CharField(choices=[('Librarian', 'Librarian'), ('Reader', 'Reader')], default='Reader', verbose_name='Role'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Magazine',
        ),
        migrations.AddField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Book'),
        ),
        migrations.AddField(
            model_name='loan',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reader'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Book'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reader'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author', verbose_name='Author'),
        ),
    ]
