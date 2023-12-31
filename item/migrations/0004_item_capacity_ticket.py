# Generated by Django 5.0 on 2023-12-10 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_date_item_venue_alter_item_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='item.item')),
            ],
        ),
    ]
