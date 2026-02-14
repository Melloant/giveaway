from django.contrib import admin
from .models import Participant, Gift, Registration, Ad


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'municipio', 'created_at')
    search_fields = ('name', 'phone', 'email', 'municipio')


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'sponsor', 'start', 'end', 'active')
    list_filter = ('active', 'sponsor')
    search_fields = ('title', 'sponsor')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'gift', 'created_at')
    search_fields = ('participant__name', 'participant__phone', 'gift__title')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'sponsor', 'active', 'start', 'end')
    list_filter = ('active', 'sponsor', 'position')
    search_fields = ('title', 'sponsor')
