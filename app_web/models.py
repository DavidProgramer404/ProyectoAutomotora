from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

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
    

class UsuarioManager(BaseUserManager):
    def create_user(self, correo,nombre,apellido,rut,direccion,telefono,tipo_usuario,password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        user = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            direccion=direccion,
            telefono=telefono,
            tipo_usuario=tipo_usuario,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, correo, nombre, apellido, rut, direccion, telefono, tipo_usuario, password=None):
        user = self.create_user(
            correo, nombre, apellido, rut, direccion, telefono, tipo_usuario, password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.EmailField( max_length=200,unique=True)
    nombre = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=200, null=False)
    rut = models.CharField(max_length=12, unique=True,null=False)
    direccion = models.CharField(max_length=200, null=False)
    telefono = models.CharField(max_length=20, null=False)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='id_tipo_usuario')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'rut', 'direccion', 'telefono', 'tipo_usuario']
    # META
    class Meta:
        managed = False
        db_table = 'usuarios'
    
    def __str__(self):
        return self.nombre


class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    nro_asiento = models.IntegerField(null=False)
    anio = models.IntegerField(null=False)
    marca = models.CharField(max_length=200,null=False)
    nro_venta =models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    tipo_auto = models.ForeignKey(TipoAuto, on_delete=models.CASCADE, db_column='id_tipo_auto')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,db_column='id_comuna')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='id_usuario')
    # META
    class Meta:
        managed = False
        db_table = 'autos'
    
    def __str__(self):
        return self.nombre
    
    