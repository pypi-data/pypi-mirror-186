"""
This file is part of the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""

import re
from typing import List
from pdmn.problogname import problog_name

"""
The glossary object contains the entire pDMN glossary.
It interprets each line, and creates a Type or Predicate/Function object.
"""


class Glossary:
    """
    The Glossary object contains all types, functions and predicates.
    During initialisation, it reads and interprets all the types, functions,
    constants, relations and booleans it can find and it reports any errors.
    Once the Glossary is created and initialized without errors, it's
    possible to print out the predicates in their ProbLog version.
    """
    def __init__(self, glossary_dict: dict):
        """
        Initialise the glossary.
        Create 4 default types, create an empty list of predicates, and
        interpret all 3 different glossaries.

        :arg dict: glossary_dict, the dictionary containing for each glossary
            type their tables.
        """
        self.types = [Type('String', None),
                      Type('Int', None),
                      Type('Float', None),
                      Type('Real', None)]
        self.predicates: List[Predicate] = []
        self.__read_types(glossary_dict["Type"], 0, 1, 2)
        self.__read_predicates(glossary_dict["Function"], "Function")
        self.__read_predicates(glossary_dict["Predicate"], "Predicate")

    def __str__(self):
        """
        Magic method to convert the Glossary to string.
        Prints out all the types, predicates and functions it contains.
        """
        retstr = "Glossary containing:\n"
        for typ in self.types:
            retstr += f"\t{str(typ)}\n"
        for pred in self.predicates:
            retstr += f"\t{str(pred)}\n"
        return retstr

    def contains(self, typestr):
        """
        Checks whether or not a type was already added to the glossary.

        :returns bool: True if the type has been added already.
        """
        for typ in self.types:
            if typestr == typ.name:
                return True
        return False

    def find_type(self, t):
        """
        Looks for types in the glossary.

        :returns List<Type>: the types found.
        """
        types = []
        for typ in self.types:
            if typ.match(t):
                types.append(typ)
        return next(filter(lambda x: x.match(t), self.types))

    def __read_types(self, array, ix_name=0, ix_type=1, ix_posvals=2):
        """
        Read and interpret all the types listed in the Type glossary.
        When it finds the keyword, it tries to interpret the other columns on
        that row.

        :arg np.array: the numpy array containing the Type glossary.
        :arg int: ix_name, the index for the name column.
        :arg int: ix_type, the index for the type column.
        :arg int: ix_posvals, the type for the posvals column.
        :returns None:
        """
        error_message = ""
        rows, cols = array.shape
        # Skip the first 2 rows, as these are headers.
        for row in array[2:]:
            # Loop over all the rows.
            name = row[ix_name]
            name = name.strip()

            # Get, and try to decypher the type.
            # If we're not able to find the type, raise error.
            typ = row[ix_type]
            try:
                typ = self.find_type(typ)
            except StopIteration:
                error_message = (f"DataType \"{typ}\" should be either a"
                                 f" (String, Int, Float) or a"
                                 f" user-defined type")
                raise ValueError(error_message)

            # Check for possible values.
            posvals = row[ix_posvals]
            try:
                # Match for the int range type, for instance [1, 10].
                int_reg = r'(\[|\()(-?\d+)\s*(?:\.\.|,)\s*(-?\d+)\s*(\]|\))'
                match = re.match(int_reg, posvals)

            except Exception:  # TODO: find errortype to except and fix except.
                match = None

            # Interpret range of int, if a match was found.
            if match:
                match = list(match.groups())
                if match[0] == '(':
                    match[1] += 1
                if match[-1] == ')':
                    match[2] -= 1
                posvals = '..'.join(match[1:-1])
            elif posvals is not None:
                posvals = ', '.join([problog_name(x) for x in
                                    re.split(r'\s*,\s*', posvals)])

            # Create the type and append it to the list.
            self.types.append(Type(name, typ, posvals))

    def __read_predicates(self, array, glosname, ix_name=0,
                          ix_type=1, zero_arity=False):
        """
        Method to read and interpret predicates.
        Loops over an array containing only predicates or functions,
        and filters them into subcategories.

        The possible entries are: Predicate, Function, partial Function,
            boolean, and relation..

        :arg array: a glossary table
        :arg glosname: the name of the glossary, i.e. Function, Predicate,
            Constant or Boolean
        :arg ix_name: the column index of the name column. By default this is
            always the first column.
        :arg ix_type: the column index of the type column. By default this is
            always the second column.
        :arg zero_arity: bool which should be True when the predicate is a
            0-arity predicate (constants and booleans).

        :returns None:
        """
        # It's possible that there's no glossary defined.
        if array is None:
            return

        for row in array[2:]:
            full_name = row[ix_name].strip()
            partial = False
            typ = None
            predicate = None

            # Check if it's a (partial) function/constant or a
            # relation/boolean.
            if re.match('(partial )?Function|Constant', glosname):
                predicate = False
                typ = row[ix_type]
                if typ:
                    typ = typ.strip()

                # Check if it's a partial function
                partial = bool(re.match('(?i)partial', full_name))
                full_name = full_name.replace('partial ', '')
                try:
                    typ = self.find_type(typ)
                except TypeError:
                    raise ValueError(f'DataType of Function "{full_name}" is'
                                     f' empty')
                except StopIteration:
                    raise ValueError(f'DataType "{typ}" of "{full_name}" is'
                                     f' not an existing Type')

            # The predicate is a relation.
            else:
                predicate = True

            # Create the predicate.
            p = Predicate.from_string(full_name, predicate, typ, self,
                                      partial, zero_arity)

            # Append the new predicate to the list.
            self.predicates.append(p)

    def lookup(self, string: str):
        """
        TODO
        REWORK ENTIRE METHOD.
        """
        return list(filter(lambda x: x,
                           map(lambda x: x.lookup(string), self.predicates)))

    def to_theory(self):
        """
        Convert the types into fact statements for the ProbLog theory.
        """
        theory = ''.join([x.to_theory() for x in self.types])
        return theory


class Type:
    """
    Class representing a type, i.e., a collection of elements over which can be
    iterated.
    The tricky part is that while pDMN is typed logic, ProbLog is not.
    In ProbLog, we introduce a predicate to denote an elements type.
    E.g., a type Person would be represented by `person(ann). person(bob).` in
    ProbLog.
    """
    def __init__(self, name: str, super_type, posvals="-"):
        """
        :arg str: the name of the type.
        :arg Type: the super type of the type.
        :arg str: posvals, the possible values of the type.
        """
        self.name = name
        if name != "Int" and name != "Float" and name != "Real" \
                and name != "String":
            self.display_name = self.name[0].lower() + self.name[1:]
        else:
            self.display_name = self.name[0].lower() + self.name[1:]
        self.super_type = super_type
        self.possible_values = posvals

        self.struct_args = []
        self.knows_values = True
        self.source_datatable = ""

        # Check the input.
        if posvals is None:
            raise ValueError(f"Values column for type {self.name} is empty."
                             f" Did you forget a '-'?")

        # Toggle knows_values if the values are known.
        if posvals == "_" or posvals == "-" or posvals == "−":
            self.knows_values = False
            self.possible_values = ""

    def __str__(self):
        """
        Magic method to turn the type into a string.

        :returns str: the typename.
        """
        return f"Type: {self.name}"

    def to_theory(self):
        """
        TODO
        """
        theory = ""
        if self.possible_values:
            for val in self.possible_values.split(','):
                theory += f"{self.display_name}({val.strip()}). "
            theory += "\n"
        return theory

    def match(self, value):
        if self.basetype == self:  # When comparing with string, int, float,...
            return re.match(f'^{self.name}$', value, re.IGNORECASE)
        else:
            return re.match(f'^{self.name}$', value)

    @property
    def basetype(self):
        """
        The basetype represents one of the ancestor types, such as int or str.

        :returns type: the basetype.
        """
        try:
            return self.super_type.basetype
        except AttributeError:
            return self


class Predicate:
    """
    Class which represents both predicates and functions.
    This double meaning is a relic of the past, and is to be fixed.
    In the future, a separate Function class should be created.

    In ProbLog, we represent an n-ary function by an (n+1)-ary predicate.
    """
    def __init__(self, name: str, args: List[Type], super_type: Type,
                 partial=False, full_name=None, zero_arity=False):
        """
        Initialises a predicate.
        :arg zero_arity: bool which should be True when the predicate is a
            0-arity predicate (constants and booleans).
        """
        self.name = name
        self.args = args
        self.super_type = super_type
        self.partial = partial
        self.repr = self.interpret_name()
        self.full_name = full_name
        self.struct_args = {}
        self.zero_arity = zero_arity

        if not self.args and self.is_function and not zero_arity:
            print(f'WARNING: "{self.name}" has been interpreted as single'
                  f' value instead of a function. Functions should be defined'
                  f' as FunctionName of Type and Type ...')
        elif not self.args and self.is_relation and not zero_arity:
            print(f'WARNING: "{self.name}" has been interpreted as a boolean'
                  f' value instead of a relation. Predicates should be defined'
                  f' as Type and Type ... is PredicateName')

    def __str__(self):
        """
        TODO
        """
        retstr = f"Predicate: {self.name}"
        return retstr

    @staticmethod
    def from_string(full_name: str, predicate: bool, super_type: Type,
                    glossary: Glossary, partial=False,
                    zero_arity=False):
        """
        Static method to create a predicate from string.

        :arg str: full_name, the full name.
        :arg bool: predicate, true if predicate, false if function.
        :arg Type: super_type, the super type of the predicate.
        :arg Glossary: glossary, the glossary.
        :arg bool: partial, whether or not it's a partial function.
        :arg zero_arity: bool which should be True when the predicate is a
            0-arity predicate (constants and booleans).
        :returns Predicate:
        """
        if not predicate:  # Check if it's a function.
            regex = (r'^(?P<name>.*)$')
        else:
            regex = (r'^(?P<name>.*)$')
        try:
            name = re.match(regex, full_name).group('name')
        except AttributeError:
            name = full_name
        try:
            # args = re.match(regex, full_name).group('args').split(' and ')
            raise IndexError
        except (AttributeError, IndexError):
            if zero_arity:
                return Predicate(full_name, [], super_type, partial,
                                 zero_arity=zero_arity)
            else:  # We need to find the relation's types.
                # We simply loop over all words and look for full matches.
                # TODO This should be done better. Types could be multiple
                # words.
                args = []
                name_elements = full_name.split(" ")

                for element in name_elements:
                    for t in glossary.types:
                        if re.fullmatch(element, t.name):
                            args.append(t)
                            break
                return Predicate(name, args,
                                 super_type, partial,
                                 full_name, zero_arity)

        return Predicate(name, [glossary.find_type(t) for t in args],
                         super_type, partial, full_name, zero_arity)

    def is_function(self):
        """
        Method to check whether the predicate is a function.
        Since only functions have super types, we use that as a check.
        Note that constants are a special case of functions.

        :returns boolean:
        """
        if self.super_type is None:
            return False
        else:
            return True

    def is_relation(self):
        """
        Method to check whether the predicate is a relation.
        A predicate is either a relation or a function, so we use that as a
        check. Note that booleans are a special case of relations.

        :returns boolean:
        """
        return not self.is_function()

    def interpret_name(self):
        """
        Method to interpret the name.
        This method forms a generic name representation, by replacing the
        arguments by dummies.
        In this way, it creates a skeleton structure for the name.

        Thus, it returns the name, without the arguments.
        For instance, `Country borders Country` becomes
        `(?P<arg0>.+) borders (?P<arg1>.+)`.
        This way, arg0 and arg1 can be found easily later on.
        """
        if not self.args:
            return self.name
        elif self.args:
            name_elements = self.name.split(" ")
            new_alias = ""
            arg_index = 0
            arglist = [arg.name for arg in self.args]
            for element in name_elements:
                if element in arglist:
                    new_alias += f"(?P<arg{arg_index}>.+) "
                    arg_index += 1
                    continue
                else:
                    new_alias += f"{element} "
            return new_alias[:-1]  # We drop the last space.
        else:
            raise ValueError("No idea what went wrong.")

    def lookup(self, string: str):
        """
        Method to compare a string to this predicate, to see if the predicate
        appears in the string in any form.
        TODO: make this more clear.
        """
        d = re.match(self.repr, string)
        if d:
            d = d.groupdict()
            return self, [v for k, v in sorted(d.items(),
                                               key=(lambda x: int(x[0][3:])))]
