from django.contrib import admin
from .models import Habilidades, Rol, Empleado

# Para edad importar:
from datetime import date

# Para exportar CSV:
import csv
from django.http import HttpResponse

# Para exportar PDF:
from reportlab.pdfgen import canvas

# Para importar ckeditor
from django_ckeditor_5.widgets import CKEditor5Widget

class RolAdmin (admin.ModelAdmin):
    list_filter = (
        'habilidadesRol',
    )

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'nombreEmp',
        'apellidoEmp',
        'rolEmp',
        'departamentoEmp',
        'edad'
    )
    
    search_fields = (
        'apellidoEmp',
        'nombreEmp',
    )
    
    list_filter = (
        'rolEmp',
        'departamentoEmp',
    )
    
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'observaciones': CKEditor5Widget(config_name='default'),
        }
    
    def edad(self,obj):
        today = date.today()
        age = today.year - obj.fechaNac.year - ((today.month, today.day) < (obj.fechaNac.month, obj.fechaNac.day))
        return age
    
    def exportar_empleados_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

        writer = csv.writer(response)
        writer.writerow(['Nombre', 'Apellido', 'Rol', 'Departamento', 'Fecha de Nacimiento'])

        for empleado in queryset:
            writer.writerow([
                empleado.nombreEmp,
                empleado.apellidoEmp,
                empleado.rolEmp,
                empleado.departamentoEmp,
                empleado.fechaNac
            ])

        return response
    
    exportar_empleados_csv.short_description = "Exportar empleados seleccionados a CSV"
    
    def exportar_empleados_pdf(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'

        p = canvas.Canvas(response)
        y = 800
        p.setFont("Helvetica", 12)
        p.drawString(100, y, "Lista de Empleados")

        y -= 30
        for empleado in queryset:
            p.drawString(100, y, f'{empleado.nombreEmp} {empleado.apellidoEmp} - {empleado.rolEmp}')
            y -= 20
            if y < 50:
                p.showPage()
                y = 800

        p.showPage()
        p.save()
        return response

    exportar_empleados_pdf.short_description = "Exportar empleados seleccionados a PDF"
    
    actions = [exportar_empleados_csv,exportar_empleados_pdf]



admin.site.register(Habilidades)
admin.site.register(Rol,RolAdmin)
admin.site.register(Empleado,EmpleadoAdmin)