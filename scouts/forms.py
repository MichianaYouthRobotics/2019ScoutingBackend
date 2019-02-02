from django import forms
from scouts.models import Scout


class ScoutForm(forms.ModelForm):
    class Meta:
        model = Scout
        fields = ['person', 'robot_number', 'match_number', 'hatches_secured']
