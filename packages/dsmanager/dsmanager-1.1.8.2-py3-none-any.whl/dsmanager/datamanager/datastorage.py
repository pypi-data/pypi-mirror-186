"""@Author: Rayane AMROUCHE

Datastorage Class.
"""

import json

from typing import Any

import pandas as pd  # type: ignore

import dsmanager

class DataStorage(dict):
    """A dictionary that can be accessed through attributes."""

    def __dir__(self):
        return sorted(set(dir(super()) + list(self.keys())))

    def __getattr__(self, __name: str) -> Any:
        return self[__name]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict_value):
        self.__dict__ = dict_value

    def _models_serialization(self, obj: Any):
        def _is_jsonable(obj_):
            try:
                json.dumps(obj_)
                return True
            except (TypeError, OverflowError):
                return False

        def _serialize(obj_):
            if isinstance(obj_, pd.core.frame.DataFrame):
                return {
                    "DataFrame": {
                        "Column": list(obj_.columns),
                        "Shape": f"{obj_.shape[0]} row(s) x {obj_.shape[1]} column(s)",
                    }
                }
            if isinstance(obj_, dsmanager.Model):
                return {"estimator": str(obj_.estimator), "params": obj_.params}
            try:
                res = obj_.__dict__
            except AttributeError as _:
                res = "Cannot be serialized"
            return res

        return obj if _is_jsonable(obj) else _serialize(obj)

    def __repr__(self) -> str:
        try:
            res = json.dumps(
                self,
                indent=4,
                default=self._models_serialization,
                sort_keys=True,
            )
        except TypeError as _:
            res = super().__repr__()
        return res
