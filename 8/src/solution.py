from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Movie
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, future=True)
session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session = session_maker()


# BEGIN (write your solution here)
async def get_all_movies(session):
    """
    Получает все фильмы с режиссёрами из базы данных асинхронно.
    """
    # Подход с прямым JOIN и загрузкой
    from sqlalchemy.orm import contains_eager
    
    # Создаем запрос с JOIN и явной загрузкой
    movie_query = (
        select(Movie)
        .join(Movie.director)
        .options(contains_eager(Movie.director))
        .order_by(Movie.title)
    )
    
    # Асинхронное выполнение
    exec_result = await session.execute(movie_query)
    all_films = exec_result.unique().scalars().all()
    
    # Форматируем результат
    result_list = []
    for film in all_films:
        formatted_film = (
            f"{film.title} by {film.director.name}, "
            f"released on {film.release_date}, "
            f"duration: {film.duration} min, "
            f"genre: {film.genre}, "
            f"rating: {film.rating}"
        )
        result_list.append(formatted_film)
    
    return result_list
# END
