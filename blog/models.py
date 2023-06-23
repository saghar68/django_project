from django.db import models



#title,text,about,created,status,user


class Post(models.Model):
    STATUS=(
        ('pub','PUBLISHED'),
        ('drf','DRAFT'),
    )
    
    ABOUT=(
        ('html','HTML'),
        ('css','CSS'),
        ('java','JAVA'),
        ('python','PYTHON'),
        ('django','DJANGO'),
        
    )
    
    title=models.CharField(max_length=150)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATUS,max_length=10)
    about=models.CharField(choices=ABOUT,max_length=10)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
  
    