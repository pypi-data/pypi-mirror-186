import pymysql


class Db():
    '''database access layer'''

    def __init__(self, dbsvr, dbuser, dbpswd, dbname):

        self.dbname = dbname
        self.dbsrvr = dbsvr
        self.dbuser = dbuser
        self.dbpswd = dbpswd

        self.cnn = self.connect()

    def __enter__(self):
        self.cnn = self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cnn.close()

    def connect(self):
        '''connects to mysql'''
        return pymysql.connect(host=self.dbsrvr,
                               user=self.dbuser,
                               password=self.dbpswd,
                               database=self.dbname)

    def close(self):
        '''closes the db connection'''
        self.cnn.close()

    def singlequery(self, qry, arglist=()):
        '''Performs a single query returns the number of rows affected'''

        csr = self.cnn.cursor()
        res = csr.execute(qry, arglist)
        self.cnn.commit()

        return res

    def namedselect(self, qry, arglist=()):
        '''Performs a single query returns the rows selected'''

        csr = self.cnn.cursor()
        csr.execute(qry, arglist)

        self.cnn.commit()

        for row in csr.fetchall():
            yield {d[0]: r for d, r in zip(csr.description, row)}

    def executemany(self, qry, arglist):
        '''Performs a single qry returns the number of rows affected'''

        csr = self.cnn.cursor()
        res = csr.executemany(qry, arglist)
        self.cnn.commit()

        return res

    def singleselect(self, qry, arglist=()):
        '''Performs a single query returns the rows selected'''

        csr = self.cnn.cursor()
        csr.execute(qry, arglist)

        self.cnn.commit()

        return csr.fetchall()

    def singlerow(self, qry, arglist=()):
        '''Performs a single query returns the first/only row selected'''

        csr = self.cnn.cursor()
        csr.execute(qry, arglist)

        self.cnn.commit()

        return csr.fetchall()[0]
