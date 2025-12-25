from django.contrib import admin
from .models import Movie, Actor, Review

class MovieActorInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'is_favorite')
    list_filter = ('year', 'is_favorite')
    inlines = [MovieActorInline]
    exclude = ('actors',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'movie', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'movie')