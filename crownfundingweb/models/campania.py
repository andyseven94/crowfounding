from django.db import models
from crownfundingweb.models import Categoria
from django.contrib.auth.models import User
import datetime
    
class Campania(models.Model):
    categorias = models.ManyToManyField(Categoria, related_name = 'campanias') 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_campania = models.CharField(max_length=255, unique =True)
    slug = models.SlugField()
    descripcion_campania = models.TextField(blank = True) 
    imagen_campania = models.ImageField(upload_to='imagenes/', default='')
    video_campania = models.FileField(upload_to='videos_campania/', blank=True)
    monto_objetivo = models.DecimalField(max_digits=10, decimal_places=2, blank = False)
    fecha_inicio = models.DateField(null = False, default=datetime.date.today())
    fecha_fin= models.DateField(blank = False)
    activa = models.BooleanField( null = False)
    inserted_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self) -> str:
        return f'{self.nombre_campania} ({self.id})'
    
    class Meta:
        db_table = 'pr_campania'
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'
