from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

class Product(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True) 
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

def set_slug(sender, instance, *args, **kwargs):
    if instance.titulo and not instance.slug:
        slug = slugify(instance.titulo)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.titulo, str(uuid.uuid4())[:8] )
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Product)