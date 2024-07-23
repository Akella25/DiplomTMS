from django import forms

choicess = [(None, ''), (True, 'c'), (False, 'без')]


class HotelSearchForm(forms.Form):
    citi = forms.CharField(required=False)
    star = forms.IntegerField(max_value=5, min_value=1, required=False)
    pool = forms.ChoiceField(required=False, choices=choicess, )
