from django.db import models



# title,director,runtime,year,language,poster

class Movie(models.Model):

    title = models.CharField(max_length=200)

    director = models.CharField(max_length=200)
    
    runtime = models.CharField(max_length=200)
    
    year = models.CharField(max_length=200)
    
    language = models.CharField(max_length=200)
    
    poster = models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):

        return self.title
    



