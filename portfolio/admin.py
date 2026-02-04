from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Project, Skill, ProfilePhoto, Role, Certification
# Register your models here.

# ================= Profile Photo Inline =================
class ProfilePhotoInline(admin.TabularInline):
    model = ProfilePhoto
    extra = 1
    ordering = ("order",)
    fields = ("image", "order", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Preview"


# ================= Profile =================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "updated_at")
    search_fields = ("full_name", "title", "email")
    list_filter = ("updated_at",)
    inlines = [ProfilePhotoInline]
    fields = (
        "full_name",
        "title",
        "bio",
        "about",
        "email",
        "resume",
        "linkedin",
        "github",
        "facebook",
    )


# ================= Project =================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "created_at", "live_link")
    search_fields = ("title", "tech_stack")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


# ================= Skill =================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# ================= Profile Photo (Standalone view) =================
@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ("profile", "order", "image_preview")
    list_editable = ("order",)
    list_filter = ("profile",)
    ordering = ("profile", "order")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Preview"


# ================= Role =================
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("title",)


# ================= Certification =================
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "date_awarded", "certificate_link")
    search_fields = ("title", "issuer")
    list_filter = ("issuer", "date_awarded")
    ordering = ("-date_awarded",)

    def certificate_link(self, obj):
        if obj.certificate_url:
            return format_html(
                '<a href="{}" target="_blank">View Certificate</a>',
                obj.certificate_url
            )
        return "-"

    certificate_link.short_description = "Certificate"

