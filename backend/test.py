from libs.db import Base

if __name__ == '__main__':
    base = Base(host='192.168.1.58')
    base.test_connection()

