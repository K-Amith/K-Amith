from django import forms


class Feedback_form(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":5,}))
