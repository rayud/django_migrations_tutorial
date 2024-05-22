class AppRouter:
    """
    A router to control all database operations on models in the
    app1 and app2 applications.
    """
    

    def db_for_read(self, model, **hints):
        """
        Attempts to read app1 and app2 models go to their respective databases.
        """
        if model._meta.app_label == 'migrations_app':
            return 'default'
        elif model._meta.app_label == 'migrations_app2':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app1 and app2 models go to their respective databases.
        """
        if model._meta.app_label == 'migrations_app':
            return 'default'
        elif model._meta.app_label == '':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in app1 or app2 is involved.
        """
        if obj1._meta.app_label in ('migrations_app', 'migratons_app2') and obj2._meta.app_label in ('migrations_app', 'migrations_app'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app1 and app2 apps only appear in their respective databases.
        """
        if app_label == 'migrations_app':
            return db == 'default'
        elif app_label == 'migrations_app2':
            return db == 'secondary'
        return None
