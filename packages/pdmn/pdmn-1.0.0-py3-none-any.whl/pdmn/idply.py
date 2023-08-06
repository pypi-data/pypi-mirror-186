"""
This file is part of the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""

import re
from ply import lex, yacc
from pdmn.interpret import VariableInterpreter, PredicateInterpretation


class Parser:
    """
    The parser is used to parse pDMN strings and find out their underlying
    secrets.
    This is a complex part of the solver, and works on magic and hope.
    """
    def __init__(self, i: VariableInterpreter):
        """
        Initialises the parser.

        :arg i: a VariableInterpreter object.
        :returns Object:
        """
        self.result = ''
        self.interpreter = i
        self.lexer = lex.lex(module=self)
        self.parser = yacc.yacc(module=self)
        self.variables = []
        self.expected_type = None
        self.parsing_errors = {}

    def parse_val(self, column_header: str, value: str) -> str:
        """
        Parse a pDMN notation inside a cell.

        :param column_header: the column header of the cell
        :param value: the value inside the cell
        :returns str: the parsed notation.
        """
        # self.variables = variables
        self.result = ''
        if value is None or re.match('^-$', str(value)):
            return ""

        comparator = '^(?:>|<)(?:=)?|='

        if '=' in column_header:
            column_header, value = column_header.split('=')

        if not re.match(comparator, str(value)):
            value = f'= {value}'

        try:
            self.parser.parse(column_header + value)
        except ValueError:
            error = (f"Encountered error when parsing: "
                     f"unable to parse \"{value}\" in column"
                     f" \"{column_header}\"")
            if column_header in self.parsing_errors:
                self.parsing_errors[column_header].append(value)
            else:
                self.parsing_errors[column_header] = [value]
        self.variables = []
        self.expected_type = None
        self.result = self.result[0].lower() + self.result[1:]

        return self.result

    reserved = {
        'Not': 'NOT',
        'not': 'NOT',
        'yes': 'YES',
        'Yes': 'YES',
        'No': 'NO',
        'no': 'NO',
        'abs': 'ABS',
        'Abs': 'ABS',
        'min': 'MIN',
        'Min': 'MIN',
        'max': 'MAX',
        'Max': 'MAX'
    }

    tokens = [
                 'NUMBER', 'COMPARE',
                 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'COMMA',
                 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'UNTIL', 'ID',
                 'PERCENT', 'STRAIGHTQUOTE', 'LQUOTE', 'RQUOTE',
                 'LACC', 'RACC', 'DOT', 'HASHTAG'
             ] + list(reserved.values())

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9\s]*'
        t.value = t.value.strip()
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    t_PLUS = r'\+'
    t_MINUS = r'(-|−)'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACK = r'\['
    t_RBRACK = r'\]'
    t_UNTIL = r'\.\.'
    t_COMMA = r','
    t_COMPARE = r'(>|<)(=)?'
    t_EQUALS = r'='
    t_PERCENT = r'%'
    t_STRAIGHTQUOTE = r'"'
    t_LQUOTE = '“'
    t_RQUOTE = '”'
    t_LACC = r"\{"
    t_RACC = r"\}"
    t_DOT = r'\.'
    t_HASHTAG = r'\#'

    def t_NUMBER(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Warning: Integer value too large %d", t.value)
            t.value = 0
        return t

    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UMINUS', 'HASHTAG'),
    )

    # A statement serves as the returnvalue:
    # if a statement is found, we return it.
    # As long as there is no rule that forms a statement, the yacc will try to
    # keep looking for matches.
    # A match that forms a statement, ends the search.
    def p_returnval(self, t):
        'return : statement'
        self.result = t[1]

    # Yes and No just return the name of the predicate.
    def p_yes(self, t):
        '''statement : expression EQUALS YES'''
        t[0] = f'{t[1]}'

    def p_no(self, t):
        '''statement : expression EQUALS NO'''
        t[0] = f'\+{t[1]}'

    # A don't care doesn't need any notation.
    def p_dontcare(self, t):
        '''statement : expression EQUALS MINUS
                     | expression EQUALS '''

    def p_eqnotlist(self, t):
        'statement : expression EQUALS NOT LPAREN expression RPAREN'
        pred = str(t[1])
        if ')' in str(t[1]):
            t[0] = f'\+{pred.split(")")[0]}, {t[5]})'
        else:
            t[0] = f'\+{pred}({t[5]})'

    def p_eqnot(self, t):
        'statement : expression EQUALS NOT LPAREN list RPAREN'
        t[0] = '\+{}'.format(' | '.join('{} = {}'
                                         .format(t[1], x) for x in t[5]))

    def p_eqlist(self, t):
        '''statement : expression EQUALS list'''
        t[0] = '({})'.format(' | '.join('{} = {}'
                                        .format(t[1], x) for x in t[3]))

    def p_equals(self, t):
        '''statement : expression EQUALS expression'''
        pred = str(t[1])
        if ')' in str(t[1]):
            t[0] = f'{pred.split(")")[0]}, {t[3]})'
        else:
            t[0] = f'{pred}({t[3]})'
        # t[0] = f'{t[1]}'

    def p_compare(self, t):
        '''statement : expression COMPARE expression'''
        t[0] = f'{t[1]} {t[2]} {t[3]}'

    def p_range(self, t):
        """
        statement : expression EQUALS lbound expression UNTIL expression rbound
                  | expression EQUALS lbound expression COMMA expression rbound
        """
        comp_1 = '<' if t[3] in ['(', ']'] else '=<'
        comp_2 = '<' if t[7] in [')', '['] else '=<'
        t[0] = f"{t[4]} {comp_1} {t[1]} & {t[1]} {comp_2} {t[6]}"

    def p_prange(self, t):
        """
        statement : expression EQUALS LPAREN expression UNTIL expression RPAREN
        """
        comp_1 = '<' if t[3] in ['(', ']'] else '=<'
        comp_2 = '<' if t[7] in [')', '['] else '=<'
        t[0] = f"{t[4]} {comp_1} {t[1]} & {t[1]} {comp_2} {t[6]}"

    # Dirty workaround to fix bug.
    def p_rrange(self, t):
        """
        statement : expression EQUALS LPAREN expression UNTIL expression RBRACK
        """
        comp_1 = '<' if t[3] in ['(', ']'] else '=<'
        comp_2 = '<' if t[7] in [')', '['] else '=<'
        t[0] = f"{t[4]} {comp_1} {t[1]} & {t[1]} {comp_2} {t[6]}"

    def p_nrange(self, t):
        """
        statement : expression EQUALS NOT LPAREN lbound expression COMMA \
        expression rbound RPAREN
        """
        comp_1 = '<' if t[3] in ['(', ']'] else '=<'
        comp_2 = '<' if t[7] in [')', '['] else '=<'
        t[0] = f"{t[1]} {comp_1} {t[4]} & {t[4]} {comp_2} {t[6]}"

    # A list is 2 expressions seperated by a comma.
    # Lists that exist of multiple comma's will be seperated and added to the
    # array one by one.
    def p_list(self, t):
        '''list : expression COMMA expression
                | list COMMA expression'''
        try:
            t[1].append(t[3])
            t[0] = t[1]
        except AttributeError:
            t[0] = [t[1], t[3]]

    def p_expression_abs(self, t):
        'expression : ABS expression'
        t[0] = f'abs({t[2]})'

    def p_quotes(self, t):
        '''
        expression : LQUOTE expression RQUOTE
                   | STRAIGHTQUOTE expression STRAIGHTQUOTE
        '''
        t[0] = f'\"{t[2]}\"'

    def p_domain_size(self, t):
        '''
        expression : HASHTAG expression
        '''
        type_name = re.findall(r"(.*?)(\[| |$)", str(t[2]))[0][0]
        t[0] = f'#{{ typevar[{type_name}_t] : true}}'

    def p_expression_binop(self, t):
        """
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE DIVIDE expression
                   | expression DIVIDE expression
                   | expression PERCENT expression
        """
        if t[2] == '+':
            t[0] = f'{t[1]} + {t[3]}'
        elif t[2] == '-':
            t[0] = f'{t[1]} - {t[3]}'
        elif t[2] == '*':
            t[0] = f'{t[1]} * {t[3]}'
        elif t[2] == '/':
            t[0] = f'{t[1]}/{t[3]}'
            if t[3] == '/':  # For // operator.
                t[0] = f'({t[1]} - {t[1]}%{t[4]})/{t[4]}'
        elif t[2] == '%':
            t[0] = f'{t[1]} % {t[3]}'

    def p_expression_uminus(self, t):
        'expression : MINUS expression %prec UMINUS'
        t[0] = f'-{t[2]}'

    def p_expression_group(self, t):
        'expression : LPAREN expression RPAREN'
        t[0] = t[1] + t[2] + t[3]

    def p_lbound(self, t):
        '''lbound : LPAREN
                  | LBRACK
                  | RBRACK'''
        t[0] = t[1]

    def p_rbound(self, t):
        '''rbound : RPAREN
                  | RBRACK
                  | LBRACK'''
        t[0] = t[1]

    def p_expression_number(self, t):
        'expression : NUMBER'
        t[0] = t[1]

    def p_dot(self, t):
        'expression : NUMBER DOT NUMBER'
        t[0] = f"{t[1]}.{t[3]}"

    def p_expression_name(self, t):
        'expression : ID'
        try:
            interpretation = self.interpreter.interpret_value(t[1], self.variables,
                                                              self.expected_type)
        except KeyError as e:
            raise ValueError(e)
        if self.expected_type is None and not t[1] == '__PLACEHOLDER__':
            try:
                self.expected_type = interpretation.type.name
            except AttributeError:
                self.expected_type = ""

        if (type(interpretation) == PredicateInterpretation):
            t[0] = interpretation
        elif not self.expected_type:
            t[0] = interpretation
        else:
            t[0] = f'{interpretation}'

    def p_error(self, t):
        try:
            print(f"Syntax error at '{t.value}'")
            raise ValueError(f"Syntax error at '{t.value}'")
            # breakpoint()
        except AttributeError:
            pass
