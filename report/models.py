from django.db import models

class Docx_file(models.Model):
    sr = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    file = models.FileField(upload_to='docx_files', null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True)  # Allowing session_key to be null or blank


class Prompt(models.Model):
    sno = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    p_input = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Topic: ' + self.p_input


