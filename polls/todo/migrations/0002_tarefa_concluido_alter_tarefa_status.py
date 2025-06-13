# Generated by Django 5.1.4 on 2025-01-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(choices=[('concluido', 'concluido'), ('em andamento', 'em andamento'), ('pendente', 'pendente')], default='pendente', max_length=20, null=True),
        ),
    ]
