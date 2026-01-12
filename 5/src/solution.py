from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
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
    Возвращает список всех фильмов с именами их режиссёров.
    """
    # Создаем запрос с JOIN между Movie и Director
    query = (
        select(Movie, Director.name)
        .join(Director, Movie.director_id == Director.id)
        .order_by(Movie.title)
    )
    
    # Выполняем запрос
    results = session.execute(query).all()
    
    # Форматируем результат
    formatted_movies = []
    for movie, director_name in results:
        movie_str = (
            f"{movie.title} by {director_name}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        formatted_movies.append(movie_str)
    
    return formatted_movies
# END
