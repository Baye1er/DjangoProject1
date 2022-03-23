from django.db import models


# Create your models here.
class Category(models.Model):
    contrat_longue_duree = 'CDI'
    contrat_courte_duree = 'CDD'
    stage = 'Stage'
    formation = 'Formation'

    choix_categorie = [
        (contrat_longue_duree, 'CDI'),
        (contrat_courte_duree, 'CDD'),
        (stage, 'Stage'),
        (formation, 'Formation')
    ]

    name = models.CharField(max_length=20, help_text='Type', choices=choix_categorie,
                            default=contrat_courte_duree, )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class Formulaire(models.Model):
    objet = models.CharField(max_length=200, help_text='Titre du poste')
    email = models.EmailField()
    nom_complet = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    cv = models.FileField(upload_to='uploads/', blank=True, null=True, help_text='Optionel')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email