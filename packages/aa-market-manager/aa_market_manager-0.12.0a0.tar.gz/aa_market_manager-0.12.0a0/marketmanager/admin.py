from eveuniverse.models import (
    EveGroup, EveMarketGroup, EveRegion, EveSolarSystem, EveType,
)

from django.contrib import admin

from allianceauth.services.hooks import get_extension_logger
from esi.models import Token

from marketmanager.app_settings import (
    MARKETMANAGER_TASK_PRIORITY_PRICE_CONFIGS,
    MARKETMANAGER_TASK_PRIORITY_SUPPLY_CONFIGS,
)
from marketmanager.models import (
    Channel, ManagedSupplyConfig, Order, PriceConfig, PrivateConfig,
    PublicConfig, StatisticsConfig, Structure, SupplyConfig, Webhook,
)
from marketmanager.tasks import run_price_config, run_supply_config

from .admin_helpers import list_2_html_w_tooltips

logger = get_extension_logger(__name__)


@admin.register(PublicConfig)
class PublicConfigAdmin(admin.ModelAdmin):
    filter_horizontal = ["fetch_regions"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # This should filter regions to valid market regions, ie. no shattered, AT or Jove
        if db_field.name == "fetch_regions":
            kwargs["queryset"] = EveRegion.objects.filter(id__lt="11000000")
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(StatisticsConfig)
class StatisticsConfigAdmin(admin.ModelAdmin):
    filter_horizontal = ["calculate_regions"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # This should filter regions to valid market regions, ie. no shattered, AT or Jove
        if db_field.name == "calculate_regions":
            kwargs["queryset"] = EveRegion.objects.filter(id__lt="11000000")
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(PrivateConfig)
class PrivateConfigAdmin(admin.ModelAdmin):
    list_display = ('token', 'failed', 'failure_reason')
    filter_horizontal = ["valid_corporations", "valid_structures"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "token":
            required_scopes = ['esi-markets.structure_markets.v1']
            kwargs["queryset"] = Token.objects.all(
            ).require_scopes(required_scopes)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SupplyConfig)
class SupplyConfigAdmin(admin.ModelAdmin):
    list_display = (
        'eve_type', 'buy_order', 'volume', 'price',
        '_locations', 'last_result_volume', 'last_run')
    filter_horizontal = [
        "structure", "structure_type", "webhooks",
        "debug_webhooks", "solar_system", "region",
        "channels", "debug_channels"]
    autocomplete_fields = ['eve_type']
    list_filter = (
        'buy_order', 'webhooks',
        'debug_webhooks', 'managed_supply_config')
    actions = ['run_selected_supply_configs']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Only items that have market groups?
        if db_field.name == "eve_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_market_group__isnull=False, published=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # This should filter Citadels (1657) and NPC Stations (15) as viable Structure_Types for this selection
        # This should filter regions to valid market regions, ie. no shattered, AT or Jove
        if db_field.name == "structure_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_group__id__in=[15, 1657], published=1)
        if db_field.name == "region":
            kwargs["queryset"] = EveRegion.objects.filter(id__lt="11000000")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    @admin.action(description="Run Selected SupplyConfigs")
    def run_selected_supply_configs(modeladmin, request, queryset):
        for config in queryset:
            run_supply_config.apply_async(
                args=[config.id], priority=MARKETMANAGER_TASK_PRIORITY_SUPPLY_CONFIGS)

    def _locations(self, obj):
        my_groups = [x.name for x in obj.structure.order_by('name')]

        return list_2_html_w_tooltips(
            my_groups,
            10
        )


@admin.register(PriceConfig)
class PriceConfigAdmin(admin.ModelAdmin):
    list_display = (
        '_types', 'buy_order', 'price', '_locations', 'last_run')
    filter_horizontal = [
        'eve_type', "eve_market_group", "eve_group", "structure", "structure_type",
        "webhooks", "debug_webhooks", "solar_system", "region", "channels", "debug_channels"]
    list_filter = (
        'buy_order', 'webhooks', 'debug_webhooks', )
    actions = ['run_selected_price_configs']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Only items that have market groups?
        if db_field.name == "eve_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_market_group__isnull=False, published=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # This should filter Citadels (1657) and NPC Stations (15) as viable Structure_Types for this selection
        # This should filter regions to valid market regions, ie. no shattered, AT or Jove
        if db_field.name == "structure_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_group__id__in=[15, 1657], published=1)
        if db_field.name == "eve_region":
            kwargs["queryset"] = EveRegion.objects.filter(id__lt="11000000")
        if db_field.name == "eve_solar_system":
            kwargs["queryset"] = EveSolarSystem.objects.filter(
                id__lt="21000000")
        if db_field.name == "eve_group":
            kwargs["queryset"] = EveGroup.objects.filter(published=1)
        if db_field.name == "eve_market_group":
            kwargs["queryset"] = EveMarketGroup.objects.filter(
                parent_market_group__isnull=True)
        if db_field.name == "eve_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_market_group__isnull=False, published=1)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    @admin.action(description="Run Selected PriceConfig")
    def run_selected_price_configs(modeladmin, request, queryset):
        for config in queryset:
            run_price_config.apply_async(
                args=[config.id], priority=MARKETMANAGER_TASK_PRIORITY_PRICE_CONFIGS)

    def _locations(self, obj):
        my_groups = [x.name for x in obj.structure.order_by('name')]

        return list_2_html_w_tooltips(
            my_groups,
            10
        )

    def _types(self, obj):
        my_groups = [x.name for x in obj.eve_type.order_by('name')]

        return list_2_html_w_tooltips(
            my_groups,
            10
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('eve_type', 'price', 'eve_solar_system', 'is_buy_order',
                    'issued_by_character', 'issued_by_corporation', 'updated_at')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'solar_system', 'eve_type',
                    'owner_id', 'pull_market', 'updated_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # This should filter Citadels (1657) and NPC Stations (15) as viable Structure_Types for this selection
        if db_field.name == "eve_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_group__id__in=[15, 1657], published=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ManagedSupplyConfig)
class ManagedSupplyConfigAdmin(admin.ModelAdmin):
    list_display = (
        'managed_app_reason', 'managed_quantity',
        'managed_app_identifier')
    filter_horizontal = [
        "managed_structure", "managed_structure_type", "managed_webhooks", "managed_debug_webhooks",
        "managed_solar_system", "managed_region", "managed_channels", "managed_debug_channels"]
    list_filter = (
        'managed_buy_order', 'managed_webhooks',
        'managed_debug_webhooks')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Only items that have market groups?
        if db_field.name == "managed_eve_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_market_group__isnull=False, published=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # This should filter Citadels (1657) and NPC Stations (15) as viable Structure_Types for this selection
        # This should filter regions to valid market regions, ie. no shattered, AT or Jove
        if db_field.name == "managed_structure_type":
            kwargs["queryset"] = EveType.objects.filter(
                eve_group__id__in=[15, 1657], published=1)
        if db_field.name == "managed_region":
            kwargs["queryset"] = EveRegion.objects.filter(id__lt="11000000")
        return super().formfield_for_manytomany(db_field, request, **kwargs)
