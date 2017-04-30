#!/usr/bin/pyhon2.7.9


class NotANumber(Exception):
    def __str__(self):
        return repr("Argument is not a number")


class NotAString(Exception):
    def __str__(self):
        return repr("Argument is not a string")
