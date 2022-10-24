import sys

TESTING = False


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


if 'test' in sys.argv:
    TESTING = True
    MIGRATION_MODULES = DisableMigrations()
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
