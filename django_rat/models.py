from django.db import models


# Create your models here.
class Resume(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=25, unique=True)
    profilePicUrl = models.TextField(max_length=60)
    summary = models.TextField(max_length=50)

    def __str__(self):
        """A string representation of the model."""
        return self.name


class Projects(models.Model):
    resume = models.ForeignKey(Resume, on_delete=False)
    name = models.CharField(max_length=50)
    screenshots = models.ImageField()
    completion = models.DateField()
    started = models.DateField()
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.name
