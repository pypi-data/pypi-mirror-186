from typing import Union, Optional, Callable, Dict, Any
from cx_Oracle import (
    DbType,
    DB_TYPE_CHAR
)

ora_params = Union[dict, list]


class OraCustomType(object):

    def __init__(
        self,
        ora_type: Union[type, DbType],
        size: Optional[int] = None,
        array_size: Optional[int] = None,
        in_converter: Optional[Callable] = None,
        out_converter: Optional[Callable] = None,
        type_name: Optional[str] = None,
        encoding_errors: Optional[str] = None,
    ):
        self.ora_type = ora_type
        self.size = size
        self.array_size = array_size
        self.in_converter = in_converter
        self.out_converter = out_converter
        self.type_name = type_name
        self.encoding_errors = encoding_errors

    def get_as_cursor_var_kwargs(self) -> Dict[str, Any]:
        cursor_var_kwargs: Dict[str, Any] = {}

        if self.size is not None:
            cursor_var_kwargs["size"] = self.size

        if self.array_size is not None:
            cursor_var_kwargs["arraysize"] = self.array_size

        if self.in_converter is not None:
            cursor_var_kwargs["inconverter"] = self.in_converter

        if self.out_converter is not None:
            cursor_var_kwargs["outconverter"] = self.out_converter

        if self.type_name is not None:
            cursor_var_kwargs["typename"] = self.type_name

        if self.encoding_errors is not None:
            cursor_var_kwargs["encodingErrors"] = self.encoding_errors

        return cursor_var_kwargs


class OraCustomChar(OraCustomType):

    def __init__(
        self,
        size: Optional[int] = None,
        array_size: Optional[int] = None,
        in_converter: Optional[Callable] = None,
        out_converter: Optional[Callable] = None,
        type_name: Optional[str] = None,
        encoding_errors: Optional[str] = None,
    ):
        super(OraCustomChar, self).__init__(
            DB_TYPE_CHAR,
            size=size,
            array_size=array_size,
            in_converter=in_converter,
            out_converter=out_converter,
            type_name=type_name,
            encoding_errors=encoding_errors,
        )
