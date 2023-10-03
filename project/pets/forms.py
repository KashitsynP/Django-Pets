from django import forms
from pets.models import User, Pet

class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            "surname": "Фамилия",
            "firstname": "Имя", 
            "age": "Возраст", 
            "email": "E-mail"
            }

class AddPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {
            "name": "Кличка",
            "kind": "Вид животного", 
            "breed": "Порода", 
            "owner": "Владелец"
            }
        