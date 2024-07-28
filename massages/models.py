from django.db import models
class User_massages(models.Model):
    letter_theme = models.CharField(max_length=100,default=None)
    sending_data = models.DateTimeField(default=None)
    receiving_data = models.DateTimeField(default=None)
    massage_text = models.CharField(max_length=50,default=None)
    files_list = models.CharField(default=None)


