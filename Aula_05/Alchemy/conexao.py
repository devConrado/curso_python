#!/usr/bin/python3

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, DateTime)
from datetime import datetime

engine = create_engine('sqlite:///teste.db', echo=False)
metadata = MetaData(bind=engine)
user_table = Table('usuarios',metadata,
				   Column('id',Integer,primary_key=True),
				   Column('nome',String(40),index=True),
				   Column('idade',Integer,nullable=False),
				   Column('senha',String),
				   Column('data_criacao',DateTime, default=datetime.now),
				   Column('data_atualizacao',DateTime, default=datetime.now,onupdate=datetime.now))
metadata.create_all(engine)