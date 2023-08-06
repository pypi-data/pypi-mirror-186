"""
Code for the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""
import argparse
from pdmn.glossary import Glossary
from pdmn.interpret import VariableInterpreter
from pdmn.idply import Parser
import sys
from pdmn.table_operations import (fill_in_merged, identify_tables,
                                   find_glossary, find_execute_method,
                                   create_theory)
# from post_process import merge_definitions


def main():
    """
    The main function for the pDMN solver.
    """

    if len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v']:
        print('pDMN solver 1.0.0')
        return

    # Parse the arguments.
    argparser = argparse.ArgumentParser(description='Run pDMN on DMN tables.')
    argparser.add_argument('path_to_file', metavar='path_to_file', type=str,
                           help='the path to the xlsx or xml file')
    argparser.add_argument('-n', '--name', metavar='name_of_sheet', type=str,
                           help='the name(s) of the sheet(s) to execute',
                           nargs='+')
    argparser.add_argument('-o', '--outputfile', metavar='outputfile',
                           type=str,
                           default=None,
                           help='the name of the outputfile')
    argparser.add_argument('-x', '--execute',
                           action='store_true',
                           help='execute the .lp file using ProbLog')
    args = argparser.parse_args()

    # Open the file on the correct sheet and read all the tablenames.
    filepath = args.path_to_file

    if filepath.endswith('.xlsx'):
        sheetnames = args.name
        if sheetnames is None:
            raise IOError("No sheetname given")
        sheets = fill_in_merged(filepath, sheetnames)
        tables = identify_tables(sheets)

    else:
        raise IOError("Invalid filepath")

    g = Glossary(find_glossary(tables))
    query_preds = find_execute_method(tables)
    i = VariableInterpreter(g)
    parser = Parser(i)

    # Create the theory.
    theory = create_theory(tables, parser, g, query_preds)
    print('Done parsing.')
    if len(parser.parsing_errors) != 0:
        print("Errors detected in specification.\nUnable to parse headers:")
        for header, error_list in parser.parsing_errors.items():
            print(f"\tin {header}:")
            for error in error_list:
                print(f"\t\t{error}")
        print("No output was created.")
        return
    # If an output file is listed, write to it.
    if args.outputfile:
        file_path = args.outputfile
        if ".lp" not in args.outputfile:
            file_path += args.name_of_sheet.replace(' ', '_') + ".lp"
        fp = open(file_path, 'w')
        fp.write(theory)
        fp.close()

    # If execution requested, run ProbLog.
    if args.execute:
        from problog.program import PrologString
        from problog import get_evaluatable

        p = PrologString(theory)

        print(get_evaluatable().create_from(p).evaluate())

if __name__ == "__main__":
    main()
