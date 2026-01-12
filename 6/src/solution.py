from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    """
    Возвращает список всех фильмов с их режиссёрами.
    """
    query = (
        select(Movie)
        .join(Movie.director)  # Явный JOIN
        .options(joinedload(Movie.director))  # Жадная загрузка
        .order_by(Movie.title) # Сортировка
    )
    
    movies = session.scalars(query).unique().all()
    return movies
# END
