from django.contrib import admin
from sales.models import Sale


class SalesAdmin(admin.ModelAdmin):
	list_display = ('id', 'buyer', 'store', 'status', 'timestamp')


admin.site.register(Sale, SalesAdmin)