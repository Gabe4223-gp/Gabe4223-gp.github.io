from django.db import models


# Create your models here.
class BusinessIdeas(models.Model):
    prompt_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.prompt_text
