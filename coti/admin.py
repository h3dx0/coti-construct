from django.contrib import admin

# Register your models here.
from coti.models import TInstallation, TColor, TPresentation, TPayment, Seller, Profile, Frame, Accessory


class SellerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'telephone', 'commission']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'weight', 'price', 'price_in_usd']


class FrameAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'weight', 'price', 'frame_profile']


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'units', 'units_by_sqr_meters', 'price', 'price_in_usd', 'presentation', 'profile']


admin.site.register(TInstallation)
admin.site.register(TColor)
admin.site.register(TPresentation)
admin.site.register(TPayment)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Accessory, AccessoryAdmin)
