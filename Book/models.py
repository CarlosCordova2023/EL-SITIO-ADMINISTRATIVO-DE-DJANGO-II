from django.db import models, migrations
from django.utils import timezone


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField()
   

    def __str__(self):
        return self.titulo


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
  
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        permissions = [
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        ]


    def __str__(self):
        return self.title
    

class Migration(migrations.Migration):

    dependencies = [
        ('Book', 'previous_migration_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='book',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]