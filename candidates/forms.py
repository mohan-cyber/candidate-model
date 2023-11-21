from django import forms
from .models import Candidatedirectory


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidatedirectory
        exclude = [
            "created_date",
            "created_by",
            "modified_date",
            "modified_by",
            "status",
        ]
