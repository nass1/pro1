from django import forms

class APIform(forms.Form):
    Name = forms.CharField()
    Price = forms.CharField()
    Comment = forms.CharField()


class SearchForm(forms.Form):
    Search = forms.CharField()


class ImportForm(forms.Form):
    Name = forms.CharField()