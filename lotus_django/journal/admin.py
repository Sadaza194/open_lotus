from django.contrib import admin
from journal.models import Entry, Journal

# Register your models here.
admin.site.register(Entry)
admin.site.register(Journal)