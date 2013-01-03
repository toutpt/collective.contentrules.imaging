Introduction
============

This addon let you configure a pre compute of images scales using a content rule.

Using gallery or slideshow addons can be a problem when you handle lots of photos.
To optimize the database Plone do not pre compute image's scales. But when it's
time to display of photo gallery with 30 thumbs the server has to compute them
at the same time. That's what this addon try to workaround.

How to use
==========

You have to create the content rule in the backoffice and then activate it
on the folder where you will have all your photos.