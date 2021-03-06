from django.conf.urls import url

from input_forms import views


urlpatterns = [
                       url(r"^$", views.index,
                           name="index"),
                       url(r"^create$", views.create,
                           name="create"),
                       url(r"^update", views.update,
                           name="update"),
                       url(r"^search", views.search,
                           name="search"),
                       url(r"^preview/(?P<input_form_id>[^/]+)/$", views.preview,
                           name="preview"),
                       url(r"^configureTemplate$", views.configure_template_for_endpoint,
                           name="configure_template_for_endpoint"),
                       url(r"^configureTemplateForQueue", views.configure_template_for_queue,
                           name="configure_template_for_queue"),
                       url(r"^apply$", views.apply_template,
                           name="apply_template"),
                       url(r"^applyToQueue", views.apply_template_to_queue,
                           name="apply_template_to_queue"),
                       url(r"^applyStandalone$", views.apply_standalone_template,
                           name="apply_standalone_template"),
                       url(r"^edit/(?P<input_form_id>[^/]+)/$", views.edit,
                           name="edit"),
                       url(r"^delete/(?P<input_form_id>[^/]+)/$", views.delete,
                           name="delete"),
                       url(r"^(?P<input_form_id>[^/]+)$", views.detail,
                           name="details"),
                       url(r"^new/(?P<template_id>[^/]+)$", views.new_from_template,
                           name="new_from_template"),
                       url(r"^view_from_template/(?P<template_id>[^/]+)/$", views.view_from_template,
                           name="view_from_template"),
                       url(r"^edit_from_template/(?P<template_id>[^/]+)/$", views.edit_from_template,
                           name="edit_from_template"),
                       ]
