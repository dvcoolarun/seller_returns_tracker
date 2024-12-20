# Generated by Django 4.2.16 on 2024-12-01 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('returns', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisputeCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispute_reason', models.TextField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('UNDER_REVIEW', 'Under Review'), ('CLOSED', 'Closed'), ('RESOLVED', 'Resolved'), ('REJECTED', 'Rejected')], default='OPEN', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('resolution_notes', models.TextField(blank=True, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dispute_case', to='orders.order')),
                ('return_request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispute_case', to='returns.returnrequest')),
            ],
        ),
    ]
