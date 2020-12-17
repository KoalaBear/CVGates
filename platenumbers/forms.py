from django import forms

from platenumbers.models import PlateNumber


class PlateNumberForm(forms.ModelForm):
    class Meta:
        model = PlateNumber
        fields = "__all__"
