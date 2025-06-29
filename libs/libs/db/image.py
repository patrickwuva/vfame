def get_image_by_id(db, id):
    db.connect()
    sql = "SELECT * FROM images WHERE id = %s;"
    db.cursor.execute(sql, (id,))
    result = db.cursor.fetchone()
    if result:
        return result 
    else:
        print(f"No image found with ID {id}")
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
        id = db.cursor.fetchone()['id']
        db.connection.commit()
        return id
    except Exception as e:
        print(f'error on insert image: {e}')
        db.connection.rollback()
        return None


