import psycopg2

class Base:
    def __init__(self, host='localhost'):
       self.info = f"host={host}' port='5432' user='vf' password='victoria' dbname='frame'"
       self.connection = None
       self.cursor = None

    def connect(self):
        if self.connection is None or self.cursor is None:
            self.connection = psycopg2.connect(self.info)
            self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def test_connection(self):
        try:
            if self.connection is None:
                self.connect()
            self.cursor.execute('SELECT 1;')
            result = self.cursor.fetchone()

            if result and result[0] == 1:
                print('Database connection is working')
                return True
            else:
                print('Database connection failed')
        except Exception as e:
            print(f'Databaser connection failed with error: {e}')


