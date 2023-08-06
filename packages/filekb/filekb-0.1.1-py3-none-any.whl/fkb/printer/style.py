# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

import colored


def SetBackgroundColor(color: str) -> str:
    '''
    Set background color.
    Arguments:
    color       - the color string to set, that
                  can be either a word (e.g., 'green')
                  or an hex code (e.g., '#00AB00')
    Returns:
    A string representing the code to set the background color
    '''
    return colored.bg(color)


def SetForegroundColor(color: str) -> str:
    '''
    Set foreground color.
    Arguments:
    color       - the color string to set, that
                  can be either a word (e.g., 'green')
                  or an hex code (e.g., '#00AB00')
    Returns:
    A string representing the code to set the foreground color
    '''
    return colored.fg(color)


def SetStyle(style: str) -> str:
    '''
    Set a specific text style
    Arguments:
    style       - a string representing the desired
                  style, examples:
                  'bold'
                  'underline'
    Returns:
    A string representing the code to set the desired style
    '''
    return colored.attr(style)


def ResetStyle() -> str:
    '''
    Reset applied style.
    Returns:
    A string representing the code to reset the style and colors to default
    '''
    return colored.attr('reset')

def ColorizeString(string : str, color : str) -> str:
    '''
    This function applies the provided color to the specified string
    Arguments:
    msg   - The message to be colored
    color - The name of the color (or hex code), e.g., 'red' or '#C0C0C0'
    Returns:
    A colored message
    '''
    return SetForegroundColor(color) + string + ResetStyle()

ALT_BGROUND = SetBackgroundColor('#303030')
BOLD = SetStyle('bold')
UND = SetStyle('underlined')
RESET = ResetStyle()