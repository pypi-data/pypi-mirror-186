"""
This file is part of the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""

import re
from pdmn.glossary import Glossary, Predicate
from pdmn.problogname import problog_name
from typing import Dict


class VariableInterpreter:
    """
    TODO
    """
    def __init__(self, glossary: Glossary):
        """
        Initialises the VariableInterpreter.

        :arg glossary: a glossary object.
        :returns Object:
        """
        self.glossary = glossary

    def interpret_value(self,
                        value: str,
                        variables: Dict = {},
                        expected_type=None):
        """
        Method to interpret a value of a pDMN notation.
        Here be dragons.

        :arg value: string which needs to be interpreted.
        :arg variables: list containing the variables.
        :arg expected_type:
        :returns str: the interpretation of the notation.
        """
        # TODO: instead of string variables, make Variable class with existing
        # type to which can be referred.
        lu = self.glossary.lookup(str(value))
        interpretations = []

        # Length of lookup is zero if it is a variable, and not a relation or
        # function.
        if len(lu) == 0:
            if str(value) == '__PLACEHOLDER__':
                pass
            elif not expected_type:
                expected_type = variables[str(value)]
            return Value(value, expected_type, variables)
        for l in lu:
            if (expected_type is not None and expected_type !=
                    l[0].is_function()):
                pass  # TODO: fix this!
            try:
                interpretations.append(
                        PredicateInterpretation(l[0], l[1], self, variables))
            except ValueError:
                continue
        if len(interpretations) == 0:
            raise ValueError(f'The value of "{value}" could not be'
                             f' interpreted.')
        if len(interpretations) == 1:
            return interpretations[0]
        if len(interpretations) > 1:
            print(f"Warning: Multiple possible interpretations for {value}."
                  f" Selecting the last one found.")
            return interpretations[-1]


class Value:
    """
    An object to represent a value.
    """
    def __init__(self, value: str, valuetype, variables):
        """
        Initialised a Value object.

        :arg value: a string containing the value.
        :arg valuetype:
        :arg variables:
        :returns Object:
        """
        self.value = value
        self.type = valuetype
        self.check(variables)

    def check(self, variables):
        """
        TODO
        """
        if re.match('.* (and|of) .*', str(self.value)):
            raise ValueError(f'The compiler does not know how to interpret'
                             f' the following: "{self.value}".')
        return
        # TODO: reinclude below code.
        if self.value not in variables.keys() and \
                self.value not in self.type.possible_values:
            raise ValueError(f'WARNING: {self.value} occurs in a position'
                             f' of type {self.type.name}'
                             f' but does not appear in possible values')

    def __str__(self) -> str:
        """
        Magic method to format a variable interpretation to string.

        :returns str:
        """
        return f'{problog_name(self.value)}'


class PredicateInterpretation:
    """
    TODO
    """
    def __init__(self, pred: Predicate,
                 arguments,
                 inter: VariableInterpreter,
                 variables):
        """
        Initialises the PredicateInterpretation object.

        :arg pred: the predicate to interpret.
        :arg arguments:
        :arg inter: the variable interpreter.
        :arg variables:
        :returns Object:
        """
        self.pred = pred
        self.args = [inter.interpret_value(arg, variables=variables,
                                           expected_type=t) for arg, t in
                     zip(arguments, pred.args)]
        # if

    @property
    def type(self):
        """
        Method to get the type of the predicate.

        :returns Type: supertrype of the predicate.
        """
        return self.pred.super_type

    @property
    def value(self):
        """
        TODO
        """
        return self.pred.name

    def __str__(self):
        """
        Magic method to return this object in string form.
        """
        if self.args:
            return '{}({})'.format(problog_name(self.pred.name),
                                   ', '.join([arg.__str__() for arg in self.args]))
        else:
            return f'{problog_name(self.pred.name)}'
