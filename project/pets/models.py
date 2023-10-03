from django.db import models


class User(models.Model):
    surname = models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return f'{self.surname} {self.firstname} {self.email}'
    
    class Meta:
        verbose_name = 'user'
    
class Pet(models.Model):
    name = models.CharField(max_length=50) # Кличка
    kind = models.CharField(max_length=50, null=False) # Вид
    breed = models.CharField(max_length=30) # Порода
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f'{self.kind} {self.name}'
    
    class Meta:
        verbose_name = 'pet'
