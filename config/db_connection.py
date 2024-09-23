from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost:3306/2010_2019_FallMarathons", echo=True)

meta = MetaData()

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()