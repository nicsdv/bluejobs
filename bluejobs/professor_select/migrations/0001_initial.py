# Generated by Django 4.1.7 on 2024-03-11 19:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.PositiveIntegerField()),
                ('venue', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_sections', to='professor_select.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_classes', to='landing_page.department')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_code', models.CharField(max_length=10)),
                ('day_schedule', models.CharField(max_length=20)),
                ('time_schedule', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_matter_expertise', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('workload_management', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('grading_leniency', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('approachability', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('friendliness', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('comment', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_reviews', to='professor_select.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_ratings', to='professor_select.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_reviews', to='landing_page.student')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_select.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor_select.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='landing_page.student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSectionStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_students', to='professor_select.coursesection')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_courses', to='landing_page.student')),
            ],
        ),
        migrations.AddField(
            model_name='coursesection',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_classes', to='professor_select.professor'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_schedule', to='professor_select.sectionschedule'),
        ),
        migrations.AddConstraint(
            model_name='professorrating',
            constraint=models.UniqueConstraint(fields=('student', 'professor', 'course'), name='student_rating'),
        ),
        migrations.AddConstraint(
            model_name='professorfavorite',
            constraint=models.UniqueConstraint(fields=('student', 'professor', 'course'), name='student_favorite'),
        ),
        migrations.AddConstraint(
            model_name='coursesection',
            constraint=models.UniqueConstraint(fields=('course', 'section'), name='course_section'),
        ),
    ]
