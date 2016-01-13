from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,blank=False)
    name = models.CharField(max_length=100,blank=True)
    details = models.TextField()
    implementation =models.CharField(max_length=200,blank=True)
    features = models.TextField()
    tools = models.TextField()
    slug = models.SlugField()
    image1 = models.ImageField(upload_to=title)
    image2 = models.ImageField(upload_to=title)
    image3 = models.ImageField(upload_to=slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title