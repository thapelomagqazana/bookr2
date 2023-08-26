from django.contrib.admin.apps import AdminConfig


class ReviewAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'
