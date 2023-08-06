"""
This file is part of the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""


import numpy as np
import re
from pdmn.idply import Parser
from typing import List


def variname(string: str) -> str:
    """
    Function to return the variable of a header in the form of "Type called
    var"

    :arg string: the headerstring of which the variable name needs to be found.
    :returns str: the variable name.
    """
    return re.split(r'\s+[cC]alled\s+', string)[-1]


class Table:
    """
    The table object represents decision and constraint tables.

    :attr name: str
    :attr hit_policy: str
    :attr inputs: List[np.array]
    :attr outputs: List[np.array]
    :attr output_values: List[str]
    :attr rules: List[np.array]
    """
    def __init__(self, array: np.array, parser: Parser, aux_var_needed=True):
        """
        Initialises a table object for decision or constraint tables.
        Table interprets and splits up every table into inputs, outputs, rules,
        name and hit policy, after which it doesn't save the table array.

        :arg array: the np.array containing the table.
        :arg Parser: the parser
        :returns Table:
        """
        self.inputs: List[np.array] = []
        self.outputs: List[np.array] = []
        self.rules: List[np.array] = []
        self.name = self._read_name(array)
        self.hit_policy = self._read_hitpolicy(array)
        self.aux_var_needed = aux_var_needed

        self._read_inputs(array)
        self._read_outputs(array)
        self._read_rules(array)
        self._read_output_values(array)
        self.parser = parser

    def _read_name(self, array: np.array) -> str:
        """
        Method to read the name of a table, which is located in the top-left
        cell.

        :arg array: the np.array containing the table.
        :returns str: the name of the table.
        """
        return array[0, 0]

    def _read_hitpolicy(self, array: np.array) -> str:
        """
        Method to read the hit policy of a table, which is located at [1,0].

        :arg array: the np.array containing the table.
        :returns str: the hit policy of the table.
        """
        # Single cells containing value shouldn't be interpreted as tables.
        if len(array) == 1:
            return "None"  # None in string, because it's used in regex checks.
        return array[1, 0]

    def _read_inputs(self, array: np.array) -> None:
        """
        Method to read all the input columns of a table.
        A column is an input column if the first cell contains the table name.
        E.g. the columns under the merged cells representing the name.

        :arg array: the np.array containing the table.
        :returns None:
        """
        for x in range(1, array.shape[1]):
            if array[0, x] != self.name:
                return
            self.inputs.append(array[1, x])

    def _read_outputs(self, array: np.array) -> None:
        """
        Method to read all the output columns of a table.
        A column is an output column if the first cell doesn't contain the
        table name.
        E.g. all columns not under the merged cells representing the name.

        :arg array: the np.array containing the table.
        :returns None:
        """
        for x in range(1, array.shape[1]):
            if array[0, x] == self.name:
                continue
            self.outputs.append(array[1, x])

    def _read_rules(self, array: np.array) -> None:
        """
        Method to read all the rules of a table.
        A rule is basically all the rows of a table that start with an index.

        :arg array: the np.array containing the table.
        :returns None:
        """
        # Single cells containing value shouldn't be interpreted as tables.
        if len(array) == 1:
            return
        for x in range(1, array.shape[0]):
            if array[x, 0] != self.hit_policy and array[x, 0] != None:
                break
        self.rules = array[x:, 1:]

    def _read_output_values(self, array: np.array) -> None:
        """
        Method to read output values, in the case of a chance table.

        :arg array: the np.array containing the table.
        :returns None:
        """
        if len(array) == 1:
            return
        for x in range(1, array.shape[0]):
            if array[x, 0] != self.hit_policy:
                break
        if array[x, 0] is None:
            self.output_values = list(array[x, 1:])
        else:
            self.output_values = []

    def _type_predicates(self, column_headers) -> List:
        # We also need to add the necessary *type* predicates.
        type_preds = set()  # Use set to avoid duplicates.
        for i, col in enumerate(column_headers):
            interpretation = self.parser.interpreter.interpret_value(col)
            for arg in interpretation.args:
                pred_name = interpretation.args[0].type.display_name
                type_pred = f"{pred_name}({arg})"
                type_preds.add(type_pred)
        return list(type_preds)

    def _export_definitions(self) -> str:
        """
        Method to export the table as definitions.
        When the hitpolicy is 'U' or 'A', we can translate the entire
        table into definitions in ProbLog form.

        If the output is idpz3, then we add a constraint which says that any
        one of the outputs needs to be true. Otherwise, they don't show up as
        relevant.

        :returns str: the table as definitions.
        """
        # Set the headername in comments.
        string = f'% {self.name}\n'
        # Iterate over every outputcolumn.
        for i, col in enumerate(self.outputs):
            if i > 0:
                # When creating a definition for the second, third, ... output,
                # we need to add the name again.
                string += f'% {self.name}\n'
            falsecount = 0
            for r, row in enumerate(self.rules):
                conditions = list(filter(
                    lambda x: x,
                    (self.parser.parse_val(variname(col), row[i])
                     for i, col in enumerate(self.inputs))))

                # If there are no probabilities present, the output values
                # appear in the rows itself.
                if not self.output_values:
                    conclusion = self.parser.parse_val(col,
                                                       row[i + len(self.inputs)])
                else:
                    conclusion = self.parser.parse_val(col,
                                                       self.output_values[i + len(self.inputs)])
                    probability = row[i + len(self.inputs)]
                    conclusion = f"{probability}::{conclusion}"
                # A definition can't contain a not in the conclusion.
                # A negation of a predicate is implied by the other rules.
                if '\+' in conclusion:
                    # If all the row are 'not', we need to specify that none of
                    # the predicates are true because there's no implicit
                    # rule which defines this.
                    if falsecount == len(self.rules) - 1:
                        conditions = "false"
                        conclusion = conclusion.replace("\+", " ")
                        conclusion = conclusion[2:-1]  # Strip the brackets.
                    else:
                        falsecount = falsecount + 1
                        continue
                if not conclusion:
                    continue
                conditions += self._type_predicates(self.inputs + self.outputs)
                if not conditions:
                    conditions = 'true'
                else:
                    conditions = ', '.join(conditions)
                if conditions:
                    string += (f'{conclusion} :- {conditions}.\n')
                else:
                    string += f'{conclusion}.\n'

            string += '\n\n'
        return string

    def _export_annotated_disjunction(self) -> str:
        """
        Method to export the table as annoted disjunction.

        :returns str: the table as definitions.
        """
        # Set the headername in comments.
        string = f'% {self.name}\n'
        # Iterate over every row.
        conclusions = []
        for r, row in enumerate(self.rules):
            # variables, iquantors, oquantors = self.variables_iq_oq(
            #                                   repres=quantor_repr)
            # We need to gather all conclusions to format them as AD.
            conclusions = []
            for i, col in enumerate(self.outputs):
                # Iterate over every col and interpret its probabilities.

                conditions = list(filter(lambda x: x,
                                         (self.parser.parse_val(variname(col),
                                                                row[i])
                                          for i, col in enumerate(self.inputs))))

                conclusion = self.parser.parse_val(col,
                                                   self.output_values[i + len(self.inputs)])
                probability = row[i + len(self.inputs)]
                conclusion = f"{probability}::{conclusion}"
                conclusions.append(conclusion)

            # We also need to add the necessary *type* predicates.
            conditions += self._type_predicates(self.inputs + self.outputs)

            if conditions:
                string += f"{';'.join(conclusions)} :- {','.join(conditions)}.\n"
            else:
                string += f"{';'.join(conclusions)}."
        string += '\n\n'
        return string

    def export(self):
        """
        Export tries to find the hit policy for a table, and then returns the
        method needed to transfer the table to idp form.
        These hit policies are currently:

          * A, U           -> translate to rules;
          * Ch             -> translate to annotated disjunction;

        Every hit policy has it's own method.

        :returns method: the output of export method for the table.
        """

        # List all possible hit policies.
        actions = {
            r'^[AUF]$': self._export_definitions,
            r'^Ch$': self._export_annotated_disjunction
        }
        # Try, except is necessary to avoid StopIteration error.
        try:
            # Find hit policy.
            hp = next(map(lambda x: x.re.pattern,
                          filter(lambda x: x,
                                 (re.match(x, self.hit_policy)
                                     for x in actions))))
        except StopIteration:
            return None
        return actions[hp]()
