from djongo import models

# Create your models here.


class Categories(models.Model):
    
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    class Meta :
        abstract : True 
    
    def __str__(self):
        return self.name

    objects = models.DjongoManager()



class Articles(models.Model):
    
    title = models.CharField(max_length=100, default='ANONYMOUS')
    contributor = models.CharField(max_length=30, default='ANONYMOUS')
    source = models.CharField(max_length=1000, default='unproven')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    image_link = models.TextField( default='ANONYMOUS')
    html_text = models.TextField(default='<body> Empty set </body>')
    

    class Meta :
        abstract : True 
    
    def __str__(self):
        return self.contributor+" added a "+self.category.__str__()+" about :"+self.title

    objects = models.DjongoManager()
