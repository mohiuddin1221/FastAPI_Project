
from fastapi_amis_admin.admin import admin
from admin_setup import site 
from src.auth.models import User 

@site.register_admin 
class UserAdmin(admin.ModelAdmin):
    page_schema = "user_account" 
    model = User 
    search_fields = [User.username] 
    list_filter = [User.username] 
    list_display = [User.uid, User.username, User.email]