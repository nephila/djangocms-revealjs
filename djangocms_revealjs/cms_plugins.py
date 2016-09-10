# -*- coding: utf-8 -*-
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from .models import FragmentModel, SlideModel, SlideNote, SlideCode


class RevealChildPlugin(CMSPluginBase):
    module = _('Reveal.JS')
    admin_preview = False
    allow_children = False
    text_enabled = True
    parent_classes = ['RevealSlidePlugin']

    def render(self, context, instance, placeholder):
        context = super(RevealChildPlugin, self).render(context, instance, placeholder)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class RevealNotePlugin(RevealChildPlugin):
    name = _(u"Slide note")
    model = SlideNote
    render_template = "djangocms_revealjs/revealjs_note.html"

    def icon_src(self, foo):
        return static("img/slide_note.png")
plugin_pool.register_plugin(RevealNotePlugin)


class RevealCodePlugin(RevealChildPlugin):
    name = _(u"Slide code")
    model = SlideCode
    render_template = "djangocms_revealjs/revealjs_code.html"

    def icon_src(self, foo):
        return static("img/slide_code.png")
plugin_pool.register_plugin(RevealCodePlugin)


class RevealFragmentPlugin(TextPlugin):
    """
    Plugin to handle Reveal.JS fragments
    """
    name = _(u"Slide fragment")
    module = _('Reveal.JS')
    model = FragmentModel
    render_template = "djangocms_revealjs/revealjs_fragment.html"
    admin_preview = False
    allow_children = False
    text_enabled = True
    parent_classes = ['RevealSlidePlugin']
    fields = ['body', 'effects']

    def render(self, context, instance, placeholder):
        context = super(RevealFragmentPlugin, self).render(context, instance, placeholder)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def icon_src(self, foo):
        return static("img/fragment.png")
plugin_pool.register_plugin(RevealFragmentPlugin)


class RevealBlockFragmentPlugin(RevealFragmentPlugin):
    """
    Plugin to handle Reveal.JS fragments; rendered as display: block HTML element.
    """
    name = _(u"Slide block fragment")
    render_template = "djangocms_revealjs/revealjs_fragment_block.html"
plugin_pool.register_plugin(RevealBlockFragmentPlugin)


class RevealSlidePlugin(TextPlugin):
    """
    Plugin to insert Reveal.JS slide element.
    """
    name = _(u"Slide")
    module = _('Reveal.JS')
    model = SlideModel
    render_template = "djangocms_revealjs/revealjs.html"
    admin_preview = False
    allow_children = True
    text_enabled = False
    child_classes = ['RevealFragmentPlugin', 'RevealBlockFragmentPlugin', 'RevealCodePlugin', 'RevealNotePlugin']
    fieldsets = (
        (None, {'fields': ('title', 'sub_title', 'body')}),
        ('Options', {'fields': (('transition', 'transition_speed'), 'css_class'), 'classes': 'collapse'}),
        ('Background', {'fields': (('background_css', 'background_image'), 'background_transition_slide'), 'classes': 'collapse'})
    )

    def render(self, context, instance, placeholder):
        context = super(RevealSlidePlugin, self).render(context, instance, placeholder)
        request = context['request']
        context.update({
            'edit_mode': getattr(request, 'toolbar', None) and getattr(request.toolbar, 'edit_mode'),
        })
        return context
plugin_pool.register_plugin(RevealSlidePlugin)


class RevealSlidesContainer(CMSPluginBase):
    """
    Reveal.JS slide container.
    """
    name = _(u"Container")
    module = _('Reveal.JS')
    render_template = "djangocms_revealjs/revealjs_container.html"
    admin_preview = False
    allow_children = True
    child_classes = ['RevealSlidePlugin']

    def render(self, context, instance, placeholder):
        context = super(RevealSlidesContainer, self).render(context, instance, placeholder)
        request = context['request']
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'edit_mode': getattr(request, 'toolbar', None) and getattr(request.toolbar, 'edit_mode'),
        })
        return context
plugin_pool.register_plugin(RevealSlidesContainer)
