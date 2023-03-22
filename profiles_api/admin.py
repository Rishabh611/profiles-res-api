from django.contrib import admin
from .models import UserProfiles, ProfileFeedItem

# Register your models here.
admin.site.register(UserProfiles)
admin.site.register(ProfileFeedItem)
