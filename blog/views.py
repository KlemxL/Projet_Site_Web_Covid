from django.shortcuts import render
#from .models import Post

from django.shortcuts import redirect
from django.contrib import messages


from .forms import CommandesForm, Paiement
from .models import Commande
from .models import Produit
from django.db.models import Max
from django.db.models import Sum
import datetime
#from .models import Produit
#from .models import Commandes
#from django.contrib.auth.form

def home(request):
    
    return render(request, 'blog/home.html')

def collectivite(request):
    commandes=Commande.objects.all()
    
    nbcommande=Commande.objects.count()
    somme=Commande.objects.values('produitChoisis__nom').annotate(Sum('quantite'))
    #somme2=Commande.objects.values('produitChoisis_id') \
    #.annotate(Produit_unite=Sum('quantite')) \
    #.order_by('-Produit_unite')

    return render(request, 'blog/collectivite.html',{'somme': somme,'commandes': commandes,'nbcommande': nbcommande})

def demandes(request):
    
    if request.method == 'POST':
        form = CommandesForm(request.POST)
        form_p=Paiement(request.POST)
        if form.is_valid() and form_p.is_valid():
            pommeDeTerre= form.cleaned_data['pommeDeTerre']
            qte1=form.cleaned_data['qte1']
            papierToilettes= form.cleaned_data['papierToilettes']
            qte2=form.cleaned_data['qte2']
            lait= form.cleaned_data['lait']
            qte3=form.cleaned_data['qte3']
            bananes= form.cleaned_data['bananes']
            qte4=form.cleaned_data['qte4']
            courgettes= form.cleaned_data['courgettes']
            qte5=form.cleaned_data['qte5']
            pommes= form.cleaned_data['pommes']
            qte6=form.cleaned_data['qte6']
            tomates= form.cleaned_data['tomates']
            qte7=form.cleaned_data['qte7']
            fraises= form.cleaned_data['fraises']
            qte8=form.cleaned_data['qte8']
            savon= form.cleaned_data['savon']
            qte9=form.cleaned_data['qte9']
            shampoing= form.cleaned_data['shampoing']
            qte10=form.cleaned_data['qte10']
            chocolat= form.cleaned_data['chocolat']
            qte11=form.cleaned_data['qte11']
            quantites=[qte1,qte2,qte3,qte4,qte5,qte6,qte7,qte8,qte9,qte10,qte11]
            produits=[pommeDeTerre,papierToilettes,lait,bananes,courgettes,pommes,tomates,fraises,savon,shampoing,chocolat]
            prods=Produit.objects.all()
            for idx in range(len(produits)):
                if produits[idx]==True:
                    commande=Commande(demandeur=request.user,produitChoisis=prods[idx],quantite=quantites[idx])
                    commande.save()
            
            messages.success(request, f'Commande effectuée!')
            return redirect('blog-home')
    else:
        form = CommandesForm()
        form_p=Paiement()
        
    return render(request, 'blog/demandes.html', locals()) #, locals()) #



"""
def demandes(request):
    
    if request.method == 'POST':
        form = CommandesForm(request.POST)
        
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Commande effectuée!')
            return redirect('blog-home')
    else:
        form = CommandesForm()
        
        
    return render(request, 'blog/demandes.html', {'form': form})

#def demandeurs(request):
#    return render(request, 'blog/demandeurs.html')

"""




