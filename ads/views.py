from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Movie, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'rating', 'text']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ваш отзыв (необязательно)'}),
        }

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ads/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False) 
            review.movie = movie             
            review.save()                    
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = ReviewForm()

    return render(request, 'ads/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })

def top_movies(request):
    favorites = Movie.objects.filter(is_favorite=True).order_by('-year')[:5]
    return render(request, 'ads/top_movies.html', {'movies': favorites})