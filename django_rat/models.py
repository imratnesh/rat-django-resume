from django.db import models


# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=3, primary_key=True)
    profilePicUrl = models.CharField(max_length=100, null=True)
    summary = models.TextField(null=False)

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
