from django.conf import settings


DEFAULT_APP_NAME = 'django_org'
DJANGO_ORG_APP_NAME = getattr(settings, 'DJANGO_ORG_APP_NAME', DEFAULT_APP_NAME)

DJANGO_ORG_ENTERPRISE = getattr(settings, 'DJANGO_ORG_ENTERPRISE', f'{DEFAULT_APP_NAME}.Enterprise')
DJANGO_ORG_POST = getattr(settings, 'DJANGO_ORG_POST', f'{DEFAULT_APP_NAME}.Post')
DJANGO_ORG_WORK_MODE = getattr(settings, 'DJANGO_ORG_WORK_MODE', f'{DEFAULT_APP_NAME}.WorkMode')
DJANGO_ORG_WORK_SHIFT = getattr(settings, 'DJANGO_ORG_WORK_SHIFT', f'{DEFAULT_APP_NAME}.WorkShift')
DJANGO_ORG_DEPARTMENT_TYPE = getattr(settings, 'DJANGO_ORG_DEPARTMENT_TYPE', f'{DEFAULT_APP_NAME}.DepartmentType')
DJANGO_ORG_DEPARTMENT = getattr(settings, 'DJANGO_ORG_DEPARTMENT', f'{DEFAULT_APP_NAME}.Department')
DJANGO_ORG_PERSON = getattr(settings, 'DJANGO_ORG_PERSON', f'{DEFAULT_APP_NAME}.Person')
DJANGO_ORG_EMPLOYEE = getattr(settings, 'DJANGO_ORG_EMPLOYEE', f'{DEFAULT_APP_NAME}.Employee')
