#import asyncpg
#import asyncio
import aiomysql
from fastapi import FastAPI
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from urllib.parse import quote_plus

from app.core.config import USERNAME, PASSWORD

#loop = asyncio.get_event_loop()


class DBSession :
    db = None
    readOnly_db = None

oDBSession = DBSession()

async def connect_to_db(app: FastAPI) -> None:
    db_session = await getDBConnection()
    app.state.db_session = db_session.get("writeDB")
    app.state.rdb_session = db_session.get("readOnlyDB")
    
    # app.state.pool = await aiomysql.create_pool(
    #                             host=str(MYSQL_HOST), port=int(MYSQL_PORT),
    #                             user=str(MYSQL_USER), password=str(MYSQL_PWD),
    #                             db=str(MYSQL_DB) , loop=None, autocommit=False)

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    app.state.db_session.close()
    # app.state.pool.close()

    logger.info("Connection closed")


async def getDBConnection():
    try:
        if DBSession.db:
            return oDBSession.db 
        
        # connection_string = 'postgresql://'+str(username)+":"+str(password)+'@host:5432/postgres'
        connection_string="postgresql://postgres.bfhhajmrfsutjzwvhiyp:"+str(PASSWORD)+"@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"
        logger.info("Connecting to {0}", connection_string)
        db = create_engine(
                            connection_string % quote_plus(str(MYSQL_PWD)),
                            echo=DEBUG,                        
                            pool_size=20, 
                            max_overflow=20
                        )
        
        session_factory = sessionmaker(bind=db, autoflush=False, expire_on_commit=True)
        ReadOnlySessionLocal = sessionmaker(bind=db, autocommit=False, autoflush=False)

        oDBSession.db = session_factory()
        oDBSession.readOnly_db = ReadOnlySessionLocal()
        
        return { "writeDB" : oDBSession.db, "readOnlyDB" : oDBSession.readOnly_db } 
    except BaseException as error:
        print(error)
