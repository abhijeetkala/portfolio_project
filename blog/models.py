from django.db import models

# Create  a blog model here.
class Blog(models.Model):
    #title
    title = models.CharField(max_length=200)
    #publication date
    pub_date = models.DateTimeField()
    #body
    body = models.TextField()
    #Images
    image = models.ImageField(upload_to='pictures/')
