from fastapi_amis_admin.admin import admin
from admin_setup import site
from src.product.models import Category


@site.register_admin
class CategoryAdmin(admin.ModelAdmin):
    page_schema = "category"
    model = Category
    search_fields = [Category.title]
    list_filter = [Category.title, Category.id]
    list_display = [
        Category.id,
        Category.title,
        Category.description,
        Category.created_at,
    ]
