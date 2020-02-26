# Generated by Django 2.2.7 on 2019-11-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='end_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(verbose_name='Height (in)'),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='start_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(verbose_name='Weight (lb)'),
        ),
    ]
