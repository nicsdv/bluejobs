from django import forms
from professor_select.models import ProfessorRating
from rate_a_professor.models import Upvotes

class ProfessorRatingForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        exclude = ['professor', 'student', 'rating_date_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject_matter_expertise'].widget.attrs['class'] = 'form-score'
        self.fields['workload_management'].widget.attrs['class'] = 'form-score'
        self.fields['grading_leniency'].widget.attrs['class'] = 'form-score'
        self.fields['approachability'].widget.attrs['class'] = 'form-score'
        self.fields['friendliness'].widget.attrs['class'] = 'form-score'
        self.fields['course'].widget.attrs['class'] = 'form-course'

class ProfessorUpvoteForm(forms.ModelForm):
    class Meta:
        model = Upvotes
        fields = ['rating']