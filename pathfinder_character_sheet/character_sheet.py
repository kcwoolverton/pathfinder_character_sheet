#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2e498956

# Compiled with Coconut version 3.0.3-post_dev33

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3-post_dev33', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import argparse  #1 (line in Coconut source)
from random import Random  #2 (line in Coconut source)

import justpy as jp  #4 (line in Coconut source)
from pathfinder_character_sheet.character_sheet_frontend import *  #5 (line in Coconut source)
from pathfinder_character_sheet.character_sheet_parser import *  #6 (line in Coconut source)
from pathfinder_character_sheet.styles import *  #7 (line in Coconut source)

parser = argparse.ArgumentParser(description='Process some integers.')  #9 (line in Coconut source)
parser.add_argument('input_file', type=str, help='The xml file for your character.')  #10 (line in Coconut source)
parser.add_argument('--port', type=int)  #11 (line in Coconut source)

def server(char):  #13 (line in Coconut source)
    wp = jp.WebPage(data=_coconut.dict((('checked', False), ('hp', char.max_hp))))  #14 (line in Coconut source)
    jp.Link(href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css", a=wp)  #15 (line in Coconut source)

    main_div = jp.Div(classes="w-full h-screen p-4", style="background-color: {_coconut_format_0}".format(_coconut_format_0=(background_color)), a=wp)  #17 (line in Coconut source)
    rng = Random()  #18 (line in Coconut source)
    history_box = make_title_box("50px", "1/4", "", overflow=True)  #19 (line in Coconut source)
    large_row, button = make_large_row(wp, make_title_box("50px", "1/4", "", text="Long Rest", click=_coconut_partial(long_rest_click, char=char)), char, rng, history_box)  #20 (line in Coconut source)
    large_row.set_class('mt-4')  #27 (line in Coconut source)
    title_row = make_title_row(char, button, history_box)  #28 (line in Coconut source)
    main_div.add(title_row, make_useful_info_row(wp, button, char, rng, history_box), large_row)  #29 (line in Coconut source)
    return wp  #30 (line in Coconut source)


if __name__ == "__main__":  #32 (line in Coconut source)
    args = parser.parse_args()  #33 (line in Coconut source)
    file_to_read = args.input_file  #34 (line in Coconut source)
    if not file_to_read.endswith(".xml"):  #35 (line in Coconut source)
        raise ValueError("Input file must be an xml file.")  #36 (line in Coconut source)
    char = parse_xml(file_to_read)  # type: Character  #37 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #37 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #37 (line in Coconut source)
    __annotations__["char"] = 'Character'  #37 (line in Coconut source)
    @_coconut_tco  #38 (line in Coconut source)
    def server_partial():  #38 (line in Coconut source)
        return _coconut_tail_call(server, char)  #39 (line in Coconut source)

    port = 8080  #40 (line in Coconut source)
    if args.port:  #41 (line in Coconut source)
        port = args.port  #42 (line in Coconut source)
    jp.justpy(server_partial, port=port)  #43 (line in Coconut source)
