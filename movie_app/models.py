from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='movies_count')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()

    def __str__(self):
        return self.title

    @property
    def rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        average = 0
        for i in reviews:
            average += i.stars
        return average / reviews.count()


STAR_CHOICES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *')
)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews', )
    stars = models.IntegerField(default=1, choices=STAR_CHOICES)

    def __str__(self):
        return self.text
# Create your models here.
