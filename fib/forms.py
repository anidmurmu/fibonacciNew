from django import forms

class NumberForm(forms.Form):
    nth_term = forms.IntegerField()

    def clean(self):
        cleaned_data = super(NumberForm, self).clean()
        nth_term = cleaned_data.get('nth_term')
        if nth_term <= 0:
            raise forms.ValidationError('Enter positive number')
        if nth_term > 100000:
            raise forms.ValidationError('Number above 100000 is not allowed!')