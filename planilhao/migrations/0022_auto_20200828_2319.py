# Generated by Django 3.0.8 on 2020-08-29 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilhao', '0021_auto_20200828_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impressora',
            name='catalogo',
            field=models.FileField(default='catalogos/None/no-img.jpg', null=True, upload_to='catalogos/'),
        ),
        migrations.AlterField(
            model_name='impressora',
            name='foto',
            field=models.ImageField(default='imagens/None/no-img.jpg', null=True, upload_to='imagens/'),
        ),
        migrations.AlterField(
            model_name='multifuncional',
            name='catalogo',
            field=models.FileField(default='catalogos/None/no-img.jpg', null=True, upload_to='catalogos/'),
        ),
        migrations.AlterField(
            model_name='multifuncional',
            name='foto',
            field=models.ImageField(default='imagens/None/no-img.jpg', null=True, upload_to='imagens/'),
        ),
        migrations.AlterField(
            model_name='multifuncional_producao',
            name='catalogo',
            field=models.FileField(default='catalogos/None/no-img.jpg', null=True, upload_to='catalogos/'),
        ),
        migrations.AlterField(
            model_name='multifuncional_producao',
            name='foto',
            field=models.ImageField(default='imagens/None/no-img.jpg', null=True, upload_to='imagens/'),
        ),
    ]
