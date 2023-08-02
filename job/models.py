from django.db import models
from django.utils.text import slugify

'''
django model fileds:
    - html widget
    - validation
    - db size
'''

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return 'jobs/%s.%s'%(instance.id,extension)

# Create your models here.
class Job(models.Model): #table
    title = models.CharField(max_length=100)    #column
    #location
    job_type = models.CharField(max_length=15, choices= JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null= True)

    def save(self, *args, **kwargs):
        ## logic
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
def cv_upload(instance, filename):
    imagename, extension = filename.split(".")
    return 'apply/%s_cv.%s'%(instance.name,extension)

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(null=True)
    cv = models.FileField(upload_to=cv_upload)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
'''
Relations:
    - One to Many   [author - posts]
    - Many to Many  [user - groups]
    - One to one    [user - profile]
'''