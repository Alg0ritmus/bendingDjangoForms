from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200, blank=True)
    kg =  models.IntegerField( null= True)

    def __str__(self) -> str:
        return str(self.id) +"| "+ self.name

class FriendShip(models.Model):
    persons = models.ManyToManyField(Person)

    def __str__(self) -> str:
        return str(self.id)

class Secret(models.Model):
    secret = models.CharField(max_length=200, null = True, blank=True)
    # pretty straight-forward ... 1-1
    owner = models.OneToOneField(Person,on_delete=models.CASCADE, blank=True, null=True,related_name="owner")
    # 1 person(involved not owner)  can have multiple Secret
    person1 = models.ForeignKey(FriendShip,on_delete=models.CASCADE, blank=True, null=True,related_name="involved")

    def __str__(self) -> str:
        return self.secret

#######################################################x
#       BASKETBALL DB

# over ride user

   

class Archive(models.Model):
    # 1 user can have multiple Archives
    # 1 archive can have only 1 User
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    established = models.DateField(null=True) 

    def __str__(self) -> str:
        return str(self.user.username)


class Article(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True,blank=True)
    #images = 
    likes = models.IntegerField(null = True, blank=True)
    disslikes = models.IntegerField(null = True,blank=True)
    archive = models.ForeignKey(Archive,on_delete=models.CASCADE,null=True)
    established = models.DateField(null=True) 

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    likes = models.IntegerField(null = True,blank=True)
    disslikes = models.IntegerField(null = True,blank=True)
    context = models.TextField(null=True,blank=True)
    # multiple comments <-> One  User
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    articel = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    established = models.DateField() 

    def __str__(self) -> str:
        return str(self.author.username)

class Pinned(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE,null=True,blank=True)
    established= models.DateField()

    def __str__(self) -> str:
        return str(self.article.title)


#######################################

# USING upload_to...
""" 
class UploadFile(models.Model):
    pdf_file = models.FileField(upload_to='filesFromUsers')

    def __str__(self) -> str:
        return self.pdf_file.name
 """
# Using MEDIA_ROOT & MEDIA_URL
class UploadFile(models.Model):
    pdf_file = models.FileField()

    def __str__(self) -> str:
        return self.pdf_file.name

# upload multiple files

