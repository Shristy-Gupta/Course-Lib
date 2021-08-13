from django.contrib import admin
from app.models import courses,UserCourse,Payment,learning,prerequisite,tag,video


# To show learning,prerequisite,tag within courses table
class videoAdmin(admin.TabularInline):
    model=video

class TagAdmin(admin.TabularInline):
    model=tag

class learningAdmin(admin.TabularInline):
    model=learning

class prerequisiteTagAdmin(admin.TabularInline):
    model=prerequisite

class courseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin,learningAdmin,prerequisiteTagAdmin,videoAdmin]
    list_display=["name","price","discount","active"]

class payementAdmin(admin.ModelAdmin):
    model=Payment
    list_display=["order_id","user","course","status"]
    list_filter=["status","course"]    
# Register your models here.

admin.site.register(courses,courseAdmin)
admin.site.register(video)
admin.site.register(Payment,payementAdmin)
admin.site.register(UserCourse)
# admin.site.register(learning)
# admin.site.register(prerequisite)
# admin.site.register(tag)
