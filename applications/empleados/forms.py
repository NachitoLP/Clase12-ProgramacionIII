from django import forms
from .models import Empleado
from ..departamentos.models import Departamento

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombreEmp', 'apellidoEmp', 'rolEmp', 'departamentoEmp', 'fechaNac', 'observaciones']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rolEmp'].label = "Rol del Empleado"
        self.fields['departamentoEmp'].label = "Departamento"
        self.fields['departamentoEmp'].queryset = Departamento.objects.filter(isActivo=True)
        

""" 
El método __init__ personalizado sirve para modificar el formulario en tiempo de ejecución, después de que Django ya hizo la construcción inicial.
Siempre que lo sobrescriban, tienen que llamar primero a super().__init__() para que el formulario se inicialice bien. 
"""