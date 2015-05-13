from django.db import models
from django.contrib.auth.models import User

class utilisateurs(models.Model):
    user=models.OneToOneField(User,unique=True)
	numetudiant = models.CharField(max_length=7)
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	annee = models.CharField(max_length=1)
	departement = models.CharField(max_length=30)
	statut = models.CharField(max_length=30)
	style = models.CharField(max_length=100)
	certificat = models.CharField(max_length=300)
	photo = models.CharField(max_length=300)
	
        
class choregraphies(models.Model):
	user=models.OneToOneField(User,unique=True)
	dance = models.CharField(max_length=100)
	
	
class dances(models.Model):
	choregraphe=models.OneToOneField(User,unique=True)
	dance = models.CharField(max_length=100)
	
	
class privileges(models.Model):
	statut = models.CharField(max_length=30)
	pageaccede = models.CharField(max_length=300)
