from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.language
    

class Theme(models.Model):
    theme = models.CharField(max_length=10)

    def __str__(self):
        return self.theme


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name