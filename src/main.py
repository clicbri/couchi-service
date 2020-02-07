from src.repository.database.base import db

if __name__ == "__main__":
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
