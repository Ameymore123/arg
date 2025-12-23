from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.credits} Credits"

class Docx_file(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docx_files')
    timestamp = models.DateTimeField(auto_now_add=True)

class Prompt(models.Model):
    sno = models.AutoField(primary_key=True)
    p_input = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Topic: ' + self.p_input

# Transaction history (optional but recommended)
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)



    
