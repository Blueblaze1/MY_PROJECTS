from django.db import models

class Txt(models.Model):
    text_file=models.FileField(upload_to="txt/")
