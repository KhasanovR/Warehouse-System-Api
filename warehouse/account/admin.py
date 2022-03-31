from django.contrib import admin
from reversion.admin import VersionAdmin

from warehouse.account.models import User


@admin.register(User)
class UserAdmin(VersionAdmin):
    pass
