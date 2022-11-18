# Generated by Django 4.1.3 on 2022-11-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=10)),
                ('unique_code', models.CharField(max_length=10, unique=True)),
                ('Size', models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30')], default=10, max_length=10)),
                ('Quality', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], default='high', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colour', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('black', 'black')], default='red', max_length=20)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
    ]
