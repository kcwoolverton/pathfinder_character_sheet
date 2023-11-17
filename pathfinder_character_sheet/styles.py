#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc0c64093

# Compiled with Coconut version 3.0.3-post_dev30

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3-post_dev30', '', False)
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

import justpy as jp  #1 (line in Coconut source)

background_color = "#f9f9f9"  #3 (line in Coconut source)
button_color = "blue-500"  #4 (line in Coconut source)
hover_color = "blue-600"  #5 (line in Coconut source)
header_color = "#A0522D"  #6 (line in Coconut source)
text_color = "text-white"  #7 (line in Coconut source)

table_classes = "min-w-full bg-white border rounded shadow"  #9 (line in Coconut source)
table_style = "transform: scale(1.0)"  #10 (line in Coconut source)
header_row_classes = "bg-gray-300"  #11 (line in Coconut source)
header_cell_classes = "py-2 px-3 text-center"  #12 (line in Coconut source)
cell_classes = "border text-center items-center justify-center"  #13 (line in Coconut source)
cell_style = ""  #14 (line in Coconut source)

ac_classes = "flex w-full p-4 m-4"  #16 (line in Coconut source)

flex_row_classes = "flex w-full gap-4"  #18 (line in Coconut source)
flex_row_style = "background-color: {_coconut_format_0};".format(_coconut_format_0=(background_color))  #19 (line in Coconut source)
one_third_col_classes = "flex flex-col w-1/3 gap-4"  #20 (line in Coconut source)

large_row_classes = "flex w-full gap-4 pb-8"  #22 (line in Coconut source)
large_row_style = "background-color: {_coconut_format_0};".format(_coconut_format_0=(background_color))  #23 (line in Coconut source)

reset_button_classes = "bg-{_coconut_format_0} hover:bg-{_coconut_format_1} {_coconut_format_2} font-bold py-2 px-4 rounded".format(_coconut_format_0=(button_color), _coconut_format_1=(hover_color), _coconut_format_2=(text_color))  #25 (line in Coconut source)
reset_button_style = ""  #26 (line in Coconut source)

checkbox_div_classes = "flex w-full p-4 m-4"  #28 (line in Coconut source)
checkbox_div_style = "background-color: transparent;"  #29 (line in Coconut source)
checkbox_classes = "bg-blue-500 m-2 p-2"  #30 (line in Coconut source)
checkbox_style = "transform: scale(1.0);"  #31 (line in Coconut source)

hit_points_classes = "border border-gray-300 shadow-lg p-4 rounded-md m-4 focus:outline-none focus:bg-white focus:border-purple-500"  #33 (line in Coconut source)
hit_points_style = ""  #34 (line in Coconut source)

collapse_button_classes = 'bg-{_coconut_format_0} hover:bg-{_coconut_format_1} {_coconut_format_2} font-bold py-2 px-4 flex justify-between items-center'.format(_coconut_format_0=(button_color), _coconut_format_1=(hover_color), _coconut_format_2=(text_color))  #36 (line in Coconut source)
spell_button_classes = 'bg-{_coconut_format_0} hover:bg-{_coconut_format_1} {_coconut_format_2} font-bold py-2 px-4'.format(_coconut_format_0=(button_color), _coconut_format_1=(hover_color), _coconut_format_2=(text_color))  #37 (line in Coconut source)
collapse_button_style = ""  #38 (line in Coconut source)

roll_cell_style = ""  #40 (line in Coconut source)
roll_cell_classes = "bg-{_coconut_format_0} hover:bg-{_coconut_format_1} {_coconut_format_2} font-bold py-2 px-4 text-center".format(_coconut_format_0=(button_color), _coconut_format_1=(hover_color), _coconut_format_2=(text_color))  #41 (line in Coconut source)

caret_style = ""  #43 (line in Coconut source)
caret_classes = "fas fa-angle-down right-2"  #44 (line in Coconut source)

@_coconut_tco  #46 (line in Coconut source)
def make_col_flex_div(overflow=False):  #46 (line in Coconut source)
    classes = "flex-col w-full"  #47 (line in Coconut source)
    if overflow:  #48 (line in Coconut source)
        classes += " overflow-auto overflow-x-auto"  #49 (line in Coconut source)
    return _coconut_tail_call(jp.Div, classes=classes, style="background-color: {_coconut_format_0}".format(_coconut_format_0=(background_color)))  #50 (line in Coconut source)



def make_title_box(height,  # type: str  #53 (line in Coconut source)
    width,  # type: str  #53 (line in Coconut source)
    title,  # type: str  #53 (line in Coconut source)
    click=None, text="", overflow=False):  #53 (line in Coconut source)
    box_style = "background-color: #f9f9f9; border: 1px solid #ccc; shadow-lg; padding: 20px; w-{_coconut_format_0}; height: {_coconut_format_1}; rounded;".format(_coconut_format_0=(width), _coconut_format_1=(height))  #54 (line in Coconut source)
    if overflow:  #55 (line in Coconut source)
        box_style += " overflow-y: auto;"  #56 (line in Coconut source)
    if click:  #57 (line in Coconut source)
        box = jp.Div(classes="bg-{_coconut_format_0} hover:bg-{_coconut_format_1} {_coconut_format_2} shadow-lg p-4 m-4 rounded-md flex items-center justify-center".format(_coconut_format_0=(button_color), _coconut_format_1=(hover_color), _coconut_format_2=(text_color)), style="border:tpx: solid #ccc; shadow-lg; padding: 20px; w-{_coconut_format_0}; height: {_coconut_format_1}".format(_coconut_format_0=(width), _coconut_format_1=(height)), inner_html="<b>" + text, click=click)  #58 (line in Coconut source)
    else:  #64 (line in Coconut source)
        box = jp.Div(classes="border border-gray-300 shadow-lg p-4 rounded-md m-4 flex text-center items-center justify-center", style=box_style, text=text)  #65 (line in Coconut source)
    title = jp.H2(classes="font-bold mb-2 text-center justify-center", text=title)  #67 (line in Coconut source)
    box.add(title)  #68 (line in Coconut source)
    return box  #69 (line in Coconut source)
