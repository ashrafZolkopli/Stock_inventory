from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User (AbstractUser):
    staff_id = models.CharField(
        _("Staff Id"),
        max_length=6,
        validators=[
            RegexValidator(
                '^[0-9]{6}&',
                _('Plese insert a valid staff id'),
            )
        ],
        unique=True
    )


class Department(models.Model):
    department_name = models.CharField(
        _("Department Name"),
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        _("Department Slug Name"),
        blank=True,
        default=""
    )

    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True,
    )

    def __str__(self):
        return self.department_name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.department_name)
        super(Department, self).save(*args, **kwargs)


def set_department_default():
    return Department.objects.get_or_create(
        department_name="Department not selected"
    )[0]


class Position(models.Model):
    position_name = models.CharField(
        _("Position Name"),
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        _("Position Slug Name"),
        blank=True,
        default=""
    )

    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True,
    )

    def __str__(self):
        return self.position_name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.position_name)
        super(Position, self).save(*args, **kwargs)


def set_position_default():
    return Position.objects.get_or_create(
        department_name="Position not selected"
    )[0]


class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User Account"),
        on_delete=models.PROTECT,
    )

    department = models.ForeignKey(
        Department,
        verbose_name=_("Staff Department"),
        on_delete=models.SET(set_department_default),
        related_name='userinfo_department',
        related_query_name='department_userinfo',
    )

    position = models.ForeignKey(
        Position,
        verbose_name=_("Staff Position"),
        on_delete=models.SET(set_position_default),
        related_name='userinfo_position',
        related_query_name='position_userinfo',
    )

    def __str__(self):
        return f'{self.user.staff_id} as \
            {self.position.position_name} at \
                {self.department.department_name}'
