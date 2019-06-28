from django.db import models

# Create your models here.

class Blog(models.Model):
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField()

    def approve(self):
        self.approved_comment = True
        self.save()

    