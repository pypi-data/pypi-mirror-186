from typing import Any, Dict
import tabulize as tz
import pandas as pd

from pandalchemize.records import df_to_records

Record = Dict[str, Any]


class SqlTable:
    def __init__(self, name: str, engine) -> None:
        self.name = name
        self.engine = engine
        self._sqltable = tz.SqlTable(name, engine)
        
    def __repr__(self) -> str:
        return repr(self._sqltable)
        
    def pull(self) -> pd.DataFrame:
        self._sqltable.pull()
        return pd.DataFrame(self._sqltable.old_records)
    
    def push(self, df: pd.DataFrame) -> None:
        records = df_to_records(df)
        self._sqltable.push(records)
        
    def record_changes(self, df: pd.DataFrame) -> dict:
        records = df_to_records(df)
        return self._sqltable.record_changes(records)

    
def read_sqltable(name: str, engine) -> SqlTable:
    return SqlTable(name, engine)


def read_sqltable_dataframe(name: str,engine) -> tuple[SqlTable, pd.DataFrame]:
    sqltable = SqlTable(name, engine)
    df = sqltable.pull()
    return sqltable, df


def to_sql(df: pd.DataFrame, sqltable: SqlTable) -> None:
    sqltable.push(df)
