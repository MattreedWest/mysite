from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500, default = "")
    pub_Date = models.DateTimeField("date published")

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, default = "")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.text
