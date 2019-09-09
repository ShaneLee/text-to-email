from database_con import get_connection

def get_ids():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""SELECT id FROM emails;""")
    return cursor.fetchall()

def insert_id(id):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO emails (id) VALUES ('%s')""" % (id))
    db.commit()
    db.close()
