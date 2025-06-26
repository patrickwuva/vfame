from .base import Base

def get_image_by_id(db: Base, image_id: int):
    db.connect()

    sql = "SELECT * FROM images WHERE id = %s;"
    result = db.query(sql, (image_id,))
    if result:
        return result[0] 
    else:
        print(f"No image found with ID {image_id}")
        return None

def insert_image(db: Base, filename, original_format, gif_path=None):
    db.connect() 

    sql = """
        INSERT INTO images (filename, original_format, gif_path)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    try:
        db.execute(sql, (filename, original_format, gif_path))
        image_id = db.cursor.fetchone()['id']
        return image_id
    except Exception as e:
        db.connection.rollback()
        return None


