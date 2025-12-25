from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя актёра")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска"
    )
    poster = models.ImageField(upload_to='ads/', blank=True, null=True, verbose_name="Постер")
    description = models.TextField(blank=True, verbose_name="Описание")
    director = models.CharField(max_length=100, verbose_name="Режиссёр")
    is_favorite = models.BooleanField(default=False, verbose_name="В топ-5")
    actors = models.ManyToManyField(Actor, blank=True, verbose_name="Актёры")

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-year']

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE, verbose_name="Фильм")
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        verbose_name="Оценка (1–5)"
    )
    text = models.TextField(verbose_name="Текст отзыва", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.author_name}: {self.rating}★ — {self.movie.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']