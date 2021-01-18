from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()