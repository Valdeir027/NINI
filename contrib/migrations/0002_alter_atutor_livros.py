# Generated by Django 4.2.4 on 2023-09-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_alter_capitulo_livro_alter_capitulo_titulo_and_more'),
        ('contrib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atutor',
            name='livros',
            field=models.ManyToManyField(blank=True, to='livro.livro'),
        ),
    ]
