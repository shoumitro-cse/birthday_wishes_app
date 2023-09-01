from django.contrib import admin
from customers.models import Customer


class UserActionAdmin:
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if change:
            if hasattr(obj, "updated_by"):
                obj.updated_by = request.user
        else:
            if hasattr(obj, "created_by"):
                obj.created_by = request.user
            if hasattr(obj, "updated_by"):
                obj.updated_by = request.user
        obj.save()

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        obj.delete()


@admin.register(Customer)
class DashboardsAdmin(UserActionAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthdate', 'created_at', 'created_by', 'updated_at', 'updated_by']
    list_display_links = ['name']
    search_fields = ['name']
