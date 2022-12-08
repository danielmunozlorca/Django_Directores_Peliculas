from django.db import models
import uuid

# Create your models here.

class Directores (models.Model):
    Nombre = models.CharField(max_length=50,help_text="ingresar nombre director")
    FechaNacimiento = models.DateField()

    def __str__ (self):
        return self.Nombre

class Películas (models.Model):
    Título = models.CharField(max_length=64,help_text="ingresar nombre película")
    AñoLanzamiento = models.IntegerField()

    def __str__ (self):
        return self.Título

class Buscador (models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,help_text="Id único") 
    Director = models.ForeignKey(Directores,null= False,blank=False,on_delete=models.CASCADE)
    Película = models.ForeignKey(Películas,null=False,blank=False,on_delete=models.CASCADE)

    def __str__ (self):
        return '%s, %s' %(self.Película,self.Director)    