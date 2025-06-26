def get_image_by_id(db, image_id):
    db.connect()

    sql = "SELECT * FROM images WHERE id = %s;"
    db.cursor.execute(sql, (image_id,))
    result = db.cursor.fetchone()
    if result:
        return result 
    else:
        print(f"No image found with ID {image_id}")
        return None
   
def get_image_by_path(db, path):
    db.connect()

    sql = "SELECT * FROM images WHERE filename = %s;"
    db.cursor.execute(sql, (path,))
    result = db.cursor.fetchone()
    if result:
        return result 
    else:
        print(f"No image found with path {path}")
        return None
    
def insert_image(db, filename, original_format, gif_path = None):
    db.connect() 

    sql = """
    INSERT INTO images (filename, original_format, gif_path)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    try:
        db.cursor.execute(sql, (filename, original_format, gif_path))
        image_id = db.cursor.fetchone()['id']
        db.connection.commit()
        return image_id
    except Exception as e:
        print(f'error on insert image: {e}')
        db.connection.rollback()
        return None


