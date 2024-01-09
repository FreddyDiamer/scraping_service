from django import forms
from .models import City, Language


class FilterForm(forms.Form):
  city = forms.ModelChoiceField(
    queryset=City.objects.all(), label='Cities', to_field_name='slug', 
    required=False, widget=forms.Select(attrs={ 'class': 'form-control' }), initial='London')
  lang = forms.ModelChoiceField(
    queryset=Language.objects.all(), label='Languages', to_field_name='slug', 
    required=False, widget=forms.Select(attrs={ 'class': 'form-control' }), empty_label='Select lang')