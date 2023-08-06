from typing import Dict, Union

from sqlalchemy.orm import Session, sessionmaker, Query
from sqlalchemy.sql.elements import or_

try:
    from sqlalchemy import Column, engine, case, func, cast, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.dialects.postgresql import BOOLEAN, FLOAT, INTEGER, BIGINT, \
        JSON, TIMESTAMP, VARCHAR
except ImportError:
    raise ImportError("sqlalchemy is required by zesty.zbs-api but needs to be vendored separately. Add postgres-utils to your project's requirements that depend on zbs-api.")

try:
    from zesty.models.InstancesTags import InstancesTags
except ImportError:
    from src.models.InstancesTags import InstancesTags

Base = declarative_base()


class EbsVolume(Base):
    # TODO: Move this model into our Alembic system
    # when a modification of this model is needed.
    __tablename__ = "disks"

    volume_id = Column(VARCHAR, primary_key=True)
    org_id = Column(VARCHAR, index=True)
    account_uuid = Column(VARCHAR, index=True)
    account_id = Column(VARCHAR, index=True)
    region = Column(VARCHAR, index=True)
    volume_type = Column(VARCHAR, index=True)
    cloud = Column(VARCHAR, index=True)
    availability_zone = Column(VARCHAR)
    create_time = Column(TIMESTAMP)
    encrypted = Column(BOOLEAN)
    size = Column(INTEGER)
    snapshot_id = Column(VARCHAR)
    state = Column(VARCHAR)
    iops = Column(INTEGER)
    tags = Column(JSON)
    attachments = Column(JSON)
    attached_to = Column(JSON)
    monthly_cost = Column(FLOAT, default=0)
    is_unused_resource = Column(INTEGER, default=0)
    unused_since = Column(VARCHAR)
    agent_installed = Column(BOOLEAN, default=False)
    _zbs_supported_os = Column(INTEGER)
    potential_savings = Column(FLOAT, default=0)

    def __init__(
            self,
            volume_aws_schema: Dict,
            account_uuid: str = None):
        if account_uuid:
            self.account_uuid = account_uuid
        else:
            self.account_uuid = volume_aws_schema["account_uuid"]

        self.volume_id = volume_aws_schema["volume_id"]
        self.org_id = volume_aws_schema["org_id"]
        self.account_id = volume_aws_schema["account_id"]
        self.cloud = volume_aws_schema["cloud"]
        self.region = volume_aws_schema["region"]
        self.volume_type = volume_aws_schema["volume_type"]
        self.availability_zone = volume_aws_schema["availability_zone"]
        self.create_time = volume_aws_schema["create_time"]
        self.encrypted = volume_aws_schema["encrypted"]
        self.size = volume_aws_schema["size"]
        self.snapshot_id = volume_aws_schema["snapshot_id"]
        self.state = volume_aws_schema["state"]
        self.iops = volume_aws_schema.get("iops", 0)
        self.tags = volume_aws_schema.get("tags", {})
        self.attachments = volume_aws_schema.get("attachments", [])
        self.attached_to = volume_aws_schema.get("attached_to", [])
        self.monthly_cost = volume_aws_schema.get("monthly_cost", 0)
        self.is_unused_resource = volume_aws_schema.get(
            "is_unused_resource", 0)
        self.unused_since = volume_aws_schema.get("unused_since", None)
        self.agent_installed = volume_aws_schema.get("agent_installed", False)
        self._zbs_supported_os = volume_aws_schema.get("_zbs_supported_os")
        self.potential_savings = volume_aws_schema.get("potential_savings", 0)

    def __repr__(self):
        return f"{self.__tablename__}:{self.volume_id}"

    @classmethod
    def instance_id_filter(cls, query: Query, value: str):
        query = query.filter(
            case((or_(cls.attached_to == None, func.json_array_length(cls.attached_to) == 0), False),
                 else_=func.jsonb(cls.attached_to).op('?')(value)))
        return query

    @classmethod
    def instance_name_filter(cls, query: Query, value: str):
        session = query.session
        subq = session.query(InstancesTags.instance_name)
        query = query.filter(
            cast(func.array(subq.scalar_subquery().where(func.jsonb(cls.attached_to).op('?')(InstancesTags.instance_id))), String)
            .regexp_replace(r'[\{\}"]', '', 'g') == value)
        return query

    @classmethod
    def instance_tags_filter(cls, query: Query, value: str):
        session = query.session
        subq = session.query(InstancesTags.instance_tags)

        python_types_to_pg = {int: BIGINT, float: FLOAT, bool: BOOLEAN}
        for key_val in value:
            key = key_val.get('key')
            val = key_val.get('value')
            if key is not None and val is not None:
                if not isinstance(val, str):
                    query = query.filter(cast(cast(func.jsonb(subq.scalar_subquery().where(
                        func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id)).op('->')(key), String), python_types_to_pg[type(val)]) == val)
                else:
                    val = f'"{val}"'
                    query = query.filter(cast(func.jsonb(subq.scalar_subquery().where(
                        func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id)).op('->')(key), String) == val)
            elif key is not None:
                query = query.filter(func.jsonb(subq.scalar_subquery().where(
                        func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id)).op('?')(key))
            elif val is not None:
                if isinstance(val, str) or isinstance(val, bool):
                    val = f'"{val}"'
                query = query.filter(cast(subq.scalar_subquery().where(
                        func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id), String)
                                     .regexp_replace(r'.+\: (' + str(val) + r')[,\s}].*', "\\1") == f"{val}")
        return query

    # Custom query
    @classmethod
    def custom_query(cls, session: Union[Session, sessionmaker]) -> Query:
        q = session.query(cls)
        subq = session.query(InstancesTags.instance_name)
        subq_2 = session.query(func.json_object_keys(InstancesTags.instance_tags))
        subq_3 = session.query(InstancesTags.instance_tags)

        q = q.add_columns(case((or_(cls.attached_to == None, func.json_array_length(cls.attached_to) == 0), ''),
                               else_=cast(cls.attached_to, String).regexp_replace(r'[\[\]"]', '', 'g'))
                          .label("instance_id"),
                          cast(func.array(subq.scalar_subquery().where(func.jsonb(cls.attached_to).op('?')(InstancesTags.instance_id))), String).regexp_replace(r'[\{\}"]', '', 'g')
                          .label("instance_name"),
                          func.array(subq_2.scalar_subquery().where(func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id))
                          .label('instance_tags_keys'),
                          subq_3.scalar_subquery().where(func.jsonb(cls.attached_to).op('->>')(0) == InstancesTags.instance_id)
                          .label('instance_tags')
                          )

        return q

    def get_volume_id(self):
        return self.volume_id

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def create_tables(engine: engine.base.Engine) -> None:  #type: ignore
    Base.metadata.create_all(engine, checkfirst=True)
