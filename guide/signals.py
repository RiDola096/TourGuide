from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Guide


@receiver(post_save, sender=Guide)
def guide_updated(sender, instance, created, **kwargs):
    if created:
        guide = instance
        user = User.objects.create_user(guide.username, guide.email, guide.password)
        guide.user = user
        guide.save()

@receiver(post_delete, sender=Guide)
def guide_deleted(sender, instance, **kwargs):
    guide = instance
    user = guide.user
    user.delete()
