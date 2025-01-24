from db import connect_to_db, setup_db


def load_data_to_db(data: list[dict]) -> None:
    """Load data to the database
    Calls `setup_db()` to ensure the database structure is in place, 
    then iterates through the data and inserts each row.
    """
    
    conn = connect_to_db()
    
    if not conn:
        print("Failed to connect to the database.")
        return
    
    setup_db(conn)
    
    try:
        with conn.cursor() as cursor:
            for row in data:
                cursor.execute(
                    """
                    INSERT INTO users (user_id, name, email, signup_date, domain) 
                    VALUES (%s, %s, %s, %s, %s)
                    """, 
                    (row["user_id"], row["name"], row["email"], row["signup_date"], row["domain"])
                )
        conn.commit()
    except Exception as e:
        print(f"Failed to load data to the database: {e}")
        return
    finally:
        conn.close()
        print("Data loaded to the database.")
