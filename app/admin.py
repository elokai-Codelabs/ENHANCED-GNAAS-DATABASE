from django.contrib import admin
from .models import Executive,Position,Committee,Committee_Member, Union,Zone, Fellowship,Patron,Alumni_rep, Program
# -----------------------------
# EXCEL UPLOAD
from import_export.admin import ImportExportModelAdmin
# ----------------------------
# Register your models here.
admin.site.register(Executive)
admin.site.register(Position)
admin.site.register(Committee)
admin.site.register(Committee_Member)
admin.site.register(Union)
admin.site.register(Zone)
admin.site.register(Fellowship)
admin.site.register(Patron)
admin.site.register(Alumni_rep)
admin.site.register(Program)




class ExecutiveAdmin(ImportExportModelAdmin):
    list_display = '__all__'



