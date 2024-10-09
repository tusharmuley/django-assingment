# Question 3: Do Django signals run in the same database transaction as the caller?
# By default, Django signals run in the same database transaction as the caller. The post_save signal is fired after the model instance has been saved to the database. However, this only occurs after the database transaction is committed if you are using atomic transactions.

# Here’s a code snippet demonstrating this:


from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver
@receiver(post_save, sender=User)
def handle_user_saved(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal running inside the transaction")
    else:
        print("Signal running outside the transaction")

# Create a user within an atomic transaction
with transaction.atomic():
    new_user = User.objects.create(username='test_user', password='password')
    
    
    
    
    
# Explanation:

# The signal handler checks whether it’s running within a transaction using transaction.get_connection().in_atomic_block. Since post_save is fired after the model instance is saved, it will be within the transaction.