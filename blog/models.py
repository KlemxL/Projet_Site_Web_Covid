from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Post(models.Model): #Commandes de produits
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Produit(models.Model): #Produits en stock
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(decimal_places=2, max_digits=1000)
    unite = models.CharField(max_length=10)

    def __str__(self):
        return self.nom
    #,"  --  ", self.description, "  --  PRIX : ", self.prix, "/" , self.unite,



class Commande(models.Model): #Commandes de produits
    date= models.DateField(default=datetime.date.today())
    demandeur = models.ForeignKey(User, on_delete=models.CASCADE)
    produitChoisis = models.ForeignKey(Produit, on_delete=models.CASCADE) #, limit_choices_to=None)   
    quantite = models.DecimalField(decimal_places=1, max_digits=100)
    
    def __str__(self):
        return "Date : " + str(self.date) + "    Demandeur :  "+str(self.demandeur.username)





