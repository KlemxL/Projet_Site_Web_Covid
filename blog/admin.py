from django.contrib import admin

from .models import Post
from .models import Produit
from .models import Commande


admin.site.register(Post)

admin.site.register(Produit) 

admin.site.register(Commande) 