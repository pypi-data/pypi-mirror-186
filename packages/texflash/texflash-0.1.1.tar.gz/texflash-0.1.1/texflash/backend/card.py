from __future__ import annotations
from datetime import date
from dataclasses import dataclass
import streamlit as st
from .parse import clean_content, get_macro_content


@dataclass
class Card:
    title: str
    content: list[str]
    delimiters: list[tuple[str, int, int]]
    stats: dict[date, list[int]] = None


class CardTagException(Exception):

    def __init__(self, title_start: int, tag: str) -> None:
        msg = f"""
        Card title start was found on line {title_start} but tag {tag} was not found afterward.
        """
        super().__init__(msg)


# _______________________________________________________________________________________________ #

def extract_card_title(lines: list[str], start: int, end: int):
    string = " ".join(lines[start:end]).replace("\n", "")
    return clean_content(get_macro_content(string))


def extract_card_content(lines: list[str], start: int, end: int) -> list[str]:
    card_content = list()
    string = lines[start:end]
    for line_idx in range(len(string)):
        line = string[line_idx].strip()
        if line.startswith(r"\item"):
            line = r"\item " + line[5:]
        card_content.append(line)
    return card_content


def parse_card_content(card_content: list[str]) -> list[tuple[str, int, int]]:
    macros = ("equation", "itemize", "enumerate")
    macros = {k: {"start": f"\\begin{{{k}}}", "end": f"\\end{{{k}}}"} for k in macros}
    all_tags = list()
    for tags in macros.values():
        all_tags.extend(list(tags.values()))
    parsed_card_content = list()
    line_idx = 0
    while line_idx < len(card_content):
        line = card_content[line_idx]
        for name, delimiters in macros.items():
            if delimiters["start"] in line:
                start = line_idx
                while not delimiters["end"] in line:
                    line_idx += 1
                    line = card_content[line_idx]
                line_idx += 1
                parsed_card_content.append((name, start, line_idx))
        if all(x not in line for x in all_tags):
            start = line_idx
            while not any(x in line for x in all_tags):
                line_idx += 1
                line = card_content[line_idx]
            parsed_card_content.append(("text", start, line_idx))
    return parsed_card_content


def clean_card_content(
    card_content: list[str], parsed_card_content: list[tuple[str, int, int]]
) -> list[str]:
    """ Clean everything but equation. """
    cleaned_content = list()
    for i, line in enumerate(card_content):
        for content_type, start, end in parsed_card_content:
            if start <= i < end:
                break
        if content_type != "equation":
            line = clean_content(line)
        cleaned_content.append(line)
    return cleaned_content


def make_card(
    lines: list[str], title_start: int, title_end: int, content_start: int, content_end: int
) -> Card:
    title = extract_card_title(lines, title_start, title_end)
    content = extract_card_content(lines, content_start, content_end)
    delimiters = parse_card_content(content)
    content = clean_card_content(content, delimiters)
    return Card(title, content, delimiters)


# _______________________________________________________________________________________________ #

def display_text(text: list[str]) -> None:
    st.write("\n".join(text))


def display_equation(equation: list[str]) -> None:
    string = ""
    for line in equation:
        string += line + "\n"
    st.latex(string)


def display_itemize(items: list[str]) -> None:
    string = ""
    for item in items[1:-1]:
        string += f"- {item[6:]}\n"  # remove \item
    st.write(string)


def display_enumerate(items: list[str]) -> None:
    string = ""
    for i, item in enumerate(items[1:-1]):
        string += f"{i+1}. {item}\n"
    st.write(string)


displayers = dict(
    text=display_text,
    equation=display_equation,
    itemize=display_itemize,
    enumerate=display_enumerate
)


def display_card_content(card: Card) -> None:
    for t, s, e in card.delimiters:
        displayers[t](card.content[s:e])
