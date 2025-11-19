from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUsertionForm(UserCreationForm):
  model = CustomUser
  fields = ('username','email','password1','passwors2')
  
class Meta:
    pass