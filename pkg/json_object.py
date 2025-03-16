import abc
from typing import Dict, Any, Union, List


class JSONObject(abc.ABC):
    @abc.abstractmethod
    def to_json(self) -> Dict[str, Any]:
        pass

    @classmethod
    @abc.abstractmethod
    def from_json(cls, json: Dict[str, Any]) -> 'JSONObject':
        pass

    def contains_term(self, term: str) -> bool:
        return _term_in_dict(term, self.to_json())


def _is_leaf(value: Any) -> bool:
    return not isinstance(value, (dict, list))

def _is_list(value: Any) -> bool:
    return isinstance(value, (list, tuple))

def _is_dict(value: Any) -> bool:
    return isinstance(value, dict)


def _term_in_leaf(term: str, leaf: Union[str, int, float, bool]) -> bool:
    # if term is a string, check if it is in the value
    if isinstance(leaf, str) and term in leaf:
        return True
    # if term is a number, check if it is equal to the value
    if isinstance(leaf, (int, float)) and term == str(leaf):
        return True
    # if term is a boolean, check if it is equal to the value
    if isinstance(leaf, bool) and term == str(leaf):
        return True

    return False

def _term_in_list(term: str, values: List[Any]) -> bool:
    for value in values:
        if _is_leaf(value):
            return _term_in_leaf(term, value)
        if _is_dict(value):
            return _term_in_dict(term, value)
        if _is_list(value):
            return _term_in_list(term, value)
        return False
    return False


def _term_in_dict(term: str, dictionary: Dict[str, Any]) -> bool:
    return _term_in_list(term, list(dictionary.values()))
