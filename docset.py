import sqlite3

class DocSet(object):

    def __init__(self, name):

        self.name = name
        self.init_db()

    @property
    def path(self):

        return '{name}.docset'.format(name = self.name)

    def init_db(self):

        path = '{path}/Contents/Resources/docSet.dsidx'.format(path = self.path)

        database = sqlite3.connect(path)

        cursor = db.cursor()

        try: cursor.execute('DROP TABLE searchIndex;')
        except: pass

        cursor.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
        cursor.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

        database.commit()
        database.close()
