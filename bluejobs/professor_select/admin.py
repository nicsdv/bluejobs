from django.contrib import admin
from professor_select.models import ( Professor, SectionSchedule, Course, CourseSection, 
CourseStudent, ProfessorRating, ProfessorFavorite)

'''
The following code initializes the admin panel for the models needed in the professor select app.  
This will help keep track of the existing instances of the entities and modify when necessary.

Code written by: Nics
'''

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    search_fields = ('professor_name', 'email',)
    list_display = ('professor_name', 'email',)
    list_filter = ('professor_name', 'email',)

class SectionScheduleAdmin(admin.ModelAdmin):
    model = SectionSchedule
    search_fields = ('section_code', 'day_schedule', 'time_schedule',)
    list_display = ('section_code', 'day_schedule', 'time_schedule',)
    list_filter = ('section_code', 'day_schedule', 'time_schedule',)

class CourseAdmin (admin.ModelAdmin):
    model = Course
    search_fields = ('course_code', 'course_title',  'department', )
    list_display = ('course_code', 'course_title',  'department', )
    list_filter = ('course_code', 'course_title',  'department', )

class CourseSectionAdmin (admin.ModelAdmin):
    model = CourseSection
    search_fields = ('course', 'section', 'professor', 'slots', 'venue',)
    list_display = ('course', 'section', 'professor', 'slots', 'venue',)
    list_filter = ('course', 'section', 'professor', 'slots', 'venue',)

class CourseStudentAdmin (admin.ModelAdmin):
    model = CourseStudent
    search_fields = ('course', 'student',)
    list_display = ('course', 'student',)
    list_filter =('course', 'student',)

class ProfessorRatingAdmin (admin.ModelAdmin):
    model = ProfessorRating
    search_fields = ('student','professor', 'course',)
    list_display = ('student','professor', 'course',)
    list_filter = ('student','professor', 'course',)

class ProfessorFavoriteAdmin (admin.ModelAdmin):
    model = ProfessorFavorite
    search_fields = ('student','professor', 'course',)
    list_display = ('student','professor', 'course',)
    list_filter = ('student','professor', 'course',)


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(SectionSchedule, SectionScheduleAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSection, CourseSectionAdmin)
admin.site.register(CourseStudent, CourseStudentAdmin)
admin.site.register(ProfessorRating,ProfessorRatingAdmin)
admin.site.register(ProfessorFavorite,ProfessorFavoriteAdmin)




