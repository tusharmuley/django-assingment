# Question 1: By default, are Django signals executed synchronously or asynchronously?
# Django signals are executed synchronously by default. This means that the signal's receivers are called in the same process and thread as the caller. To prove this with a code snippet, we can define a simple signal and log the time taken to handle it.

# Here's a code snippet demonstrating synchronous signal execution:

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver
@receiver(post_save, sender=User)
def handle_user_saved(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(3)  # Simulating a delay to demonstrate synchronicity
    print("Signal handler finished")

# In another part of your code where a User instance is saved:
new_user = User.objects.create(username='test_user', password='password')
print("User saved")


# Explanation:

# When User.objects.create() is called, the signal handler handle_user_saved will be executed immediately.
# The time.sleep(3) simulates a delay in the signal handler, and you will see the User saved message only after the signal handler finishes executing, proving that it's executed synchronously.