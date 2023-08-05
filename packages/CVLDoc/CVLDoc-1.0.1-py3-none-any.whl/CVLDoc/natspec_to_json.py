import argparse
import json
import os
import re
from typing import Dict, List
import cvldoc_parser
import inflection


def natspec_to_json(args) -> None:
    """
    This is the main function of generating natspec information.
    the function is getting as an input a file and generating a Json !
    """
    if args.verbosity:
        print(f'input file(s) : {args.input_file}')

    # check file existence before sending them to the parser.
    for filename in args.input_file:
        if not os.path.isfile(filename):
            if args.verbosity:
                print(f'file name: {filename} doesn\'t exist, skipping it!')
            args.input_file.remove(filename)

    if not args.input_file:
        return

    # The parse function returns a list of documentations list, one
    # list for each input file.
    files_cvl_elements = cvldoc_parser.parse(args.input_file)
    # loop through all documentation lists.
    file_number = 0

    for cvlElements_list in files_cvl_elements:
        if args.verbosity:
            print(f'processing file: {args.input_file[file_number]}')

        json_object_list = handle_cvlElements_list(cvlElements_list)

        # build output file name from input file name
        input_filename, file_extension = os.path.splitext(args.input_file[file_number])
        output_filename = os.path.join(input_filename + '-natspec' + '.json')

        json_string = json.dumps(json_object_list, indent=4)
        json_file = open(output_filename, 'w')
        json_file.write(json_string)
        json_file.close()
        file_number += 1

    if args.verbosity:
        print('processing finished!')


def handle_cvlElements_list(cvlElement_list) -> List[Dict]:
    document_dicts = []
    for cvlElement in cvlElement_list:
        result_data = handle_cvlElement(cvlElement)
        if result_data is not None:
            document_dicts.append(result_data)

    return document_dicts


# handle a CVL element
# a documentation can be a 'Free form' or an actual 'Documentation' object
def handle_cvlElement(cvl_element) -> Dict[str, any]:

    # the resulted CVL element dictionary for JSON
    element_dict = {}

    # diagnostics messages are disabled for now.
    # diagnostics = cvl_element.diagnostics()
    #
    # # display all documentation diagnostic messages, if exist
    # for message in diagnostics:
    #     print_diag(message)

    # check if this item is a FreeForm text
    # copy the relevant entries ('type' and 'text').
    if cvl_element.ast.kind == 'freeform comment':
        # free form comment has only the block text. check if not
        if cvl_element.ast.text:
            element_dict['type'] = 'text'
            element_dict['text'] = cvl_element.ast.text
            return element_dict
        else:
            return None

    else:  # not a free form element
        element_dict['content'] = cvl_element.raw()
        element_dict['type'] = cvl_element.ast.kind
        if cvl_element.ast.name is not None:
            element_dict['id'] = cvl_element.ast.name
            element_dict['title'] = inflection.humanize(inflection.titleize(cvl_element.ast.name))

        # add parameters info, if exist
        param_list = []
        for param in cvl_element.ast.params:
            param_dict = {'type': param[0], 'name': param[1]}
            param_list.append(param_dict)
        if param_list:
            element_dict['params'] = param_list

        # get the return data type
        if cvl_element.ast.returns is not None:
            element_dict['return'] = {'type': cvl_element.ast.returns}

    # loop through all element tags, saving all @dev  tags together.
    dev_contents = []
    for doc_tag in cvl_element.doc:
        if doc_tag.kind == 'dev':
            dev_contents.append(doc_tag.description.strip())
        else:
            handle_tag(element_dict, doc_tag)

    #  join all @dev tags to one tag.
    if dev_contents:
        element_dict['dev'] = '\n'.join(dev_contents)

    return element_dict


def get_parser():
    # separate the argument parser definition
    parser = argparse.ArgumentParser(description='export Natspec comments to JSON file(s)',
                                     epilog='please, use with care')
    parser.add_argument('input_file', help='specify a name of input spec file ', type=str, nargs='+')
    parser.add_argument('-v', '--verbosity', help='increase output verbosity', action='store_true')
    parser.add_argument('-dev', '--development', help='produce developer report', action='store_true')
    parser.add_argument('-user', '--user', help='produce end user report', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s Ver 0.1')
    return parser


def print_diag(diagnostic):
    diag_msg = ''

    if diagnostic.severity == diagnostic.severity.Error:
        diag_msg += '*** Error! '
    elif diagnostic.severity == diagnostic.severity.Warning:
        diag_msg += 'Warning: '
    else:  # TODO
        diag_msg += 'Info: '

    diag_msg += f'line:  {diagnostic.range.start.line} Col: {diagnostic.range.start.character}: '
    diag_msg += diagnostic.description
    print(diag_msg)


# handle documentation tags
def handle_tag(doc_dict, tag):
    if tag.kind == 'title':
        doc_dict['title'] = tag.description
    elif tag.kind == 'notice':
        doc_dict['notice'] = tag.description
    elif tag.kind == 'formula':
        doc_dict['formula'] = tag.description
    elif tag.kind == 'return':
        ret_data = doc_dict['return']
        ret_data['comment'] = tag.description
    elif tag.kind == 'param':
        param_name_match = re.match(r"^\w+", tag.description)
        if param_name_match:
            # get the param name from the comment
            # find it in the param lists, and
            param_name = param_name_match.group()
            params_info_list = doc_dict['params']
            for param_info in params_info_list:
                if param_info['name'] == param_name:
                    param_info['comment'] = tag.description
    else:
        print(f'unsupported tag: {tag.kind}')


def entry_point():
    """Entry point for the application script"""
    parser = get_parser()
    args = parser.parse_args()
    natspec_to_json(args)


if __name__ == '__main__':
    entry_point()
