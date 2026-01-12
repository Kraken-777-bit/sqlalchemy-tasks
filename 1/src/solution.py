import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# BEGIN (write your solution here)
def create_db_engine(
    db_url: str | None = None,
    echo: bool = False,
    pool_size: int = 5,
    max_overflow: int = 10
):
    """
    Создаёт и возвращает движок базы данных PostgreSQL с использованием SQLAlchemy.

    Параметры:
    - db_url: строка подключения к БД. Если None, берётся из переменной окружения DATABASE_URL.
    - echo: логировать SQL-запросы (по умолчанию False).
    - pool_size: размер пула соединений (по умолчанию 5).
    - max_overflow: максимальное количество соединений сверх размера пула (по умолчанию 10).

    Возвращает:
    - Объект движка SQLAlchemy.
    """
    if db_url is None:
        db_url = os.environ.get('DATABASE_URL')
        if db_url is None:
            raise ValueError(
                "Не указан URL базы данных. "
                "Передайте его в параметре db_url или задайте переменную окружения DATABASE_URL."
            )

    engine = create_engine(
        db_url,
        echo=echo,
        pool_size=pool_size,
        max_overflow=max_overflow,
        future=True  # используем API версии 2.0
    )
    return engine
# END
