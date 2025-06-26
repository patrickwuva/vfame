def get_video_by_id(db, id):
    db.connect()
    sql = "SELECT * FROM videos WHERE id = %s;"
    db.cursor.execute(sql, (id,))
    result = db.cursor.fetchone()
    if result:
        return result 
    else:
        print(f"No video found with ID {id}")
        return None
   
def get_video_by_path(db, path):
    db.connect()
    sql = "SELECT * FROM video WHERE filename = %s;"
    db.cursor.execute(sql, (path,))
    result = db.cursor.fetchone()
    if result:
        return result 
    else:
        print(f"No video found with path {path}")
        return None
    
def insert_video(db, filename, duration):
    db.connect() 
    sql = """
    INSERT INTO video (filename, duration)
    VALUES (%s, %s)
    RETURNING id;
    """
    try:
        db.cursor.execute(sql, (filename, duration))
        id = db.cursor.fetchone()['id']
        db.connection.commit()
        return id
    except Exception as e:
        print(f'error on insert video: {e}')
        db.connection.rollback()
        return None


