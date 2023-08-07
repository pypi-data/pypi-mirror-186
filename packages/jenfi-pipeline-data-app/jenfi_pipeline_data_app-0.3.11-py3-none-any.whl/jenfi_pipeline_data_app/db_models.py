from sqlalchemy import ForeignKey, Table, MetaData, Column, JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.attributes import flag_modified

import datetime

from sqlalchemy import Table, Column, Integer, DateTime

# This shouldn't be a function, but I can't figure out how to pass a db_engine before the class creation on import.
# ATM, all classes will have to be loaded via function =\
#
# https://stackoverflow.com/questions/4215920/how-to-bind-engine-when-i-want-when-using-declarative-base-in-sqlalchemy
# The above is the same problem. It recommends using a DeferredRefelection, but that didn't work for me.
def state_machine_run_model(app):
    Base = declarative_base()
    metadata = MetaData(bind=app.db_engine)

    class StateMachineRun(Base):
        __table__ = Table(
            "pipeline_state_machine_runs",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("result", MutableDict.as_mutable(JSON)),
            Column('created_at', DateTime, default=datetime.datetime.now),
            Column('updated_at', DateTime, default=datetime.datetime.now),
            autoload=True,
        )

        def result_to_db(self, logical_step_name, state_machine_run_id, results):
            sm_run = (
                app.db.query(StateMachineRun)
                .populate_existing()
                .with_for_update(of=StateMachineRun, nowait=False)
                .get(state_machine_run_id)
            )
            sm_run.result[logical_step_name] = results

            return app.db.commit()

    return StateMachineRun

def state_machine_model(app):
    Base = declarative_base()
    metadata = MetaData(bind=app.db_engine)

    class StateMachine(Base):
        __table__ = Table(
            "pipeline_state_machines",
            metadata,
            Column("id", Integer, primary_key=True),
            Column('created_at', DateTime, default=datetime.datetime.now),
            Column('updated_at', DateTime, default=datetime.datetime.now),
            autoload=True,
        )

    return StateMachine
