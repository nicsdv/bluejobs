from django import forms
from professor_select.models import ProfessorRating

class ProfessorRatingForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        widgets = {
            'subject_matter_expertise': forms.NumberInput(attrs={'min':'0', 'max':'10'}),
            'workload_management': forms.NumberInput(attrs={'min':'0', 'max':'10'}),
            'grading_leniency': forms.NumberInput(attrs={'min':'0', 'max':'10'}),
            'approachability': forms.NumberInput(attrs={'min':'0', 'max':'10'}),
            'friendliness': forms.NumberInput(attrs={'min':'0', 'max':'10'})
        }
        exclude = ['professor', 'student']