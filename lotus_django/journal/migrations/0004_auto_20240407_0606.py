# Generated by Django 2.2 on 2024-04-07 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_entry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='journal_id',
        ),
        migrations.AddField(
            model_name='journal',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='journal',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
