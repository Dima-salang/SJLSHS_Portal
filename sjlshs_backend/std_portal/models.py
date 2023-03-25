from django.db import models
from accounts.models import StudentUser, StudentSection, TeacherUser, StudentYear, Subject, Db_Students
from django.conf import settings
from sjlshs_backend.settings import AUTH_USER_MODEL
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files import File
from django.utils.text import slugify
from sorl.thumbnail import get_thumbnail
from tinymce import models as tinymce_models
from io import BytesIO
import os
import fitz

def get_file_extension(file_name):
    """Returns the file extension of a given file name."""
    _, extension = os.path.splitext(file_name)
    return extension


# Create your models here.

class Post(models.Model):
    Author = models.CharField(max_length=100, null=True)
    Title = models.CharField(max_length=50)
    Body = models.TextField(null=True)
    Section = models.ForeignKey(StudentSection,
    null=True, on_delete=models.CASCADE)
    Published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Author} {self.Title}"


class Modules(models.Model):
    title = models.CharField(max_length=255)
    grade = models.ForeignKey(StudentYear, null=True, 
    blank=True, on_delete=models.SET_NULL, related_name='grade')
    subject = models.ForeignKey(Subject, null=True,
    on_delete=models.SET_NULL, related_name='subject')
    thumbnail = models.ImageField(upload_to='media/modules/module_thumbnails',
    blank=True, null=True)
    file = models.FileField(upload_to=f"media/modules/")

    def __str__(self):
        return f"{self.title} - {self.grade}"
    
    def generate_pdf_thumbnail(self):
        # Get the path of the original PDF file
        original_file_path = self.file.path

        # Define the name and path for the thumbnail file
        thumbnail_path = f'media/modules/module_thumbnails/{slugify(self.title)}_thumbnail.jpg'
        thumbnail_file_path = os.path.join(settings.MEDIA_ROOT, thumbnail_path)

        # Generate the thumbnail using PyMuPDF
        with fitz.open(original_file_path) as doc:
            page = doc.load_page(0)
            pix = page.get_pixmap(alpha=False)
            with BytesIO(pix.tobytes()) as output:
                img = Image.open(output)
                img.save(thumbnail_file_path, format="JPEG")

        # Save the thumbnail to the database
        with open(thumbnail_file_path, 'rb') as f:
            django_file = File(f)
            self.thumbnail.save(thumbnail_path, django_file, save=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.thumbnail:
            self.generate_pdf_thumbnail()
        

class Schedule(models.Model):
    section = models.OneToOneField(StudentSection, 
    on_delete=models.CASCADE, related_name='sched_section')
    schedule_file = models.FileField(upload_to=f'media/schedules/', 
    max_length=255)

    def __str__(self):
        return f"{self.section} Schedule"

