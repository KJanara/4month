# Generated by Django 3.2.23 on 2023-11-27 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='post.product'),
        ),
    ]
