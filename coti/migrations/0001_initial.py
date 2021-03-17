# Generated by Django 3.1.7 on 2021-03-17 22:05

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telephone', models.CharField(max_length=10)),
                ('username', models.CharField(error_messages={'unique': 'El correo electrónico seleccionado ya está siendo usando en el sistema.'}, help_text='Debe agregar un correo electronico válido', max_length=150, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Correo electrónico')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('units', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('units_by_sqr_meters', models.BooleanField(default=False)),
                ('price_in_usd', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('high', models.DecimalField(decimal_places=6, max_digits=12)),
                ('width', models.DecimalField(decimal_places=6, max_digits=12)),
                ('thickness', models.DecimalField(decimal_places=6, max_digits=12)),
                ('area', models.DecimalField(decimal_places=6, max_digits=12)),
                ('weight', models.DecimalField(decimal_places=6, max_digits=12)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='TColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='TPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('commission', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='TPresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coti.person')),
                ('catchment', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('out_number', models.CharField(max_length=255)),
                ('int_number', models.CharField(blank=True, max_length=255, null=True)),
                ('cp', models.IntegerField()),
                ('colony', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('coti.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('piece_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coti.piece')),
            ],
            bases=('coti.piece',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('piece_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coti.piece')),
                ('price_in_usd', models.BooleanField(default=True)),
            ],
            bases=('coti.piece',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coti.person')),
                ('commission', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('coti.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_area', models.DecimalField(decimal_places=6, max_digits=12)),
                ('installation_area_wasted', models.DecimalField(decimal_places=6, max_digits=12)),
                ('pieces', models.DecimalField(decimal_places=6, max_digits=12)),
                ('pieces_closeup', models.IntegerField()),
                ('area_check', models.DecimalField(decimal_places=6, max_digits=12)),
                ('profile_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('profile_price_in_usd', models.BooleanField(default=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.tcolor')),
                ('installation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.tinstallation')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoryMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units_by_sqr_meters', models.IntegerField()),
                ('total_units', models.IntegerField()),
                ('total_units_presentation', models.IntegerField()),
                ('accessory_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('accessory_price_in_usd', models.BooleanField(default=False)),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.accessory')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.material')),
            ],
        ),
        migrations.AddField(
            model_name='accessory',
            name='presentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.tpresentation'),
        ),
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('private_comments', models.TextField(blank=True, null=True)),
                ('delivery_time', models.DateField()),
                ('exchange_rate', models.DecimalField(decimal_places=6, max_digits=12)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.material')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.tpayment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.client')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.seller')),
            ],
        ),
        migrations.CreateModel(
            name='FrameMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineal_meters', models.DecimalField(decimal_places=6, max_digits=12)),
                ('units', models.DecimalField(decimal_places=6, max_digits=12)),
                ('units_closeup', models.IntegerField()),
                ('frame_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.material')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.frame')),
            ],
        ),
        migrations.AddField(
            model_name='frame',
            name='frame_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.profile'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coti.profile'),
        ),
    ]
