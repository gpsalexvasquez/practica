from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            widget = field.widget
            # No aplicar a checkbox/multiselect por defecto
            if not isinstance(widget, (forms.CheckboxInput, forms.RadioSelect)):
                widget.attrs.update({'class': 'form-control'})
            # Placeholder opcional con nombre del campo
            widget.attrs.setdefault('placeholder', field.label)
