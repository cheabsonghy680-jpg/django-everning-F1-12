from django.db import models

# Create your models here.
class patient(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    sex = models.CharField(max_length=6,null=False,blank=False,choices={'male':'Male','female':'Female'})
    dob = models.DateField(null=False,blank=False)
    phone = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=150,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        db_table = "patients"
        ordering = ['-created']


