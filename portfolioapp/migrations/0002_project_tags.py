# Generated by Django 5.1 on 2024-09-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(choices=[('python', 'Python'), ('django', 'Django'), ('flask', 'Flask'), ('ia', 'Ia'), ('odoo', 'Odoo')], default='python', max_length=10),
        ),
    ]
