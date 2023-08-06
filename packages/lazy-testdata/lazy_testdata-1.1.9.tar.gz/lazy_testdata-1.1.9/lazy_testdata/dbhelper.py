from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import records


def connet_db(conn_str):
    engine = create_engine(conn_str, encoding='utf-8')
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session


def only_query(conn, sql):
    db = records.Database(conn)
    rows = db.query(sql)  # or db.query_file('sqls/active-users.sql')
    return rows


def exec_sql(conn, sql):
    session = connet_db(conn)
    tmp_list = session.execute(sql)
    session.commit()
    return tmp_list
