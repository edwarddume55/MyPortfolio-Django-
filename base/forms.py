from django.forms import ModelForm
from .models import Project,Skill

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','thumbnail','body']

    def __init__(self, *args, **kwargs):  # Correct the spacing in the method definition
        super(ProjectForm, self).__init__(*args, **kwargs)  # Fix the super() call

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})
