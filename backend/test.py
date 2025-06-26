from libs.db import Base
from libs.db import get_image_by_path

if __name__ == '__main__':
    base = Base(host='192.168.1.58')
    #base.test_connection()
    #print(base.insert_image(filename='test.png',original_format='png'))
    image = get_image_by_path(base, path='test.png')
    print(image)

