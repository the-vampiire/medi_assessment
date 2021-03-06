# Generated by Django 2.0.2 on 2018-03-22 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_add_categories_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.Category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
