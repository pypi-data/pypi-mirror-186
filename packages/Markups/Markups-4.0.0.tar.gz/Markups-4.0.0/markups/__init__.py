# This file is part of python-markups module
# License: 3-clause BSD, see LICENSE file
# Copyright: (C) Dmitry Shachnev, 2012-2022

from importlib.metadata import entry_points
from typing import Literal, Optional, Union, overload

from markups.abstract import AbstractMarkup
from markups.asciidoc import AsciiDocMarkup
from markups.markdown import MarkdownMarkup
from markups.restructuredtext import ReStructuredTextMarkup
from markups.textile import TextileMarkup

__version_tuple__ = (4, 0, 0)
__version__ = '.'.join(map(str, __version_tuple__))

__all__ = [
    "AbstractMarkup",
    "AsciiDocMarkup",
    "MarkdownMarkup",
    "ReStructuredTextMarkup",
    "TextileMarkup",
    "find_markup_class_by_name",
    "get_all_markups",
    "get_available_markups",
    "get_markup_for_file_name",
]

builtin_markups = [
    MarkdownMarkup,
    ReStructuredTextMarkup,
    TextileMarkup,
    AsciiDocMarkup,
]

# Public API


def get_all_markups() -> list[type[AbstractMarkup]]:
    """
    :returns: list of all markups (both standard and custom ones)
    """
    try:  # Python 3.10+
        entrypoints = entry_points(group="pymarkups")
    except TypeError:  # Older versions
        entrypoints = entry_points()["pymarkups"]
    return [entry_point.load() for entry_point in entrypoints]


def get_available_markups() -> list[type[AbstractMarkup]]:
    """
    :returns: list of all available markups (markups whose
              :meth:`~markups.abstract.AbstractMarkup.available`
              method returns True)
    """
    available_markups = []
    for markup in get_all_markups():
        if markup.available():
            available_markups.append(markup)
    return available_markups


@overload
def get_markup_for_file_name(
    filename: str, return_class: Literal[False] = False
) -> Optional[AbstractMarkup]:
    ...


@overload
def get_markup_for_file_name(
    filename: str, return_class: Literal[True]
) -> Optional[type[AbstractMarkup]]:
    ...


def get_markup_for_file_name(
    filename: str, return_class: bool = False
) -> Optional[Union[AbstractMarkup, type[AbstractMarkup]]]:
    """
    :param filename: name of the file
    :param return_class: if true, this function will return
                         a class rather than an instance

    :returns: a markup with
              :attr:`~markups.abstract.AbstractMarkup.file_extensions`
              attribute containing extension of `filename`, if found,
              otherwise ``None``

    >>> import markups
    >>> markup = markups.get_markup_for_file_name('foo.mkd')
    >>> markup.convert('**Test**').get_document_body()
    '<p><strong>Test</strong></p>\\n'
    >>> markups.get_markup_for_file_name('bar.rst', return_class=True)
    <class 'markups.restructuredtext.ReStructuredTextMarkup'>
    """
    markup_class = None
    for markup in get_all_markups():
        for extension in markup.file_extensions:
            if filename.endswith(extension):
                markup_class = markup
    if return_class:
        return markup_class
    if markup_class and markup_class.available():
        return markup_class(filename=filename)
    return None


def find_markup_class_by_name(name: str) -> Optional[type[AbstractMarkup]]:
    """
    :returns: a markup with
              :attr:`~markups.abstract.AbstractMarkup.name`
              attribute matching `name`, if found, otherwise ``None``

    >>> import markups
    >>> markups.find_markup_class_by_name('textile')
    <class 'markups.textile.TextileMarkup'>
    """
    for markup in get_all_markups():
        if markup.name.lower() == name.lower():
            return markup
    return None
