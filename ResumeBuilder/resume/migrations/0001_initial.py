# Generated by Django 2.1.5 on 2020-05-04 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=12)),
                ('Last_Name', models.CharField(max_length=12)),
                ('Linkedin_Link', models.CharField(max_length=50)),
                ('Street_Address', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=2)),
                ('Pin_Code', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=40)),
                ('College_Name', models.CharField(max_length=80)),
                ('Subject_Details', models.CharField(max_length=90)),
                ('Anticipated_Graduation_Date', models.CharField(max_length=15)),
                ('Degree', models.CharField(max_length=60)),
                ('GPA', models.FloatField(blank=True, null=True)),
                ('Technical_Skills1', models.CharField(blank=True, default='Programming', max_length=20)),
                ('Sub_Skills1', models.CharField(blank=True, max_length=150)),
                ('Technical_Skills2', models.CharField(default='Framework', max_length=20)),
                ('Sub_Skills2', models.CharField(blank=True, max_length=150)),
                ('Technical_Skills3', models.CharField(default='Databases', max_length=20)),
                ('Sub_Skills3', models.CharField(blank=True, max_length=150)),
                ('Technical_Skills4', models.CharField(default='Operating System', max_length=20)),
                ('Sub_Skills4', models.CharField(blank=True, max_length=150)),
                ('Technical_Skills5', models.CharField(default='Tools', max_length=20)),
                ('Sub_Skills5', models.CharField(blank=True, max_length=150)),
                ('Project1_Title', models.CharField(blank=True, max_length=100)),
                ('Project1_Description', models.TextField(blank=True, max_length=1000)),
                ('Project2_Title', models.CharField(blank=True, max_length=100)),
                ('Project2_Description', models.TextField(blank=True, max_length=1000)),
                ('Project3_Title', models.CharField(blank=True, max_length=100)),
                ('Project3_Description', models.TextField(blank=True, max_length=1000)),
                ('Work_Experience', models.CharField(blank=True, choices=[('WORK EXPERIENCE', 'Work Experience'), ('', 'Blank')], default='Blank', max_length=127)),
                ('Company1', models.CharField(blank=True, max_length=127)),
                ('Company1_Position', models.CharField(blank=True, max_length=40)),
                ('Company1_Start_Date', models.CharField(blank=True, max_length=15)),
                ('Company1_End_Date', models.CharField(blank=True, max_length=15)),
                ('Company1_Description', models.TextField(blank=True, max_length=2047)),
                ('Company2', models.CharField(blank=True, max_length=127)),
                ('Company2_Position', models.CharField(blank=True, max_length=40)),
                ('Company2_Start_Date', models.CharField(blank=True, max_length=15)),
                ('Company2_End_Date', models.CharField(blank=True, max_length=15)),
                ('Company2_Description', models.TextField(blank=True, max_length=2047)),
                ('Certifications', models.CharField(blank=True, choices=[('CERTIFICATIONS', 'Certification'), ('', 'Blank')], default='Blank', max_length=17)),
                ('Certification1', models.CharField(blank=True, max_length=50)),
                ('Certification2', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
