# Generated by Django 4.1.7 on 2023-03-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EarningReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField()),
                ('eps', models.DecimalField(decimal_places=2, max_digits=6)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=6)),
                ('eps_forecast', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('content', models.TextField(null=True)),
                ('source', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('ticker', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sector', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='trade',
            name='strategy',
        ),
        migrations.DeleteModel(
            name='Strategy',
        ),
        migrations.DeleteModel(
            name='Trade',
        ),
        migrations.AddField(
            model_name='earningreport',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.stock'),
        ),
    ]