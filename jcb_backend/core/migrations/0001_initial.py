# Generated by Django 5.2.1 on 2025-05-27 10:07

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_number', models.CharField(max_length=50, unique=True)),
                ('model_name', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
                ('papers', models.FileField(blank=True, null=True, upload_to='machine_papers/')),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.FileField(blank=True, null=True, upload_to='operator_photos/')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='operator_ids/')),
                ('license', models.FileField(blank=True, null=True, upload_to='operator_licenses/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_type', models.CharField(max_length=100)),
                ('amount_spent', models.FloatField()),
                ('part_repaired', models.TextField()),
                ('maintenance_date', models.DateField()),
                ('bill_file', models.FileField(upload_to='maintenance_bills/')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.machine')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operator')),
            ],
        ),
        migrations.CreateModel(
            name='WorkEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(choices=[('Plant Work', 'Plant Work'), ('Farming Work', 'Farming Work'), ('Digging/Loading Soil', 'Digging/Loading Soil'), ('Digging/Loading Sand', 'Digging/Loading Sand'), ('Local Work', 'Local Work'), ('Digging a Drain', 'Digging a Drain')], max_length=50)),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_working_hours', models.FloatField()),
                ('diesel_used', models.FloatField()),
                ('rate_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('commission_based', models.BooleanField(default=False)),
                ('commission_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.machine')),
            ],
        ),
        migrations.CreateModel(
            name='WorkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(choices=[('plant', 'Plant Work'), ('farming', 'Farming Work'), ('soil', 'Digging/Loading Soil'), ('sand', 'Digging/Loading Sand'), ('local', 'Local Work'), ('drain', 'Digging a Drain')], max_length=20)),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_hours', models.FloatField()),
                ('diesel_used', models.FloatField()),
                ('rate_per_hour', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('is_commission', models.BooleanField(default=False)),
                ('commission_amount', models.FloatField(blank=True, null=True)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=20)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.machine')),
            ],
        ),
    ]
