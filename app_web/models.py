from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50)
    # META
    class Meta:
        managed = False
        db_table = 'tipo_usuarios'
    def __str__(self):
        return self.tipo_usuario
    

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=200, null=False)

    # META
    class Meta:
        managed = False
        db_table ='regiones'
    
    def __str__(self):
        return self.region


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=200, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,db_column='id_region')

    # META
    class Meta:
        managed = False
        db_table = 'comunas'
    
    def __str__(self):
        return self.comuna
    
class TipoAuto(models.Model):
    id_tipo_auto = models.AutoField(primary_key=True)
    tipo_auto = models.CharField(max_length=200, null=False)
    # META
    class Meta:
        managed = False
        db_table = 'tipo_autos'
    
    def __str__(self):
        return self.tipo_auto