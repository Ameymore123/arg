from django.db import models
from django.contrib.auth.models import User

class Docx_file(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docx_files', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # Store the time the file was generated


class Prompt(models.Model):
    sno = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    p_input = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Topic: ' + self.p_input

