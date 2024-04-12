from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'phone', 'gender', 'nid', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        username = self.cleaned_data.get('email')  # Get username based on email
        if username:
            user.username = username
        if commit:
            user.save()
        return user
    
