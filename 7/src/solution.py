from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def delete_director(session, director_id):
    """
    Удаляет режиссёра и все связанные с ним фильмы.
    """
    # Получаем режиссёра по ID
    director = session.get(Director, director_id)
    
    if director is None:
        # Режиссёр не найден
        return
    
    # Удаляем режиссёра (связанные фильмы удалятся каскадно)
    session.delete(director)
    session.commit()
# END
