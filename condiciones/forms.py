from django.forms        import ModelForm
from general.forms       import make_custom_datefield
from condiciones.models import CondicionUnitaria

class CondicionUnitariaForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = CondicionUnitaria

