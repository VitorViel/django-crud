# Generated by Django 4.0.2 on 2022-02-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('obs', models.TextField(null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.categoria')),
            ],
            options={
                'verbose_name_plural': 'Transações',
            },
        ),
    ]
