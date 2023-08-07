# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022/12/08 13:18:24
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's print methods
══════════════════════════════
"""


import pprint
from urwid import old_str_util
from varname import nameof

from .rbasic import check_parm, is_iterable


def format_data(data: "object", indent_char: "str"="    ") -> "str":
    """
    Format data as string.
    """

    check_parm(indent_char, str)

    data_str = str(data).replace(" ", "")
    indent_n = 0
    data = []
    for char_index in range(len(data_str)):
        char = data_str[char_index]
        if char == ",":
            data.append(char)
            data.append("\n" + indent_char * indent_n)
        elif char == ":":
            data.append(char + " ")
        elif char in "[({" and data_str[char_index + 1] not in "])}":
            indent_n += 1
            data.append(char)
            data.append("\n" + indent_char * indent_n)
        elif char in "])}" and data[-1] not in "[({":
            indent_n -= 1
            data.append("\n" + indent_char * indent_n)
            data.append(char)
        else:
            data.append(char)
    data = "".join(data)
    return data

def pformat(content: "object", width: "int"=100) -> "str":
    """
    Based on module pprint.pformat, modify the chinese width judgment.
    """

    def _format(_self, object, stream, indent, allowance, context, level):
        objid = id(object)
        if objid in context:
            stream.write(pprint._recursion(object))
            _self._recursive = True
            _self._readable = False
            return
        rep = _self._repr(object, context, level)
        max_width = _self._width - indent - allowance
        width = get_width(rep)
        if width > max_width:
            p = _self._dispatch.get(type(object).__repr__, None)
            if p is not None:
                context[objid] = 1
                p(_self, object, stream, indent, allowance, context, level + 1)
                del context[objid]
                return
            elif isinstance(object, dict):
                context[objid] = 1
                _self._pprint_dict(object, stream, indent, allowance,
                                context, level + 1)
                del context[objid]
                return
        stream.write(rep)

    pprint.PrettyPrinter._format = _format
    content_str = pprint.pformat(content, width=width, sort_dicts=False)
    return content_str

def split_text(text: "str", length: "int", by_width: "bool"=False) -> "list":
    """
    Split text by length or not greater than display width.
    """

    check_parm(text, str)
    check_parm(length, int)
    check_parm(by_width, bool)

    texts = []
    if by_width:
        str_group = []
        str_width = 0
        for char in text:
            char_width = get_width(char)
            str_width += char_width
            if str_width > length:
                string = "".join(str_group)
                texts.append(string)
                str_group = [char]
                str_width = char_width
            else:
                str_group.append(char)
        string = "".join(str_group)
        texts.append(string)
    else:
        test_len = len(text)
        split_n = test_len // length
        if test_len % length:
            split_n += 1
        for n in range(split_n):
            start_indxe = length * n
            end_index = length * (n + 1)
            text_group = text[start_indxe:end_index]
            texts.append(text_group)
    return texts

def get_width(text: "str") -> "int":
    """
    Get text display width.
    """

    check_parm(text, str)
    
    total_width = 0
    for char in text:
        char_unicode = ord(char)
        char_width = old_str_util.get_width(char_unicode)
        total_width += char_width
    return total_width

def get_info(data: "object", info: "dict"={"size": 0, "total": 0, "types": {}}, surface: "bool"=True) -> "dict":
    """
    Get data informationTrue.
    """

    check_parm(info, dict)
    check_parm(surface, bool)

    data_type = type(data)
    info["total"] += 1
    info["types"][data_type] = info["types"].get(data_type, 0) + 1
    if data_type == dict:
        for element in data.values():
            get_info(element, info, False)
    elif is_iterable(data):
        for element in data:
            get_info(element, info, False)
    else:
        info["size"] = info["size"] + 1
    if surface:
        sorted_func = lambda key: info["types"][key]
        sorted_key = sorted(info["types"], key=sorted_func, reverse=True)
        info["types"] = {key: info["types"][key] for key in sorted_key}
        return info

def fill_width(text: "str", char: "str", width: "int", align: "str"="right") -> "str":
    """
    Text fill character by display width.

    Parameters
    ----------
    text : str
        Fill text.
    char : str
        Fill character.
    width : width
        Fill width.
    align : str {'left', 'right', 'center'}
        Align orientation.

        - 'left' : Fill right, align left.
        - 'right' : Fill left, align right.
        - 'center': Fill both sides, align center.
    
    Returns
    -------
    str
        Text after fill.
    """

    check_parm(text, str)
    check_parm(char, str)
    check_parm(width, int)
    check_parm(align, str)

    if get_width(char) != 1:
        error = ValueError("parameter char value error")
        raise error
    text_width = get_width(text)
    fill_width = width - text_width
    if fill_width > 0:
        if align == "left":
            new_text = "%s%s" % (char * fill_width, text)
        elif align == "right":
            new_text = "%s%s" % (text, char * fill_width)
        elif align == "center":
            fill_width_left = int(fill_width / 2)
            fill_width_right = fill_width - fill_width_left
            new_text = "%s%s%s" % (char * fill_width_left, text, char * fill_width_right)
        else:
            error = ValueError("parameter align value error")
            raise error
    else:
        new_text = text
    return new_text

def print_frame(content: "list", title: "str"=None, width: "int"=100) -> "None":
    """
    Print frame.
    """

    check_parm(content, list)
    check_parm(title, str, None)
    check_parm(width, int)
    
    width -= 2
    has_error = False
    print_blocks = []
    for block in content:
        try:
            if id(block) == id("-"):
                frame_split_line = "╠%s╣" % ("═" * width)
                print_blocks.append(frame_split_line)
            else:
                block_str = str(block)
                rows_str = block_str.split("\n")
                rows_str =[_row_str for row_str in rows_str for _row_str in split_text(row_str, width, True)]
                rows_str = ["║%s║" % fill_width(string, " ", width) for string in rows_str]
                block_str = "\n".join(rows_str)
                print_blocks.append(block_str)
        except Exception as e:
            has_error = True
            print_blocks.append(block)
    if title == None:
        title = ""
    else:
        title = f"╡ {title} ╞"
    if has_error:
        frame_top = "╒%s╕" % title.center(width, "═")
        frame_bottom = "╘%s╛" % ("═" * width)
    else:
        frame_top = "╔%s╗" % title.center(width, "═")
        frame_bottom = "╚%s╝" % ("═" * width)
    print_contents = [
        frame_top,
        *print_blocks,
        frame_bottom
    ]
    for print_content in print_contents:
        print(print_content)

def rprint(
        *args: "object",
        width: "int"=100,
        title: "str"=None,
        print_info: "bool"=False,
        format_module: "str | None"="pprint"
    ) -> "None":
    """
    Print data and data information.

    Parameters
    ----------
    *args : object
        Print contents.
    width : int
        Print frame width.
    title : str
        Print frame title.
    print_info : bool
        Whether print content data information.
    format_module : str {'pprint', 'reytool'} or None
        Content format module.

        - "pprint" : Use function pformat.
        - "reytool" : Use function format_data.
        - None : Not format.
    """

    check_parm(print_info, bool)
    check_parm(width, int)
    check_parm(title, str, None)
    check_parm(format_module, "pprint", "reytool", None)

    datas = []
    for data in args:
        datas.extend(["-", data])
    datas = datas[1:]
    if print_info:
        try:
            info = get_info(args)
        except:
            info = False
        if info:
            if info["types"][tuple] == 1:
                del info["types"][tuple]
            else:
                info["types"][tuple] -= 1
            info["types"] = ["%s: %s" % (key.__name__, val) for key, val in info["types"].items()]
            info["types"] = ", ".join(info["types"])
            datas = [
                f"size: {info['size']}",
                f"total: {info['total'] - 1}",
                info["types"],
                "-",
                *datas
            ]
    if title == None:
        try:
            title = nameof(*args, frame=2)
            if type(title) == tuple:
                title = " │ ".join(title)
        except:
            title = None
    dates_index = range(len(datas))
    if format_module == "pprint":
        _width = width - 2
        for date_index in dates_index:
            try:
                if datas[date_index] != "-":
                    datas[date_index] = pformat(datas[date_index], _width)
            except:
                pass
    elif format_module == "reytool":
        for date_index in dates_index:
            try:
                if datas[date_index] != "-":
                    datas[date_index] = format_data(datas[date_index])
            except:
                pass
    print_frame(datas, title, width)