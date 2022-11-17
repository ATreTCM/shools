from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("postgresql+psycopg2://atretik:fkbcf2018@localhost/SchoolBD", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from schools.models import Hall, User, Lesson

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


    zp_couch = User(name="Ivanovich")
    db_session.add(zp_couch)
    kr_couch = User(name="Petrovich")
    db_session.add(kr_couch)
    free_couch = User(name="Alex")
    db_session.add(free_couch)

    zp_hall = Hall(city="Zaporizhzhya", street="Sobornuy")
    db_session.add(zp_hall) 
    kr_hall = Hall(city="Krivuy Rig", street="Osvobozhdenie")
    db_session.add(kr_hall)

    zp_lesson = Lesson(hall=zp_hall, coach=zp_couch)
    db_session.add(zp_lesson)
    kr_lesson = Lesson(hall=kr_hall, coach=kr_couch)
    db_session.add(kr_lesson)
    zp_lesson = Lesson(hall=zp_hall, coach=free_couch)
    db_session.add(zp_lesson)
    db_session.commit()
    print("DataBase complate")
    
if __name__ == "__main__":
    init_db()