from django.contrib import admin
from users.models import User

class UserModel(admin.ModelAdmin):
	list_display = ('id', 'username', 'email',)

admin.site.register(User, UserModel)