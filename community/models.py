from django.db import models

class Review(models.Model):
   title = models.CharField(max_length=100)
   movie_title = models.CharField(max_length=30)
   rank = models.IntegerField()
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   hits = models.IntegerField(default=0)