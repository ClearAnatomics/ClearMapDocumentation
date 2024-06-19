#-*- coding:utf-8 -*-
u'''
embedding youtube video to sphinx

usage:

First of all, add `sphinxcontrib.youtube` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['sphinxcontrib.youtube']


then use `youtube` directive.

You can specify video by video url or video id.

.. code-block:: rst

   .. youtube:: http://www.youtube.com/watch?v=Ql9sn3aLLlI

   .. youtube:: Ql9sn3aLLlI


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''


def do_nothing(self, node):
  pass;


def setup(app):

    from . import youtube

    app.add_node(youtube.youtube,
                 html=(youtube.visit, youtube.depart),
                 latex=(do_nothing, do_nothing))
    app.add_directive('youtube', youtube.YoutubeDirective)
