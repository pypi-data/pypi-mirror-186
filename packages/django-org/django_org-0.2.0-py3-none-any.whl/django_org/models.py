from django_org import abstract_models as org_models

from .settings import (
    DJANGO_ORG_APP_NAME,
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


__all__ = []


if DJANGO_ORG_ENTERPRISE == f'{DEFAULT_APP_NAME}.Enterprise':
    class Enterprise(org_models.org.AbstractEnterprise):
        ...


    __all__.append('Enterprise')


if DJANGO_ORG_POST == f'{DEFAULT_APP_NAME}.Post':
    class Post(org_models.org.AbstractPost):
        ...


    __all__.append('Post')


if DJANGO_ORG_WORK_MODE == f'{DEFAULT_APP_NAME}.WorkMode':
    class WorkMode(org_models.shift.AbstractWorkMode):
        ...


    __all__.append('WorkMode')


if DJANGO_ORG_WORK_SHIFT == f'{DEFAULT_APP_NAME}.WorkShift':
    class WorkShift(org_models.shift.AbstractWorkShift):
        ...


    __all__.append('WorkShift')


if DJANGO_ORG_DEPARTMENT_TYPE == f'{DEFAULT_APP_NAME}.DepartmentType':
    class DepartmentType(org_models.dept.AbstractDepartmentType):
        ...


    __all__.append('DepartmentType')


if DJANGO_ORG_DEPARTMENT == f'{DEFAULT_APP_NAME}.Department':
    class Department(org_models.dept.AbstractDepartment):
        ...


    __all__.append('Department')


if DJANGO_ORG_PERSON == f'{DEFAULT_APP_NAME}.Person':
    class Person(org_models.people.AbstractPerson):
        ...


    __all__.append('Person')


if DJANGO_ORG_EMPLOYEE == f'{DEFAULT_APP_NAME}.Employee':
    class Employee(org_models.people.AbstractEmployee):
        ...


    __all__.append('Employee')
