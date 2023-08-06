from django.contrib import admin

from django_org import models, forms


from .settings import (
    DEFAULT_APP_NAME,
    DJANGO_ORG_ENTERPRISE,
    DJANGO_ORG_POST,
    DJANGO_ORG_WORK_MODE,
    DJANGO_ORG_WORK_SHIFT,
    DJANGO_ORG_DEPARTMENT_TYPE,
    DJANGO_ORG_DEPARTMENT,
    DJANGO_ORG_PERSON,
    DJANGO_ORG_EMPLOYEE
)


if DJANGO_ORG_ENTERPRISE == f'{DEFAULT_APP_NAME}.Enterprise':
    @admin.register(models.Enterprise)
    class EnterpriseAdmin(admin.ModelAdmin):
        form = forms.EnterpriseAdminForm
        list_display = ('name', 'time_zone')
        list_display_links = ('name',)
        search_fields = ('name',)
        ordering = ('name',)


if DJANGO_ORG_POST == f'{DEFAULT_APP_NAME}.Post':
    @admin.register(models.Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'name',)
        list_display_links = ('name',)
        search_fields = ('name',)
        ordering = ('enterprise__name', 'name',)


if DJANGO_ORG_WORK_MODE == f'{DEFAULT_APP_NAME}.WorkMode':
    @admin.register(models.WorkMode)
    class WorkModeAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'name',)
        list_display_links = ('name',)
        search_fields = ('name',)
        ordering = ('enterprise__name', 'name',)


if DJANGO_ORG_WORK_SHIFT == f'{DEFAULT_APP_NAME}.WorkShift':
    @admin.register(models.WorkShift)
    class WorkShiftAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'work_mode', 'name', 'number', 'start', 'end',)
        list_display_links = ('name',)
        search_fields = ('work_mode', 'name',)
        ordering = ('enterprise__name', 'work_mode__name', 'number', 'name',)


if DJANGO_ORG_DEPARTMENT_TYPE == f'{DEFAULT_APP_NAME}.DepartmentType':
    @admin.register(models.DepartmentType)
    class DepartmentTypeAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'name',)
        list_display_links = ('name',)
        search_fields = ('name',)
        ordering = ('enterprise', 'name',)


if DJANGO_ORG_DEPARTMENT == f'{DEFAULT_APP_NAME}.Department':
    @admin.register(models.Department)
    class DepartmentAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'parent', 'department_type', 'name',)
        list_display_links = ('name',)
        search_fields = ('name',)
        ordering = ('enterprise__name', 'parent__name', 'department_type', 'name',)


if DJANGO_ORG_PERSON == f'{DEFAULT_APP_NAME}.Person':
    @admin.register(models.Person)
    class PersonAdmin(admin.ModelAdmin):
        list_display = ('last_name', 'first_name', 'middle_name', 'user',)
        list_display_links = ('last_name', 'first_name', 'middle_name',)
        search_fields = list_display_links
        ordering = list_display_links


if DJANGO_ORG_EMPLOYEE == f'{DEFAULT_APP_NAME}.Employee':
    @admin.register(models.Employee)
    class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('enterprise', 'department', 'post', 'person',)
        list_display_links = ('person',)
        search_fields = ('person',)
        ordering = ('enterprise__name', 'department__name', 'post', 'person',)
