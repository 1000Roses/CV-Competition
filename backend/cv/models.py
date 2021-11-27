from django.db import models
from user.models import CustomUser
from constrain.constrain import SIDE


class Content(models.Model):
    content = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.content

class Cv(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' +  self.name

class Section(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name="section", blank= True, null= True)
    column = models.CharField(max_length=5, choices=SIDE)

    def __str__(self):
        return self.name

class SubSection(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    content = models.ManyToManyField(Content, blank= True)
    section = models.ForeignKey(Section, on_delete= models.CASCADE, related_name= 'sub_section', blank= True, null= True)

    def __str__(self):
        return self.name
