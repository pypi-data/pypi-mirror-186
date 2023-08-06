import time
from typing import Dict, Union

try:
    from sqlalchemy import Column, engine, cast, String, case, func, or_, select, text, PrimaryKeyConstraint
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import aliased, Session, sessionmaker
    from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, FLOAT, \
        JSON, VARCHAR
    from sqlalchemy.orm import Query
except ImportError:
    raise ImportError("sqlalchemy is required by zesty.zbs-api but needs to be vendored separately. Add postgres-utils to your project's requirements that depend on zbs-api.")

Base = declarative_base()


class InstancesTags(Base):
    __tablename__ = "instances_tags"

    instance_id = Column(VARCHAR, primary_key=True)
    account_id = Column(VARCHAR, index=True, default=None)
    account_uuid = Column(VARCHAR, index=True, default=None)
    instance_name = Column(VARCHAR, default=None)
    instance_tags = Column(JSON, default=None)

    __table_args__ = (
        PrimaryKeyConstraint('instance_id', name='instances_tags_pkey'),)

    def __init__(
            self,
            instance_id: str,
            account_id: str = None,
            account_uuid: str = None,
            instance_name: str = None,
            instance_tags: dict = None
            ):
        self.instance_id = instance_id,
        self.account_id = account_id
        self.account_uuid = account_uuid
        self.instance_name = instance_name
        self.instance_tags = instance_tags

    def __repr__(self) -> str:
        return f"{self.__tablename__}:{self.instance_id}"

    def asdict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_dict(self) -> dict:
        return self.asdict()


def create_tables(engine: engine.base.Engine) -> None:
    Base.metadata.create_all(engine, checkfirst=True)
