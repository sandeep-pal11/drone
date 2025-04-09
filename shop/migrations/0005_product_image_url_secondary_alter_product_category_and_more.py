# Generated by Django 5.1.3 on 2025-01-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_category_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url_secondary',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
