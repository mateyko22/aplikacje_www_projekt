# Generated by Django 4.2.7 on 2023-12-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_author_biography_alter_bookreview_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due date'),
        ),
    ]