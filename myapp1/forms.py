from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        widgets = {
            'client': forms.RadioSelect(choices=[
                ('Client A', 'Client A'),
                ('Client B', 'Client B'),
                ('Client C', 'Client C'),
            ]),
        }
        labels = {
            'items_ordered': 'Quantity',
            'client': 'Client Name',
        }

    class InterestForm(forms.Form):
        interested = forms.TypedChoiceField(
            choices=((1, 'Yes'), (0, 'No')),
            coerce=lambda x: bool(int(x)),
            widget=forms.RadioSelect,
            label='Are you interested?'
        )
        quantity = forms.IntegerField(min_value=1, initial=1, label='Quantity')
        comments = forms.CharField(widget=forms.Textarea, required=False, label='Additional Comments')