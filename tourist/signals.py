from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Tourist


@receiver(post_save, sender=Tourist)
def tourist_updated(sender, instance, created, **kwargs):
    if created:
        tourist = instance
        user = User.objects.create_user(tourist.username, tourist.email, tourist.password)
        tourist.user = user
        tourist.save()

@receiver(post_delete, sender=Tourist)
def tourist_deleted(sender, instance, **kwargs):
    tourist = instance
    user = tourist.user
    user.delete()
