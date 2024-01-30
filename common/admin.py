from django.contrib import admin
from .models import Member


# Register your models here.

# admin.site.register(Member)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "firs_name", "age")
    list_display_links = ("id", "firs_name")
    search_fields = ("firs_name",)
    list_filter = ("is_active",)

# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     list_display = ("money", "members_count", "min_age")
#     list_display_links = ("money",)
#     search_fields = ("money_",)
#     list_filter = ("min_age",)
#
#
# @admin.register(Play)
# class PlayAdmin(admin.ModelAdmin):
#     list_display = ("min_age", "members_count", "min_ball")
#     list_display_links = ("min_ball",)
#     search_fields = ("min_ball",)
#     list_filter = ("min_age",)
