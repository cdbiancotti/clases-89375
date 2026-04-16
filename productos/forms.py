from django import forms
from productos.models import JabonLiquido

# v1
class FormularioCreacionJabonLiquido(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
# v2
class FormularioCreacionJabonLiquidoCBV(forms.ModelForm):
    # marca = forms.CharField(max_length=30)
    # descripcion = forms.CharField(widget=forms.Textarea)
    # fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = JabonLiquido
        # fields = ['marca', 'descripcion']
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }