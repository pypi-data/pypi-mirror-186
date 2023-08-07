from abc import abstractmethod
from typing import Generic, Optional, Protocol, TypeVar


T = TypeVar("T")

class DescriptorProtocol(Protocol, Generic[T]):
    def __get__(self, obj: Optional[object], cls: type[object]) -> T:
        ...
    
    def __set__(self, obj: Optional[object], value: T) -> None:
        ...
    
    def __delete__(self, obj: Optional[object]) -> None:
        ...

    @property
    def name(self) -> str:
        ...


class Descriptor(Generic[T], DescriptorProtocol[T]):
    def __set_name__(self, owner: type, name: str):
        self._name = name

    @abstractmethod
    def _object_get(self, obj: object) -> T:
        raise NotImplementedError

    @abstractmethod
    def _class_get(self, cls: type[object]) -> T:
        raise NotImplementedError

    @abstractmethod
    def _set(self, obj: object, value: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def _delete(self, obj: object) -> None:
        raise NotImplementedError

    def __get__(self, obj: Optional[object], cls: type[object]) -> T:
        if obj == None:
            try:
                return self._class_get(cls)
            except AttributeError:
                raise AttributeError(f"'{cls.__name__}' object has no attribute '{self._name}'") from None
        else:
            try:
                return self._object_get(obj)
            except AttributeError:
                raise AttributeError(f"type object '{cls.__name__}' has no attribute '{self._name}'") from None

    def __set__(self, obj: object, value: T):
        self._set(obj, value)

    def __delete__(self, obj: object):
        try:
            self._delete(obj)
        except AttributeError:
            raise AttributeError(self._name)

    @property
    def name(self):
        return self._name


class Value(Generic[T], Descriptor[T]):
    def __init__(self) -> None:
        super().__init__()

    def __set_name__(self, owner: type, name: str):
        super().__set_name__(owner, name)
        self._value_attribute_name = "_Value__" + name

    
    def _object_get(self, obj: object) -> T:
        return getattr(obj, self._value_attribute_name)

    def _class_get(self, cls: type[object]) -> T:
        return getattr(cls, self._value_attribute_name)

    def _set(self, obj: object, value: T) -> None:
        setattr(obj, self._value_attribute_name, value)

    def _delete(self, obj: object) -> None:
        delattr(obj, self._value_attribute_name)

class Restrict(Generic[T], Descriptor[T]):
    def __init__(self, property: DescriptorProtocol[T], get: bool = True, set: bool = False, delete: bool = False, class_get: bool = False):
        self._property = property
        self._get_allowed = get
        self._set_allowed = set
        self._delete_allowed = delete
        self._class_get_allowed = class_get

    def _object_get(self, obj: object) -> T:
        if not self._get_allowed:
            raise AttributeError(f"unreadable attribute '{self._property.name}'")
        return self._property.__get__(obj, type(obj))

    def _set(self, obj: Optional[object], value: T) -> None:
        if not self._set_allowed:
            raise AttributeError(f"can't set attribute '{self._property.name}'")
        self._property.__set__(obj, value)

    def _delete(self, obj: Optional[object]) -> None:
        if not self._delete_allowed:
            raise AttributeError(f"can't delete attribute '{self._property.name}'")
        self._property.__delete__(obj)

    def _class_get(self, cls: type[object]) -> T:
        if not self._class_get_allowed:
            raise AttributeError(f"unreadable attribute '{self._property.name}'")
        return self._property.__get__(None, cls)