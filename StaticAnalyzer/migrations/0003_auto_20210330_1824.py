# Generated by Django 3.1.7 on 2021-03-30 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0001_initial'),
        ('StaticAnalyzer', '0002_auto_20210330_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticanalyzerandroid',
            name='STATIC_REPORT',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Report.androidstaticreport'),
        ),
    ]
