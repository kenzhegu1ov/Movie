from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    preview = models.ImageField(upload_to='previews')
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)

    def director_name(self):
        return self.director.name


STAR_CHOICES = (
    (1, "* "),
    (2, 2 * "* "),
    (3, 3 * "* "),
    (4, 4 * "* "),
    (5, 5 * "* "),
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text
