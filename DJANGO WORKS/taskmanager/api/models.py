from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    @property
    def works(self):

        qs=Task.objects.filter(employee_object=self)

        return qs

    def __str__(self):

        return self.name

class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    completed_date=models.DateTimeField()

    assigned_date=models.DateTimeField()

    status=models.BooleanField(default=False)

    employee_object=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        
        return self.title
    
    