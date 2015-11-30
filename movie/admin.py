from django.contrib import admin
from .models import SignUp,Movie , Producer , Director ,Theatre ,Shows , Hero , Heroine

# Register your models here.
admin.site.register(SignUp)
admin.site.register(Producer)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Shows)
admin.site.register(Hero)
admin.site.register(Heroine)