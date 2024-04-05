from database.connection import connect_to_db


def insert_movie_data(movie_data):

    conn = connect_to_db()
    cursor = conn.cursor()

    query = "INSERT INTO film (name, genre, year, rating, director) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, movie_data)

    conn.commit()
    cursor.close()
    conn.close()
