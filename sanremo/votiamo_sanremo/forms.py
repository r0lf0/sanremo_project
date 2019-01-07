from django.forms import ModelForm
from .models import Voto

class VotaForm(ModelForm):
    class Meta:
        model = Voto
        fields = ['voto_outfit','voto_interpretazione','voto_canzone']
