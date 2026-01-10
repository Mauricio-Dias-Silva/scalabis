
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print("Password set to 'admin123' successfully.")
except User.DoesNotExist:
    print("User 'admin' does not exist.")
