from django.forms import ModelForm, DateInput
from .models import Clients

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }