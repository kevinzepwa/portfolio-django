from django.db import models
from tinymce.models import HTMLField
import datetime

from django.utils.text import slugify

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=1000)
    intro = HTMLField()
    email = models.CharField(max_length=1000, default='')
    image = models.CharField(max_length=1000, default='')
    dribble = models.CharField(max_length=1000, default='')
    instagram = models.CharField(max_length=1000, default='')
    behance = models.CharField(max_length=1000, default='')
    role = models.CharField(max_length=1000, default='Designer')
    description = HTMLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=1000)
    percentage = models.CharField(max_length=1000)
    years = models.CharField(max_length=1000)
    icon = models.CharField(max_length=1000)
    description = HTMLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectType(models.Model):
    name = models.CharField(max_length=1000, default='')
    url = models.CharField(max_length=1000, default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000, default='')
    description = HTMLField()
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    slug = models.SlugField(db_index=True, max_length=10000, default='',
                            editable=False,
                            unique=True, blank=True, primary_key=True)
    image = models.CharField(max_length=1055, blank=True, null=True)
    video = models.CharField(max_length=1055, blank=True, null=True)
    active = models.BooleanField(default=False)
    link = models.CharField(max_length=1000)
    project_type = models.ForeignKey(ProjectType, related_name='project_type',
                                     on_delete=models.CASCADE,
                                     blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        '''Defines the ordering of the
         projects if retrieved'''
        ordering = ('date',)

    def __str__(self):
        return self.title

    def generate_slug(self):
        """generating a slug for the title of the project
            eg: this-is-an-project"""
        slug = slugify(self.title)
        new_slug = slug
        s = 1
        while Project.objects.filter(slug=new_slug).exists():
            """increase value of slug by one"""
            new_slug = f'{slug}-{s}'
            s += 1
        return new_slug

    def save(self, *args, **kwargs):
        """create a project and save to the database"""
        if not self.slug:
            self.slug = self.generate_slug()
        super(Project, self).save(*args, **kwargs)


def update_slug(sender, instance, signal, **kwargs):
    '''Signal to update an project's slug once title is updated'''
    if kwargs.get('updated', True):
        project = Project.objects.filter(slug=instance.pk)
        new_slug = slugify(instance.title)
        project.update(
            slug=new_slug
        )
