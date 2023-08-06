from __future__ import annotations
import re


def load_file(path: str, mode: str = "r") -> list[str]:
    with open(path, mode) as file:
        lines = file.readlines()
    return lines


def get_macro_content(line: str) -> tuple[int]:
    """ for now works only for line containing a single macro. """
    macro_start, macro_end = line.index('{'), line.index('}')
    return line[macro_start + 1:macro_end]


def clean_content(content: str) -> str:
    r""" Remove occurences of \something or \\
    e.g.: \Huge Some \\ Title => Some Title
    """
    regex = r"\\[^\s][a-zA-Z0-9]*"
    matches = re.finditer(regex, content, re.MULTILINE)
    matches = [match.group() for match in matches]
    return ' '.join(list(filter(lambda x: x not in matches, content.split())))


def parse_title(lines: list[str]) -> str:
    raw_title = list(filter(lambda x: r"\title{" in x, lines))[0]
    return clean_content(get_macro_content(raw_title))


# _______________________________________________________________________________________________ #

def extract_newcommands(lines: list[str]) -> list[str]:
    return list(filter(lambda x: r"\newcommand{" in x, lines))


def parse_newcommand(newcommand: str) -> tuple[str]:
    num_args = 0
    macro_start, macro_end = newcommand.index('{') + 1, newcommand.index('}')
    if newcommand[macro_end + 1] == '[':
        num_args = int(newcommand[macro_end + 2])
    command_start = macro_end + newcommand[macro_end:].index('{') + 1
    command_end = len(newcommand) - newcommand[::-1].find('}') - 1
    return newcommand[macro_start:macro_end], newcommand[command_start:command_end], num_args


def parse_args(content: str, macro: str, num_args: int) -> tuple[list[str], int]:
    args = list()
    arg_start = content.index(macro) + len(macro) + 1
    for _ in range(num_args):
        # because there could be nested braces within the argument definition.
        # e.g.: \macro{some_other_macro{arg1}}
        braces_count = 1
        for i, char in enumerate(content[arg_start:]):
            if char == '{':
                braces_count += 1
            if char == '}':
                braces_count -= 1
            if braces_count == 0:
                break
        arg_end = arg_start + i
        arg = content[arg_start:arg_end]
        args.append(arg)
        # because if another arg follows the current arg, there is "}{" after arg_end.
        arg_start = arg_end + 2
    return args, arg_end + 1


def basic_replace(occurence: str, macro: str, command: str, num_args: int) -> str:
    return occurence.replace(macro, command)


def replace_with_args(occurence: str, macro: str, command: str, num_args: int) -> str:
    args, args_end = parse_args(occurence, macro, num_args)
    macro_start = occurence.index(macro)
    macro_string = occurence[macro_start:args_end]
    processed_string = occurence.replace(macro_string, command)
    for i, arg in enumerate(args):
        processed_string = processed_string.replace(f"#{i+1}", arg)
    return processed_string


def replace_newcommand(lines: list[str], macro: str, command: str, num_args: int = 0) -> None:
    """ Modify lines in place. """
    replace_fn = replace_with_args if num_args > 0 else basic_replace
    # bellow [1:] is because first occurence is definition
    occurences = list(filter(lambda x: macro in x, lines))[1:]
    occurences_idx = [lines.index(occ) for occ in occurences]
    for occurence, idx in zip(occurences, occurences_idx):
        lines[idx] = replace_fn(occurence, macro, command, num_args)


def replace_newcommands(lines: list[str]):
    """ Modify lines in place. """
    newcommands = extract_newcommands(lines)
    for newcommand in newcommands:
        replace_newcommand(lines, *parse_newcommand(newcommand))
