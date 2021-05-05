# Generated by Django 3.2 on 2021-04-23 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_bgp', '0009_netbox_bgp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asn',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='asngroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bgppeergroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bgpsession',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='bgpsession',
            name='peer_group',
        ),
        migrations.AddField(
            model_name='bgpsession',
            name='peer_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='netbox_bgp.bgppeergroup'),
        ),
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]