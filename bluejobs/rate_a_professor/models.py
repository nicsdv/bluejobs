from django.db import models
from landing_page.models import Student
from professor_select.models import ProfessorRating

# Create your models here.
class Upvotes(models.Model):
    rating = models.ForeignKey (ProfessorRating, related_name = "upvotes", on_delete = models.CASCADE)
    student = models.ForeignKey (Student, on_delete = models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'rating'], name='student_upvote')
        ]