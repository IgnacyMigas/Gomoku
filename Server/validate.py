import abc
from exception import *


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate_name(self):
        pass

    @abc.abstractmethod
    def validate_number(self):
        pass


class Validator(AbstractValidator):
    def __init__(self, to_be_validated):
        self.to_be_validated = to_be_validated

    def validate_name(self):
        if not self._is_string():
            raise NotAString()

    def validate_number(self):
        if not self._is_number():
            raise NotANumber()

    def _is_string(self):
        return isinstance(self.to_be_validated, str)

    def _is_number(self):
        return isinstance(self.to_be_validated, (int, float))
