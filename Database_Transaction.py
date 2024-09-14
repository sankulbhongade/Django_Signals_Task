from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler that raises an exception
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started")
    raise Exception("Error in signal handler")  # Simulate an error

# Function that creates a user within a transaction
def create_user(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username='test_user')
            print("User created in view")
    except Exception as e:
        print(f"Transaction failed: {e}")
