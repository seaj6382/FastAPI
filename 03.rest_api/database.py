from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 동기용 데이터 베이스 접속 명령어 (pymysql)
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:tkfkd6303@localhost/oz-fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 접속 명령어 (aiomysql)
# - 무거운 I/O요청(5초)이 먼저 와도, 뒤에 가벼운 I/O(1초) 작업 요청이 들어오면 더 빨리 끝나는 녀석이 응답된다.
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
ASYNC_SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://root:oz-password@localhost/oz-fastapi'
engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
