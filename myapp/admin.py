from django.contrib import admin

from myapp.models import Project, About, Skill, ProjectType

admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(Skill)
admin.site.register(About)
