import psycopg2
from psycopg2.extras import RealDictCursor
from . import image

class Base:
    def __init__(self, host='localhost'):
       self.info = f"host='{host}' port='5432' user='vf' password='victoria' dbname='frame'"
       self.connection = None
       self.cursor = None

    def connect(self):
        if self.connection is None or self.cursor is None:
            self.connection = psycopg2.connect(self.info)
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_image_by_id(self, image_id):
        return image.get_image_by_id(self, image_id)

    def get_image_by_path(self, path):
        return image.get_image_by_path(self, path)    


    def insert_image(self, filename, original_format, gif_path = None):
        return image.insert_image(self, filename, original_format, gif_path)

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


