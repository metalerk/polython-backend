from django.contrib import admin
from stores.models import Store

class StoreModel(admin.ModelAdmin):
	list_display = ('id', 'name', 'owner', 'products',)

admin.site.register(Store, StoreModel)