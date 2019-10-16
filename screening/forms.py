from django import forms
from screening.models import ScreeningForm


class ScreeningCrf(forms.ModelForm):
    class Meta:
        model = ScreeningForm
        fields = ['verbal_consent', 'hospital_id', 'initials', 'gender', 'age', 'ethnicity', 'hiv',
                  'arv', 'treatment', 'live_in_catchment', 'remain_in_catchment', 'pregnant', 'informed_consent']
