#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc7c98d48

# Compiled with Coconut version 3.0.3

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3', '310', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == '__coconut__':
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

def get_stat_modifier(stat_value):  #1 (line in Coconut source)
    return (stat_value - 10) // 2  #2 (line in Coconut source)


@_coconut_tco  #4 (line in Coconut source)
def make_mod_text(mods) -> str:  #4 (line in Coconut source)
    output = []  #5 (line in Coconut source)
    for mod in mods:  #6 (line in Coconut source)
        mod_str = str(mod)  #7 (line in Coconut source)
        if int(mod) >= 0:  #8 (line in Coconut source)
            mod_str = "+" + str(mod)  #9 (line in Coconut source)
        output.append(mod_str)  #10 (line in Coconut source)

    return _coconut_tail_call("/".join, output)  #12 (line in Coconut source)


def roll_dice(rng, die_type, num_dice, num_rolls) -> list[int]:  #14 (line in Coconut source)
    rolls = []  #15 (line in Coconut source)
    for _ in range(num_rolls):  #16 (line in Coconut source)
        result = 0  #17 (line in Coconut source)
        for _ in range(num_dice):  #18 (line in Coconut source)
            result += rng.randint(1, die_type)  #19 (line in Coconut source)
        rolls.append(result)  #20 (line in Coconut source)
    return rolls  #21 (line in Coconut source)


@_coconut_tco  #23 (line in Coconut source)
def make_roll_result_text(rolls: list[int], modifiers: list[int]) -> str:  #23 (line in Coconut source)
    text = []  #24 (line in Coconut source)
    for i in range(len(rolls)):  #25 (line in Coconut source)
        roll_result = rolls[i]  #26 (line in Coconut source)
        if roll_result == 20:  #27 (line in Coconut source)
            roll_result = '<span class="text-blue-500">&#9734;{_coconut_format_0}&#9734;</span>'.format(_coconut_format_0=(roll_result))  #28 (line in Coconut source)
        elif roll_result == 1:  #29 (line in Coconut source)
            roll_result = '<span class="text-red-400">&#9785;{_coconut_format_0}&#9785;</span>'.format(_coconut_format_0=(roll_result))  #30 (line in Coconut source)
        text.append("Result: {_coconut_format_0} + {_coconut_format_1} = {_coconut_format_2}".format(_coconut_format_0=(roll_result), _coconut_format_1=(modifiers[i]), _coconut_format_2=(rolls[i] + modifiers[i])))  #31 (line in Coconut source)
    return _coconut_tail_call("<br>".join, text)  #32 (line in Coconut source)


def get_attack_info(attack_info_str: str) -> _coconut.typing.Tuple[str, str, int]:  #34 (line in Coconut source)
    num_dice, die, modifier = "", "", ""  #35 (line in Coconut source)
    curr_val = ""  #36 (line in Coconut source)
    for char in attack_info_str:  #37 (line in Coconut source)
        if num_dice == "":  #38 (line in Coconut source)
            if char == 'd':  #39 (line in Coconut source)
                num_dice = curr_val  #40 (line in Coconut source)
                curr_val = ""  #41 (line in Coconut source)
            else:  #42 (line in Coconut source)
                curr_val += char  #43 (line in Coconut source)
        elif die == "":  #44 (line in Coconut source)
            if char == '+' or char == '-':  #45 (line in Coconut source)
                die = curr_val  #46 (line in Coconut source)
                curr_val = char  #47 (line in Coconut source)
            else:  #48 (line in Coconut source)
                curr_val += char  #49 (line in Coconut source)
        else:  #50 (line in Coconut source)
            if not char == " ":  #51 (line in Coconut source)
                curr_val += char  #52 (line in Coconut source)
    if not die:  #53 (line in Coconut source)
        die = curr_val  #54 (line in Coconut source)
        modifier = 0  #55 (line in Coconut source)
    else:  #56 (line in Coconut source)
        modifier = curr_val  #57 (line in Coconut source)
    return num_dice, die, modifier  #58 (line in Coconut source)
