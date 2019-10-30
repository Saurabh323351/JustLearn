from django.contrib import admin

# Register your models here.


from Notes.models import Note

class NoteAdmin(admin.ModelAdmin):

    list_display=['id','title','description','image','color','reminder','modified_at','created_at']

admin.site.register(Note,NoteAdmin)
