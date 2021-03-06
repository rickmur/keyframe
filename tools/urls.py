from django.conf.urls import url

from tools import views

urlpatterns = [
                       url(r"^$", views.index,
                           name="index"),
                       url(r"^new/$", views.new_template,
                           name="new"),
                       url(r"^newTemplate/$", views.choose_action,
                           name="choose_action"),
                       url(r"^configureAction/$", views.configure_action,
                           name="configure_action"),
                       url(r"^defineTemplate/$", views.define_template,
                           name="define_template"),
                       url(r"^create/$", views.create,
                           name="create"),
                       url(r"^update/$", views.update,
                           name="update"),
                       url(r"^delete/(?P<template_id>\d+)/$", views.delete,
                           name="delete"),
                       url(r"^(?P<template_id>\d+)$", views.detail,
                           name="detail"),
                       url(r"^edit/(?P<template_id>\d+)/$", views.edit,
                           name="edit"),
                       url(r"^actionOptions/$", views.get_options_for_action,
                           name="get_options_for_action"),
                       url(r"^embedTemplate/$", views.get_template_input_parameters_overlay,
                           name="get_template_input_parameters"),
                       url(r"^search", views.search,
                           name="search"),
                       url(r"^execute_template", views.execute_template,
                           name="execute_template"),

                       ]
