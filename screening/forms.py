import re
from django import forms
from screening.models import Screening


class ScreeningCrf(forms.ModelForm):
    def clean(self):
        clean_data = self.changed_data
        if not re.match("[A-Z]{1,3}", clean_data.get("initials")):
            raise forms.ValidationError({"initials": "Must be all Caps. "})
        return self.changed_data

    class Meta:
        model = Screening
        fields = "__all__"
