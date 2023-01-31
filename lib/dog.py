from sqlalchemy import create_engine

from models import Dog

import ipdb

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    pass
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    pass
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    pass
    # ipdb.set_trace()
    query = session.query(Dog).filter_by(id=row.id).first()
    return query

def get_all(session):
    pass
    query = session.query(Dog).all()
    return query

def find_by_name(session, name):
    pass
    query = session.query(Dog).filter_by(name=name).first()
    return query

def find_by_id(session, id):
    pass
    query = session.query(Dog).filter_by(id=id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    pass
    query = session.query(Dog).filter_by(name=name, breed=breed).first()
    # ipdb.set_trace()
    return query


def update_breed(session, dog, breed):
    pass
    # ipdb.set_trace()
    query = session.query(Dog).filter_by(id = dog.id).first()
    query.breed = breed
    session.commit()
    return session
    