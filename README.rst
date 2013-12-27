==================
djangocms-revealjs
==================

.. image:: https://badge.fury.io/py/djangocms-revealjs.png
    :target: https://badge.fury.io/py/djangocms-revealjs

.. image:: http://img.shields.io/pypi/dm/djangocms-page-tags.png
        :target: https://pypi.python.org/pypi/djangocms-page-meta


django CMS plugin to create reveal.js presentations

**Still Experimental and largely undocumented**


Quickstart
----------

Install djangocms-revealjs::

    pip install djangocms-revealjs

Then add it to INSTALLED_APPS along with its dependencies::

    'filer',
    'djangocms_revealjs',

Download and install `reveal.js`_ in your django CMS project.

Features
--------

Provides four django CMS plugins to edit Reveal.JS presentations:

Slide (RevealSlidePlugin)
+++++++++++++++++++++++++

This is the plugin to insert normal slides.

It supports settings transitions, background color and images, markdown syntax.

Container (RevealSlidesContainer)
+++++++++++++++++++++++++++++++++

Containers allow to nest slides in a vertical way.

Only slides can be put in a container; only one-level of container is supported.

Slide fragment (RevealFragmentPlugin)
+++++++++++++++++++++++++++++++++++++

Fragments allow to display part of a slide progressively. This plugin handles
inline fragments (i.e.: like `span` elements).

Block slide fragment (RevealBlockFragmentPlugin)
++++++++++++++++++++++++++++++++++++++++++++++++

This plugin is equal to the above, but renders block fragments
(i.e.: like `div` elements).

Dependencies
------------

* `django-filer`_ >= 0.9.5

.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _reveal.js: http://lab.hakim.se/reveal-js/