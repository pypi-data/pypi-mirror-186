from django.contrib import admin
from erp_sync.models import RequestLogs, ResponseLogs

# Register your models here.

admin.site.register(RequestLogs)
admin.site.register(ResponseLogs)
