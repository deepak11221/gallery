# Generated by Django 4.1.7 on 2023-05-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='graph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='graph.graph'),
        ),
    ]
