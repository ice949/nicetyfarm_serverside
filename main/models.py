from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField(default="N/A", max_length=1000)
    description=models.TextField(default='N/A', blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated=models.DateTimeField(auto_now=True, blank=True, null=True)

    def str(self):
        return f"{self.name}"