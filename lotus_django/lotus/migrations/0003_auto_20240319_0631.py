# Generated by Django 2.2 on 2024-03-19 06:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lotus', '0002_auto_20240319_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_journal', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=255)),
                ('question_type', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('frequency', models.CharField(default='daily', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('colourscheme', models.IntegerField(default=1)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('text_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=30)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Question', unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.User', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('memory_id', models.AutoField(primary_key=True, serialize=False)),
                ('emotion', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=60)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='LikertAnswer',
            fields=[
                ('likert_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Entry')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.User'),
        ),
    ]
