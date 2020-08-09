# -*- coding:utf-8 -*-

import sys
import csv
from pathlib import Path
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

DBFILE = 'geolonia_addr_db.sqlite3'
DBNAME = 'sqlite:///' + DBFILE


Base = declarative_base()


class Address(Base):
    __tablename__ = 'geolonia'

    Id = Column(Integer, primary_key=True)
    PrefCode = Column(String(2))  # 都道府県コード
    PrefName = Column(String)     # 都道府県名
    PrefKana = Column(String)     # 都道府県名カナ
    PrefRomnan = Column(String)   # 都道府県名ローマ字
    CityCode = Column(String(5))  # 市町村コード
    CityName = Column(String)     # 市町村名
    CityKana = Column(String)     # 市町村名カナ
    CityRoman = Column(String)    # 市町村名ローマ字
    AreaCode = Column(String(12))  # 大字町丁目コード
    AreaName = Column(String)      # 大字町丁目名
    Longitude = Column(Float)       # 緯度
    Latitude = Column(Float)        # 経度

    def __init__(self, row):
        self.PrefCode = row[0]
        self.PrefName = row[1]
        self.PrefKana = row[2]
        self.PrefRomnan = row[3]
        self.CityCode = row[4]
        self.CityName = row[5]
        self.CityKana = row[6]
        self.CityRoman = row[7]
        self.AreaCode = row[8]
        self.AreaName = row[9]
        self.Longitude = float(row[10])
        self.Latitude = float(row[11])


class Geolonia(object):

    def __init__(self):
        self._engine = sqlalchemy.create_engine(DBNAME, echo=False)
        self._base = Base
        self._base.metadata.bind = self._engine
        self._base.metadata.create_all()
        self.session = sessionmaker(bind=self._engine)

    def find_long_lat(self, pref, city, area):
        ses = self.session()
        lng = 0.0
        lat = 0.0
        try:
            addr = ses.query(Address).filter_by(PrefName=pref,
                                                CityName=city,
                                                AreaName=area).one()
            lng = addr.Longitude
            lat = addr.Latitude

        except NoResultFound:
            pass

        return lng, lat


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python %s <geolonia_csv>' % (sys.argv[0]))
        exit()

    db_file = Path(DBFILE)
    if db_file.exists():
        db_file.unlink()

    filename = sys.argv[1]
    geo = Geolonia()
    with open(filename) as f:
        ses = geo.session()
        next(csv.reader(f))
        pref = ''
        for row in csv.reader(f):
            if pref != row[1]:
                pref = row[1]
                print(pref)
            ses.add(Address(row))
        ses.commit()

    print('done')
