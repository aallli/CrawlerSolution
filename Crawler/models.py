from django.db import models
from django.utils.translation import ugettext_lazy as _


class Platform(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=200, unique=True, blank=False, null=False)
    active = models.BooleanField(verbose_name=_("Active"), default=True)

    class Meta:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    def __str__(self):
        return self.name


class Channel(models.Model):
    platform = models.ForeignKey(Platform, verbose_name=_('Platform'), on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(verbose_name=_("Channel Name"), max_length=200, unique=True, blank=False, null=False)
    active = models.BooleanField(verbose_name=_("Active"), default=True)

    class Meta:
        verbose_name = _('Channel')
        verbose_name_plural = _('Channels')

    def __str__(self):
        return '%s (%s)' % (self.name, self.platform)


class Config(models.Model):
    resource = models.ManyToManyField(Channel, verbose_name=_('Resource'))

    class Meta:
        verbose_name = _('Config')
        verbose_name_plural = _('Config')
