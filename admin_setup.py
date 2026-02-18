from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from database import DATABASE_URL


site = AdminSite(settings=Settings(
    database_url=DATABASE_URL,
    admin_user='admin',
    admin_password='password123',
    language="en_US"
))