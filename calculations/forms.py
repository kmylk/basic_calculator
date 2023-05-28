from django import forms

OPERATION_CHOICES = (
    ("sum", "+"),
    ("sub", "-"),
    ("mul", "*"),
    ("div", "/"),

)


class CalculatorForm(forms.Form):
    first_value = forms.IntegerField(label="")
    operation = forms.ChoiceField(label="", choices=OPERATION_CHOICES)
    second_value = forms.IntegerField(label="")
