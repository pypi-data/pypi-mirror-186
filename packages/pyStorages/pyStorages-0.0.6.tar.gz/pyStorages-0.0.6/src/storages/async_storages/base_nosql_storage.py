import abc
from abc import abstractmethod
import copy


class BaseNoSQLStorage(abc.ABC):
    def __init__(self):
        self._data = {}

    @abstractmethod
    async def load(self):
        raise NotImplementedError

    @abstractmethod
    async def dump(self):
        raise NotImplementedError

    async def set_data(self, **kwargs):
        updated = False
        for key, value in kwargs.items():
            if key not in self._data.keys() or self._data[key] != value:
                self._data[key] = copy.deepcopy(value)
                updated = True
        if updated:
            await self.dump()

    async def delete_data(self, *keys):
        for key in keys:
            if key in self._data.keys():
                del self._data[key]
            else:
                raise KeyError(key)
        await self.dump()

    async def reset_data(self):
        self._data = {}
        await self.dump()

    async def get_data(self, *keys) -> tuple:
        if len(keys) == 0:
            return self._data,
        result = []
        for key in keys:
            if isinstance(key, list):
                sub_data = self._data
                for idx, subkey in enumerate(key):
                    if subkey in sub_data.keys():
                        sub_data = sub_data[subkey]
                    else:
                        raise KeyError("->".join(key[:idx + 1]))
                result.append(sub_data)
            elif key in self._data.keys():
                result.append(self._data[key])
            else:
                raise KeyError(key)
        return tuple(result)
