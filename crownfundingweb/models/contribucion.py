from django.db import models
from django.contrib.auth.models import User

from crownfundingweb.models import Campania
    
class Contribucion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    campania_id =models.ForeignKey(Campania, on_delete = models.CASCADE)
    monto_contribuido = models.DecimalField(max_digits=10, decimal_places=2, null = False)
    fecha_contribucion = models.DateField()
    comentario_contribucion =  models.TextField()
    inserted_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return f'{self.id}: {self.monto_contribuido} para {self.proyecto}'
    
class Meta:
        db_table = 'pr_contribucion'
        verbose_name = 'Contribución'
        verbose_name_plural = 'Contribuciones'