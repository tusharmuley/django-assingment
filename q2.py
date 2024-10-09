# Question 2: Do Django signals run in the same thread as the caller?
#Answer : Yes, Django signals run in the same thread as the caller by default. To demonstrate this, we can print the thread identifiers in both the main function and the signal handler.

# Here’s a code snippet that proves signals run in the same thread:


import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver
@receiver(post_save, sender=User)
def handle_user_saved(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

# In another part of your code where a User instance is saved:
print(f"Main thread: {threading.current_thread().name}")
new_user = User.objects.create(username='test_user', password='password')




# Explanation:

# You will see the same thread name printed in both the main thread and the signal handler, confirming that the signal runs in the same thread.