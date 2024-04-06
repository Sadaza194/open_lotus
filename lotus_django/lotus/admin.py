from django.contrib import admin
from lotus.entry import Entry
from lotus.entryChilds import Memory
from lotus.entryChilds import Journal


# Register your models here.
admin.site.register(Entry)
admin.site.register(Memory)
admin.site.register(Journal)
