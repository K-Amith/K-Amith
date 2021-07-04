from django.contrib import admin
from .models import MyObjective,MyProfile,Skill,Feed_back,Project,PersonalDetail,Hobbie,Workshop,Award

# Register your models here.
admin.site.register(Skill)
admin.site.register(Award)
admin.site.register(Workshop)
admin.site.register(Hobbie)
admin.site.register(PersonalDetail)
admin.site.register(Project)
admin.site.register(Feed_back)
admin.site.register(MyObjective)
admin.site.register(MyProfile)
