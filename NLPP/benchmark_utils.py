import itertools
import os
import json
import sys
import asyncio



def get_function_body(code):
    # Extract the function body from the provided code
    lines = code.splitlines()
    function_count = 0
    function_lines = []
    
    for line in lines:
        if line.strip().startswith('def '):
            function_count += 1
            if function_count > 6:  # if more than 3 functions start, break the loop
                break
        elif not line.startswith((' ', '\t')) and not line.strip() == '':
            # If a non-empty line does not start with an indent, break the loop
            if function_count > 0:
                break
        if function_count > 0:
            function_lines.append(line)
            
    return '\n'.join(function_lines)

def get_function_body_old(code):
    lines = code.splitlines()
    function_lines = []
    found_def = False

    for line in lines:
        # If 'def ' is found in a line, mark that we've entered the function
        if 'def ' in line:
            found_def = True
            function_lines.append(line)
            continue

        # If we've entered the function, stop including lines when we hit a line that contains text but does not start with a whitespace character
        if found_def and line.strip() != '' and not line.startswith((' ', '\t')):
            break

        # Always include the line in the function lines
        function_lines.append(line)

    return '\n'.join(function_lines)

def cut_off_prefix_old(s):
    idx_from = s.find('from ')
    idx_def = s.find('def ')
    idx_import = s.find('import ')

    # Check if none of the keywords were found
    if idx_from == -1 and idx_def == -1 and idx_import == -1:
        return s

    # Prepare a list of found indices, excluding those where the keyword was not found
    indices = [idx for idx in [idx_from, idx_def, idx_import] if idx != -1]

    # Return the string starting from the earliest found keyword
    return s[min(indices):]

def extract_code_old(code):
    code = cut_off_prefix(code.split("```python")[-1])
    code = get_function_body(code)
    return code

    
def cut_off_prefix(s):
    # Cut off the prefix from the provided string
    indices = [idx for keyword in ['from ', 'def ', 'import '] if (idx := s.find(keyword)) != -1]
    return s[min(indices):] if indices else s

def extract_code(code, assistant_tag="", use_old_parser = False):
    if use_old_parser:
        return extract_code_old(code)
    
    if assistant_tag == "":
        try:
            return get_function_body(cut_off_prefix(code.split("```python")[1]))
        except:
            return get_function_body(cut_off_prefix(code))
    # print("***", code, "***")
    try:
        return get_function_body(cut_off_prefix(code.split(assistant_tag)[1].split("```python")[1]))
    except:
        return get_function_body(code.split(assistant_tag)[1])

