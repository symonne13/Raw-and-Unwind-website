from django.db import models
import uuid
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary_storage.storage import MediaCloudinaryStorage

# =========================================================
# IMAGE UPLOAD HELPER
# =========================================================

def upload_image_to(instance, filename):
    name = getattr(instance, 'slug', None) or slugify(
        getattr(instance, 'title', 'image')
    )

    name = name[:40]

    ext = filename.split('.')[-1]

    folder = instance.__class__.__name__.lower()

    return f"{folder}/images/{name}.{ext}"


# =========================================================
# LEGACY PORTFOLIO
# =========================================================

class LegacyPortfolio(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=255
    )

    currency = models.CharField(
        max_length=10,
        default="USD, KES"
    )

    price = models.CharField(
        max_length=100,
        help_text="Price per person"
    )

    date = models.DateField(
        null=True,
        blank=True
    )

    duration_days = models.PositiveIntegerField(
        default=0
    )

    duration_nights = models.PositiveIntegerField(
        default=0
    )

    duration_hours = models.PositiveIntegerField(
        default=0
    )

    includes = models.TextField(
        help_text="Hot air balloon included"
    )

    tags = models.CharField(
        max_length=255,
        help_text="Ultimate Safari or Cruise Exclusive"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=255
    )

    main_image = models.ImageField(
        upload_to=upload_image_to
    )

    content = RichTextUploadingField()

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "LegacyPortfolio"


# =========================================================
# CULTURAL IMMERSIONS
# =========================================================

class CulturalImmersions(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=255
    )

    currency = models.CharField(
        max_length=10,
        default="USD"
    )

    price = models.CharField(
        max_length=100,
        help_text="Price per person"
    )

    season = models.CharField(
        max_length=255,
        help_text="eg. July - October"
    )

    community_impact = models.CharField(
        max_length=255,
        help_text="Supports Swahili artisan cooperatives and heritage preservation"
    )

    includes = models.TextField(
        help_text="6 days, luxury mobile camp, Maasai cultural immersion"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=255
    )

    main_image = models.ImageField(
        upload_to=upload_image_to,
        storage=MediaCloudinaryStorage()
    )

    content = RichTextUploadingField()

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "CulturalImmersion"


# =========================================================
# BLOG
# =========================================================

class Blog(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=255
    )

    cover_image = models.ImageField(
        upload_to=upload_image_to,
        help_text="Recommended size: 1200×630px."
    )

    about = models.CharField(
        max_length=100,
        help_text="eg. Conservation or Eco-Travel"
    )

    excerpt = models.TextField(
        max_length=200,
        help_text="Short summary shown on listing cards (max 200 chars)."
    )

    body = RichTextUploadingField()

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    is_featured = models.BooleanField(
        default=False,
        help_text="Pin this post to the featured slot on the homepage."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Leave blank to use the time of first publish."
    )

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # Automatically generate slug
        if not self.slug:

            base_slug = slugify(self.title)

            slug = base_slug

            counter = 1

            while Blog.objects.filter(
                slug=slug
            ).exclude(
                pk=self.pk
            ).exists():

                slug = f"{base_slug}-{counter}"

                counter += 1

            self.slug = slug

        # Automatically set published date
        if self.status == "published" and not self.published_at:

            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    @property
    def read_time(self):

        import re

        word_count = len(
            re.findall(
                r"\w+",
                self.body or ""
            )
        )

        minutes = max(
            5,
            round(word_count / 200)
        )

        return f"{minutes} min read"


# =========================================================
# OFFERS
# =========================================================

class Offer(models.Model):

    CATEGORY_CHOICES = [
        ("Signature Safari", "Signature Safari"),
        ("Regenerative Adrenaline", "Regenerative Adrenaline"),
        ("Coastal Retreat", "Coastal Retreat"),
        ("Aerial Adventure", "Aerial Adventure"),
        ("Luxury Experience", "Luxury Experience"),
        ("Cultural Experience", "Cultural Experience"),
        ("Other", "Other"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=255
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    description = models.TextField(
        max_length=1000
    )

    price = models.CharField(
        max_length=100,
        help_text="Example: $18,500 or Enquire"
    )

    price_label = models.CharField(
        max_length=100,
        default="/ experience",
        help_text="Example: / experience or / custom experience"
    )
    image = models.ImageField(
        upload_to=upload_image_to,
        storage=MediaCloudinaryStorage(),
        help_text="Upload the image for this offer."
    )
   
    is_active = models.BooleanField(
        default=True,
        help_text="Only active offers appear on the website."
    )

    is_featured = models.BooleanField(
        default=False,
        help_text="Mark this offer as featured."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "display_order",
            "-created_at"
        ]

        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.title