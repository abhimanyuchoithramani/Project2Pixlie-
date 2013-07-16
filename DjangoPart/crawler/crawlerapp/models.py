from django.db import models

# Making of the 1st model class 
class Directory(models.Model):
    
    Bussiness_name = models.CharField(max_length=300)
    Description = models.CharField(max_length=900)
    Number = models.CharField(max_length=100)
    Web_url = models.CharField(max_length=800)
    Catogory = models.CharField(max_length=200)


    def __unicode__(self):
        return self.Bussiness_name
# here foriegn key is included as a single Business can have multiple addresses.
class Adress(models.Model):
   directory =  models.ForeignKey(Directory)
   adress_name =  models.CharField(max_length=300)
   def __unicode__(self):
        return self.adress_name
# here also foriegn key is included as a single Business can have multiple Pictures.
class Photos(models.Model):
   directory =  models.ForeignKey(Directory)
   Photo_path =  models.CharField(max_length=100)
   Photo_name =  models.CharField(max_length=100)
   def __unicode__(self):
        return self.Photo_name
