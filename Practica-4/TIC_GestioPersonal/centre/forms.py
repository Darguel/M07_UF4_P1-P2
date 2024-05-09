from django.forms import ModelForm
from .models import Usuari

class UsuariForm(ModelForm):
    class Meta:
        model = Usuari
        fields = '__all__'