from  django import forms


class TemplateForm(forms.Form):
    full_name = forms.CharField()
    given_date = forms.DateField(
          widget=forms.DateInput(attrs={
                "type": "date "
          })
    )
    reference_number = forms.CharField()
    start_date = forms.DateField(
          widget=forms.DateInput(attrs={
                "type": "date "
          })
    )
    end_date = forms.DateField(
          widget=forms.DateInput(attrs={
                "type": "date "
          })
    )
     