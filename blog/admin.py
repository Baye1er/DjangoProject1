from django.contrib import admin
from blog.models import Post, Category, Formulaire

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class FormulaireAdmin(admin.ModelAdmin):
    list_display = ('objet', 'email', 'nom_complet', 'telephone', 'adresse', 'cv', 'date')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Formulaire, FormulaireAdmin)
