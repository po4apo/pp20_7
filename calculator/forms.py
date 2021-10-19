from django import forms

operators = [('+', '+'),
             ('-', '-'),
             ('*', '*'),
             ('/', '/')]


class CalculatorForm(forms.Form):
    num1 = forms.FloatField(required=0,
                            label='')
    operator = forms.ChoiceField(choices=operators,
                                 required=False,
                                 label='')
    num2 = forms.FloatField(required=0,
                            label='')


class MemoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        got_choices = kwargs.pop('choices', None)
        super().__init__(*args, **kwargs)
        got_choices.reverse()
        self.fields['list'].choices = got_choices

    choices = [({'num1': 2.0, 'operator': '+', 'num2': 1.0, 'answer': 3.0}, 3.0)]

    list = forms.ChoiceField(required=False,
                              label='Память',
                              widget=forms.Select(attrs={'size': '4', 'class': 'row'}),
                              choices=choices,
                              )
