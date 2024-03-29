# Generated by Django 3.1 on 2021-02-21 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_reportedpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportType', models.CharField(max_length=20)),
                ('reportedBy', models.CharField(max_length=150)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
            ],
        ),
    ]
