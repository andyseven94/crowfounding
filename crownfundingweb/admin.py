from django.contrib import admin
#importacion de modelos para visualizacion en modulo de administracion
from crownfundingweb.models import Categoria, Campania, Contribucion
 
admin.site.site_header = 'Administracion Crownfunding'

@admin.register (Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria' ,'slug','descripcion_categoria' ,
                    'imagen_categoria' ,'activa' ,'inserted_at' ,'updated_at' )

@admin.register (Campania)
class CampaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre_campania','slug', 'descripcion_campania',
                    'monto_objetivo', 'imagen_campania', 'video_campania',
                    'fecha_inicio','fecha_fin','activa','updated_at',
                    'inserted_at')
    
@admin.register (Contribucion)
class ContribucionAdmin(admin.ModelAdmin):
    list_display = ('monto_contribuido','fecha_contribucion', 'comentario_contribucion', 'inserted_at')

