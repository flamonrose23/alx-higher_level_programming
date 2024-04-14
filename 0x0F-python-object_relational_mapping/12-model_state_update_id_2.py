#!/usr/bin/python3

"""
Writing script changing name of State object
from database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_eng = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_eng)
    Session = sessionmaker(bind=engine)

    session = Session()

    nw_state = session.query(State).filter(State.id == '2').first()
    nw_state.name = 'New Mexico'
    session.commit()
    session.close()
