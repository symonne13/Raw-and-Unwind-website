from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

from .models import (
    Offer,
    LegacyPortfolio,
    CulturalImmersions,
    Blog,
)


# =========================================================
# OFFERS
# =========================================================

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "category",
        "price",
        "is_active",
        "is_featured",
        "display_order",
        "updated_at",
    )

    list_display_links = (
        "image_preview",
        "title",
    )

    list_filter = (
        "category",
        "is_active",
        "is_featured",
    )

    search_fields = (
        "title",
        "description",
        "category",
        "price",
    )

    list_editable = (
        "is_active",
        "is_featured",
        "display_order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview_large",
    )

    ordering = (
        "display_order",
        "-created_at",
    )

    fieldsets = (
        (
            "Offer Information",
            {
                "fields": (
                    "title",
                    "category",
                    "description",
                    "price",
                    "price_label",
                )
            },
        ),
        (
            "Offer Image",
            {
                "fields": (
                    "image",
                    "image_preview_large",
                )
            },
        ),
        (
            "Visibility & Display",
            {
                "fields": (
                    "is_active",
                    "is_featured",
                    "display_order",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" '
                'style="width:70px;height:50px;object-fit:cover;'
                'border-radius:6px;" />',
                obj.image.url
            )

        return "—"

    image_preview.short_description = "Image"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" '
                'style="max-width:500px;max-height:300px;'
                'object-fit:cover;border-radius:10px;" />',
                obj.image.url
            )

        return "No image uploaded."

    image_preview_large.short_description = "Image Preview"


# =========================================================
# LEGACY PORTFOLIO
# =========================================================

@admin.register(LegacyPortfolio)
class LegacyPortfolioAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "price",
        "currency",
        "tags",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "image_preview",
        "title",
    )

    list_filter = (
        "is_featured",
        "is_active",
        "currency",
    )

    search_fields = (
        "title",
        "tags",
        "includes",
        "content",
    )

    list_editable = (
        "is_featured",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview_large",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "Portfolio Information",
            {
                "fields": (
                    "title",
                    "currency",
                    "price",
                    "date",
                    "tags",
                )
            },
        ),
        (
            "Duration",
            {
                "fields": (
                    "duration_days",
                    "duration_nights",
                    "duration_hours",
                )
            },
        ),
        (
            "Experience Details",
            {
                "fields": (
                    "includes",
                    "content",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "main_image",
                    "image_preview_large",
                )
            },
        ),
        (
            "Website Settings",
            {
                "fields": (
                    "slug",
                    "is_featured",
                    "is_active",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" '
                'style="width:70px;height:50px;object-fit:cover;'
                'border-radius:6px;" />',
                obj.main_image.url
            )

        return "—"

    image_preview.short_description = "Image"

    def image_preview_large(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" '
                'style="max-width:500px;max-height:300px;'
                'object-fit:cover;border-radius:10px;" />',
                obj.main_image.url
            )

        return "No image uploaded."

    image_preview_large.short_description = "Image Preview"


# =========================================================
# CULTURAL IMMERSIONS
# =========================================================

@admin.register(CulturalImmersions)
class CulturalImmersionsAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "title",
        "season",
        "currency",
        "price",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "image_preview",
        "title",
    )

    list_filter = (
        "is_active",
        "is_featured",
        "currency",
    )

    search_fields = (
        "title",
        "season",
        "community_impact",
        "includes",
        "content",
    )

    list_editable = (
        "is_featured",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview_large",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "Experience Information",
            {
                "fields": (
                    "title",
                    "currency",
                    "price",
                    "season",
                    "community_impact",
                    "includes",
                    "content",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "main_image",
                    "image_preview_large",
                )
            },
        ),
        (
            "Website Settings",
            {
                "fields": (
                    "slug",
                    "is_featured",
                    "is_active",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" '
                'style="width:70px;height:50px;object-fit:cover;'
                'border-radius:6px;" />',
                obj.main_image.url
            )

        return "—"

    image_preview.short_description = "Image"

    def image_preview_large(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" '
                'style="max-width:500px;max-height:300px;'
                'object-fit:cover;border-radius:10px;" />',
                obj.main_image.url
            )

        return "No image uploaded."

    image_preview_large.short_description = "Image Preview"


# =========================================================
# BLOGS
# =========================================================

class BlogStatusFilter(admin.SimpleListFilter):

    title = "Status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("draft", "Draft"),
            ("published", "Published"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())

        return queryset


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "cover_thumbnail",
        "title",
        "about",
        "author",
        "status_badge",
        "is_featured",
        "published_at",
        "updated_at",
    )

    list_display_links = (
        "cover_thumbnail",
        "title",
    )

    list_filter = (
        BlogStatusFilter,
        "is_featured",
        "author",
    )

    search_fields = (
        "title",
        "about",
        "excerpt",
        "body",
    )

    list_editable = (
        "is_featured",
    )

    date_hierarchy = "published_at"

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "published_at",
        "cover_preview",
        "read_time_display",
    )

    actions = [
        "make_published",
        "make_draft",
        "mark_featured",
        "unmark_featured",
    ]

    fieldsets = (
        (
            "Blog Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "about",
                    "excerpt",
                    "body",
                )
            },
        ),
        (
            "Cover Image",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "author",
                    "status",
                    "is_featured",
                    "published_at",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "read_time_display",
                )
            },
        ),
    )

    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" '
                'style="width:70px;height:50px;object-fit:cover;'
                'border-radius:6px;" />',
                obj.cover_image.url
            )

        return "—"

    cover_thumbnail.short_description = "Image"

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" '
                'style="max-width:500px;max-height:300px;'
                'object-fit:cover;border-radius:10px;" />',
                obj.cover_image.url
            )

        return "No image uploaded."

    cover_preview.short_description = "Preview"

    def status_badge(self, obj):
        if obj.status == "published":
            return format_html(
                '<span style="background:#e6f4ea;color:#1a7d3a;'
                'padding:4px 10px;border-radius:20px;'
                'font-weight:600;">● Published</span>'
            )

        return format_html(
            '<span style="background:#fff8e1;color:#a07c00;'
            'padding:4px 10px;border-radius:20px;'
            'font-weight:600;">○ Draft</span>'
        )

    status_badge.short_description = "Status"

    def read_time_display(self, obj):
        return obj.read_time

    read_time_display.short_description = "Read Time"

    @admin.action(description="Publish selected posts")
    def make_published(self, request, queryset):
        updated = queryset.update(
            status="published",
            published_at=timezone.now()
        )

        self.message_user(
            request,
            f"{updated} post(s) published."
        )

    @admin.action(description="Move selected posts to Draft")
    def make_draft(self, request, queryset):
        updated = queryset.update(
            status="draft"
        )

        self.message_user(
            request,
            f"{updated} post(s) moved to draft."
        )

    @admin.action(description="Mark selected as Featured")
    def mark_featured(self, request, queryset):
        queryset.update(
            is_featured=True
        )

        self.message_user(
            request,
            "Selected posts marked as featured."
        )

    @admin.action(description="Remove Featured from selected")
    def unmark_featured(self, request, queryset):
        queryset.update(
            is_featured=False
        )

        self.message_user(
            request,
            "Featured flag removed."
        )