from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Photo(models.Model):
    photo = models.FileField()


class Header(models.Model):
    logo = models.FileField()
    footer_text = models.CharField(max_length=255)
    photo = models.ManyToManyField(Photo)
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=255)
    is_fail = models.BooleanField()
    video_fail = models.FileField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)


class Position(models.Model):
    name = models.CharField(max_length=255)


class Players(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    game = models.IntegerField()
    time_played = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()


class Background(models.Model):
    background = models.ImageField()


class Shop(models.Model):
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    volume = models.IntegerField()
    places = models.IntegerField()
    sector = models.IntegerField()
    map = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Partners(models.Model):
    img = models.FileField()


class Tournament(models.Model):
    data = models.DateTimeField()
    match = models.IntegerField()


class News(models.Model):
    news = models.TextField()
    photo = models.ImageField()
    is_file = models.BooleanField()
    video_file = models.FileField()
    video_url = models.CharField(max_length=255)
    tournament = models.ManyToManyField(Tournament)


class Team(models.Model):
    title = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    players = models.ManyToManyField(Players)


class Leadership(models.Model):
    photo = models.FileField()


class Level(models.Model):
    name = models.CharField(max_length=255)


class Leader(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Coach(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Club(models.Model):
    club = RichTextUploadingField()


class Academy(models.Model):
    academy = RichTextUploadingField()


class Arena(models.Model):
    arena = RichTextUploadingField()



