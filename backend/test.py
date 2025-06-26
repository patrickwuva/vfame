from libs.db import Base

if __name__ == '__main__':
    base = Base(host='192.168.1.58')
    #base.test_connection()
    #print(base.insert_image(filename='test.png',original_format='png'))
    image = base.get_image_by_path(path='test.png')
    print(image)
