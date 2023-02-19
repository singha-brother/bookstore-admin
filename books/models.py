import uuid 
import os 

from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete ,post_delete#, pre_save
from django.utils import timezone

# from cloudinary.models import CloudinaryField
import cloudinary

def rename_image(instance, filename):
    """
    Renames an uploaded image to include the current timestamp in the filename
    """
    _, ext = os.path.splitext(filename)
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f'{uuid.uuid4()}_{timestamp}{ext}'
    return os.path.join('covers/', new_filename)


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True 
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=300)
    price = models.IntegerField()
    pages = models.IntegerField(default=200)
    year = models.CharField(null=True, max_length=20, blank=True, default="")
    sold_out = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default="default.jpg")
    description = models.TextField(null=True, blank=True, default="")
    time_posted  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title 

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     try:
    #         img = Image.open(self.image.path)
    #         img = img.convert('RGB')
    #         if img.height > 400 or img.width > 300:
    #             output_size = (300,400)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
    #     except:
    #         pass


@receiver(pre_delete, sender=Book)
def photo_delete(sender, instance, **kwargs):
    print("-"*200)
    cloudinary.uploader.destroy(instance.image.url)
# @receiver(post_delete, sender=Book)
# def post_save_image(sender, instance, *args, **kwargs):
#     """ Clean Old Image file """
#     try:
#         if instance.image.name != 'default.jpg':
#             instance.image.delete(save=False)
#     except:
#         pass

# @receiver(pre_save, sender=Book)
# def pre_save_image(sender, instance, *args, **kwargs):
#     """ instance old image file will delete from os """
#     try:
#         old_img = instance.__class__.objects.get(id=instance.id).image.path
#         try:
#             new_img = instance.image.path
#         except:
#             new_img = None
#         if new_img != old_img:
#             if os.path.exists(old_img) and not old_img.endswith("default.png"):
#                 os.remove(old_img)
#     except:
#         pass