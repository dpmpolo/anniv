import os
from anniv import settings
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anniv.settings")

# environment is now setup
from django.contrib.auth.models import User
users = User.objects.all()
emails = []
for user in users:
    if len(user.email) > 0:
        emails.append(user.email)
print emails
send_mail('New relationship goal available', 
         'Login to view you new relationship goal!', 
         'from@example.com',
         [emails], fail_silently=True)
