import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler to print the current thread
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Example function that creates a user and checks the thread
def create_user(request):
    print(f"View running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='test_user')
