from django import forms
from django.db import models
from .choices import *
import datetime

class ShowRouteForm(forms.Form):
    routes = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    stores = forms.MultipleChoiceField(required=False)
    drivers = forms.MultipleChoiceField(required=False)
    items = forms.MultipleChoiceField(required=False)
    distances = forms.MultipleChoiceField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super (ShowRouteForm, self).__init__(*args, **kwargs)
    #     self.fields['routes'].widget.attrs['class'] = "filtered"
        
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value, self.widget = min_value, max_value, forms.NumberInput(attrs={'step': "0.01"})
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value, 'widget' : self.widget}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class MinMaxDecimal(models.DecimalField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value, self.widget = min_value, max_value, forms.NumberInput(attrs={'step': "0.01"})
        super(MinMaxDecimal, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value, 'widget' : self.widget}
        defaults.update(kwargs)
        return super(MinMaxDecimal, self).formfield(**defaults)


class MyDateField(models.DateField):
    def __init__(self, *args, **kwargs):
        self.widget = forms.DateInput(attrs={'class': "datepicker"})
        super(MyDateField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget' : self.widget}
        defaults.update(kwargs)
        return super(MyDateField, self).formfield(**defaults)