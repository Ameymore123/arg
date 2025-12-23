from django.contrib import admin
from .models import Prompt, Docx_file, Profile, Transaction
# Register your models here.


admin.site.register(Prompt)
admin.site.register(Docx_file)


admin.site.register(Profile)
admin.site.register(Transaction)
