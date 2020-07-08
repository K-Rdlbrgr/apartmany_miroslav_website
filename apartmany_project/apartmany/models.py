from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=2083)
    
    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.title, self.name)
