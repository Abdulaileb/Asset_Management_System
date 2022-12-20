# Generated by Django 4.1.3 on 2022-12-19 00:29

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Faculty', 'Faculty'), ('Department', 'Department'), ('Employee', 'Employee')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Academic', 'Academic'), ('Administration', 'Administration')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default='CYPA', max_length=50)),
                ('Name', models.CharField(max_length=100)),
                ('Business', models.CharField(choices=[('Manufacturer', 'Manufacturer'), ('wholesaler', 'Wholesaler'), ('retailers', 'Retailer'), ('service and maintenance providers', 'Service and maintenance providers'), ('independent vendors', 'Independent vendors')], default='Manufacturer', max_length=40)),
                ('Address', models.TextField(max_length=250)),
                ('City', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Website', models.URLField(blank=True, max_length=250, null=True)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Title', models.TextField()),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Departments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Model', models.TextField(max_length=200, null=True)),
                ('Serian_Num', models.CharField(blank=True, max_length=100, null=True)),
                ('Asset_State', models.CharField(choices=[('New', 'New'), ('Good', 'Good'), ('Used', 'Used'), ('Defective', 'Defective')], default='New', max_length=15)),
                ('LifeSpan', models.CharField(default='10Yrs', max_length=50, null=True)),
                ('Date_Acquired', models.DateField()),
                ('Warantee_Start_Date', models.DateField()),
                ('Date_Assigned', models.DateField()),
                ('Description', models.TextField()),
                ('Assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.assign')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.employee')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset_type')),
                ('Vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.vendor')),
            ],
        ),
    ]
