from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL="mysql+pymysql://root:root@db:3306/2010_2019_FallMarathons"
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})


meta = MetaData()

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()