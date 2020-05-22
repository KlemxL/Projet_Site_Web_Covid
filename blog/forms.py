
from django import forms
from django.db import models
from django.db.models import Model 

from .models import Commande
from .models import Produit
from django.forms import ModelForm


"""
class CommandesForm(forms.ModelForm):
    
    class Meta:
        model = Commande
        
        fields = ['demandeur','produitChoisis','QUANTITE']
        #['nom'] #,'description','prix','unite']


        #['demandeur','produitChoisis','QUANTITE']
"""
QUANTITE=(
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	)
PYM=(
	('CB','CB'),
	('Virement SEPA','Virement SEPA'),
	('Paypal','Paypal'),
	)
class CommandesForm(forms.Form):
    pommeDeTerre= forms.BooleanField(label='Pommes de Terre',required=False)
    qte1=forms.ChoiceField( label='Quantité', choices=QUANTITE, initial=1, required=False)
    papierToilettes= forms.BooleanField(required=False)
    qte2=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1 ,required=False)
    lait= forms.BooleanField(required=False)
    qte3=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    bananes= forms.BooleanField(required=False)
    qte4=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    courgettes= forms.BooleanField(required=False)
    qte5=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    pommes= forms.BooleanField(required=False)
    qte6=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    tomates= forms.BooleanField(required=False)
    qte7=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    fraises= forms.BooleanField(required=False)
    qte8=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    savon= forms.BooleanField(required=False)
    qte9=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    shampoing= forms.BooleanField(required=False)
    qte10=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)
    chocolat= forms.BooleanField(required=False)
    qte11=forms.ChoiceField( label='Quantité',  choices=QUANTITE, initial=1, required=False)

class Paiement(forms.Form):
	paiement=forms.ChoiceField(label='Mode de Paiement', choices=PYM)
        