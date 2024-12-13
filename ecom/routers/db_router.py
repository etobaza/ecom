import random


class MasterSlaveRouter:
    READ_DATABASES = ['wingman', 'wingman2']

    def db_for_read(self, model, **hints):
        return random.choice(self.READ_DATABASES)

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
