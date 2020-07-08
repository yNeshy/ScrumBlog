from djongo import models

# Create your models here.
class Users(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    class Meta :
        abstract : True 
    
    def __str__(self):
        return self.username + " - "+ self.role
    
    objects = models.DjongoManager()