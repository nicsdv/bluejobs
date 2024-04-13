from django.db import models
from landing_page.models import Student
from professor_select.models import ProfessorRating

# Create your models here.
class Upvotes(models.Model):
    rating = models.ForeignKey (ProfessorRating, related_name = "upvotes", on_delete = models.CASCADE)
    student = models.ForeignKey (Student, related_name = "student_upvotes", on_delete = models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'rating'], name='student_upvote')
        ]
    
def upvotes_by_professor (student, professor):
    query = Upvotes.objects.filter(student = student)
    arg = []
    for upvote in query:
        if upvote.rating.professor == professor:
            arg.append(upvote.rating)
    
    return arg