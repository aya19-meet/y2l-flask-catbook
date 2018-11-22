from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name,vote=0)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats
def vote(id):
	cat_object = session.query(Cat).filter_by(id=id).first()
	cat_object.vote += 1
	session.commit()


def get_cat(cat_id):
	cat = session.query(Cat).filter_by(id=cat_id).first()
	return cat