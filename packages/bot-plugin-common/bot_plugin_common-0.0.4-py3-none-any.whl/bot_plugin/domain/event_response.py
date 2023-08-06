import enum
from dataclasses import dataclass
from typing import Union


class CallbackQueryMethod(str, enum.Enum):
    CREATE = 'CREATE'
    SELECT = 'SELECT_ONE'
    SELECT_MULTIPLE = 'SELECT_MULTIPLE'
    EDIT = 'EDIT'
    DELETE = 'DELETE'


@dataclass
class CallbackQueryEvent:
    user_id: Union[str, int]
    method: CallbackQueryMethod


class MessageMethod(str, enum.Enum):
    pass


class MessageEvent:
    user_id: Union[str, int]
    text: str
