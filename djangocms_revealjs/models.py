# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from djangocms_text_ckeditor.models import AbstractText
from filer.fields.image import FilerImageField


FRAGMENT_CHOICES = {
    'grow': 'grow',
    'shrink': 'shrink',
    'roll-in': 'roll-in',
    'fade-out': 'fade-out',
    'highlight-red': 'highlight-red',
    'highlight-blue': 'highlight-blue',
    'current-visible': 'current-visible',
    'highlight-current-blue': 'highlight-current-blue',
}
TRANSITIONS = {
    'cube': 'Cube',
    'page': 'Page',
    'concave': 'Concave',
    'zoom': 'Zoom',
    'linea': 'Linear',
    'fade': 'Fade',
    'none': 'None',
    'default': 'Default'
}
TRANSITIONS_SPEED = {
    'default': 'Default',
    'fast': 'Fast',
    'slow': 'Slow'
}


class FragmentModel(AbstractText):
    """
    Fragment plugin model
    """
    effects = models.CharField(max_length=20, choices=FRAGMENT_CHOICES.items(), default='', blank=True)

    class Meta:
        verbose_name = _('fragment')
        verbose_name_plural = _('fragments')


class SlideModel(AbstractText):
    """
    Main slide plugin model
    """
    title = models.CharField(verbose_name=_(u'Title'), max_length=100,
                             default='', blank=True)
    sub_title = models.CharField(_(u'Section title'), max_length=100,
                                 default='', blank=True)
    transition = models.CharField(verbose_name=_('Transition'), max_length=20,
                                  choices=TRANSITIONS.items(), default='',
                                  blank=True)
    transition_speed = models.CharField(verbose_name=_(u'Transition speed'),
                                        max_length=20, default='', blank=True,
                                        choices=TRANSITIONS_SPEED.items())
    css_class = models.CharField(verbose_name=_(u'Custom CSS class'),
                                 max_length=100, default='', blank=True)
    background_css = models.CharField(verbose_name=_(u'Background CSS class'),
                                      max_length=100, default='', blank=True)
    background_image = FilerImageField(verbose_name=_(u'Background image'),
                                       null=True, blank=True)
    background_transition_slide = models.BooleanField(
        verbose_name=_(u'Background transition'), default=False)

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = _('slides')

    def __unicode__(self):
        if self.title:
            if self.sub_title:
                return '%s - %s' % (self.sub_title, self.title)
            return self.title
        elif self.sub_title:
            return self.sub_title
        return Truncator(strip_tags(self.body)).words(3, truncate="...")


class SlideNote(CMSPlugin):
    """
    Slide notes
    """
    note = models.TextField(verbose_name=_(u'Notes'), default='',
                            blank=True)
    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')

    def __unicode__(self):
        return Truncator(strip_tags(self.note)).words(3, truncate="...")


class SlideCode(CMSPlugin):
    """
    Slide codes
    """
    code = models.TextField(verbose_name=_(u'Code'), default='',
                            blank=True)
    class Meta:
        verbose_name = _('code')
        verbose_name_plural = _('codes')

    def __unicode__(self):
        return Truncator(strip_tags(self.code)).words(3, truncate="...")
