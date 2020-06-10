# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-06-10 11:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('barcode', models.CharField(max_length=20, unique=True)),
                ('book_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=100)),
                ('no_of_books', models.IntegerField()),
                ('book_detail', models.TextField(default='text')),
                ('department', models.CharField(choices=[('COM', 'Computer'), ('ELX', 'Electronics'), ('CIV', 'Civil'), ('BBS', 'Business'), ('MSC', 'Miscellaneous')], max_length=3)),
                ('publisher', models.CharField(max_length=100)),
                ('rack_no', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BORROWER',
            fields=[
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_id', models.CharField(max_length=20)),
                ('book_id', models.CharField(max_length=20)),
                ('issue_date', models.DateField(default=datetime.date.today)),
                ('issue_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('librarian_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_id', models.CharField(max_length=20)),
                ('return_date', models.DateField(default=datetime.date.today)),
                ('borrower_id', models.CharField(max_length=20)),
                ('borrower_name', models.CharField(max_length=100)),
                ('book_id', models.CharField(max_length=20)),
                ('book_name', models.CharField(max_length=200)),
                ('isbn_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=1)),
                ('depart', models.CharField(max_length=3)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('borrower_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='libman.BORROWER')),
                ('emp_id', models.CharField(max_length=20, unique=True)),
                ('timer', models.CharField(choices=[('FT', 'Full Timer'), ('PT', 'Part Timer')], max_length=2)),
            ],
            bases=('libman.borrower',),
        ),
        migrations.CreateModel(
            name='Sborrower',
            fields=[
                ('borrower_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='libman.BORROWER')),
                ('borrower_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('batch', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')], max_length=4)),
                ('depart', models.CharField(choices=[('BEC', 'B. Computer Engineering'), ('BIT', 'B. Information Technology'), ('BCA', 'B. Computer Application'), ('ELX', 'B. Electronics Engineering'), ('CIV', 'B. Civil Engineering'), ('BBS', 'B. Business Studies'), ('MCA', 'M. Computer Application'), ('PGD', 'PG. Computer Applications'), ('MCJ', 'M. Mass Communication and Journalism')], max_length=3)),
                ('semester', models.CharField(max_length=1)),
            ],
            bases=('libman.borrower',),
        ),
    ]