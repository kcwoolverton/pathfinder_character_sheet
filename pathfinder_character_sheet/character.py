#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x88cac848

# Compiled with Coconut version 3.0.3

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3', '', False)
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
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

from dataclasses import dataclass  #1 (line in Coconut source)
import xml.etree.ElementTree as ET  #2 (line in Coconut source)
import argparse  #3 (line in Coconut source)
try:  #4 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #4 (line in Coconut source)
except _coconut.NameError:  #4 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #4 (line in Coconut source)
sys = _coconut_sys  #4 (line in Coconut source)
if sys.version_info >= (3, 4):  #4 (line in Coconut source)
    from enum import Enum  #4 (line in Coconut source)
else:  #4 (line in Coconut source)
    from aenum import Enum  #4 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #4 (line in Coconut source)
    sys = _coconut_sys_0  #4 (line in Coconut source)
from dataclasses import field  #5 (line in Coconut source)

class Stats(Enum):  #7 (line in Coconut source)
    STR = 0  #8 (line in Coconut source)
    DEX = 1  #9 (line in Coconut source)
    CON = 2  #10 (line in Coconut source)
    INT = 3  #11 (line in Coconut source)
    WIS = 4  #12 (line in Coconut source)
    CHA = 5  #13 (line in Coconut source)

_coconut_call_set_names(Stats)  #15 (line in Coconut source)
class Movement(Enum):  #15 (line in Coconut source)
    Walk = 0  #16 (line in Coconut source)
    Climb = 1  #17 (line in Coconut source)
    Swim = 2  #18 (line in Coconut source)
    Fly = 3  #19 (line in Coconut source)

_coconut_call_set_names(Movement)  #21 (line in Coconut source)
class SavingThrows(Enum):  #21 (line in Coconut source)
    fort = 0  #22 (line in Coconut source)
    ref = 1  #23 (line in Coconut source)
    will = 2  #24 (line in Coconut source)

_coconut_call_set_names(SavingThrows)  #26 (line in Coconut source)
@dataclass  #26 (line in Coconut source)
class Spell(_coconut.object):  #27 (line in Coconut source)
    name = ''  # type: str  #28 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #28 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #28 (line in Coconut source)
    __annotations__["name"] = 'str'  #28 (line in Coconut source)
    times_memorized = 0  # type: int  #29 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #29 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #29 (line in Coconut source)
    __annotations__["times_memorized"] = 'int'  #29 (line in Coconut source)
    spell_range = ''  # type: str  #30 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #30 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #30 (line in Coconut source)
    __annotations__["spell_range"] = 'str'  #30 (line in Coconut source)
    casting_time = ''  # type: str  #31 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #31 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #31 (line in Coconut source)
    __annotations__["casting_time"] = 'str'  #31 (line in Coconut source)
    time_units = ''  # type: str  #32 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #32 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #32 (line in Coconut source)
    __annotations__["time_units"] = 'str'  #32 (line in Coconut source)
    dc = 0  # type: int  #33 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #33 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #33 (line in Coconut source)
    __annotations__["dc"] = 'int'  #33 (line in Coconut source)
    duration = ''  # type: str  #34 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #34 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #34 (line in Coconut source)
    __annotations__["duration"] = 'str'  #34 (line in Coconut source)
    effect = ''  # type: str  #35 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #35 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #35 (line in Coconut source)
    __annotations__["effect"] = 'str'  #35 (line in Coconut source)
    target = ''  # type: str  #36 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #36 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #36 (line in Coconut source)
    __annotations__["target"] = 'str'  #36 (line in Coconut source)
    save_info = ''  # type: str  #37 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #37 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #37 (line in Coconut source)
    __annotations__["save_info"] = 'str'  #37 (line in Coconut source)
    level = 0  # type: int  #38 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #38 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #38 (line in Coconut source)
    __annotations__["level"] = 'int'  #38 (line in Coconut source)

_coconut_call_set_names(Spell)  #40 (line in Coconut source)
@dataclass  #40 (line in Coconut source)
class Character(_coconut.object):  #41 (line in Coconut source)
    name = ''  # type: str  #42 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #42 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #42 (line in Coconut source)
    __annotations__["name"] = 'str'  #42 (line in Coconut source)
    level = 0  # type: int  #43 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #43 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #43 (line in Coconut source)
    __annotations__["level"] = 'int'  #43 (line in Coconut source)
    max_hp = 0  # type: int  #44 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #44 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #44 (line in Coconut source)
    __annotations__["max_hp"] = 'int'  #44 (line in Coconut source)
    current_hp = 0  # type: int  #45 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #45 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #45 (line in Coconut source)
    __annotations__["current_hp"] = 'int'  #45 (line in Coconut source)
    ac = (0, 0, 0)  # type: _coconut.typing.Tuple[int, int, int]  #46 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #46 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #46 (line in Coconut source)
    __annotations__["ac"] = '_coconut.typing.Tuple[int, int, int]'  #46 (line in Coconut source)
    skills = field(default_factory=dict)  # type: dict[str, int]  #47 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #47 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #47 (line in Coconut source)
    __annotations__["skills"] = 'dict[str, int]'  #47 (line in Coconut source)
# TODO
    conditional_skill_modifiers = ()  # type: _coconut.typing.Tuple[str, ...]  #49 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #49 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #49 (line in Coconut source)
    __annotations__["conditional_skill_modifiers"] = '_coconut.typing.Tuple[str, ...]'  #49 (line in Coconut source)
    alignment = ''  # type: str  #50 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #50 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #50 (line in Coconut source)
    __annotations__["alignment"] = 'str'  #50 (line in Coconut source)
    char_classes = ''  # type: _coconut.typing.Tuple[str, ...]  #51 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #51 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #51 (line in Coconut source)
    __annotations__["char_classes"] = '_coconut.typing.Tuple[str, ...]'  #51 (line in Coconut source)
    archetypes = ()  # type: _coconut.typing.Tuple[str, ...]  #52 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #52 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #52 (line in Coconut source)
    __annotations__["archetypes"] = '_coconut.typing.Tuple[str, ...]'  #52 (line in Coconut source)
# TODO: fix vision
# vision: dict[str, int] = field(default_factory=dict)
    movement = (0, 0, 0, 0)  # type: _coconut.typing.Tuple[int, int, int, int]  #55 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #55 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #55 (line in Coconut source)
    __annotations__["movement"] = '_coconut.typing.Tuple[int, int, int, int]'  #55 (line in Coconut source)
    damage_reduction = ()  # type: _coconut.typing.Tuple[str, ...]  #56 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #56 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #56 (line in Coconut source)
    __annotations__["damage_reduction"] = '_coconut.typing.Tuple[str, ...]'  #56 (line in Coconut source)
    stats = (0, 0, 0, 0, 0, 0)  # type: _coconut.typing.Tuple[int, int, int, int, int, int]  #57 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #57 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #57 (line in Coconut source)
    __annotations__["stats"] = '_coconut.typing.Tuple[int, int, int, int, int, int]'  #57 (line in Coconut source)
    base_attack_bonus = ()  # type: _coconut.typing.Tuple[int, ...]  #58 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #58 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #58 (line in Coconut source)
    __annotations__["base_attack_bonus"] = '_coconut.typing.Tuple[int, ...]'  #58 (line in Coconut source)
    saving_throws = (0, 0, 0)  # type: _coconut.typing.Tuple[int, int, int]  #59 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #59 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #59 (line in Coconut source)
    __annotations__["saving_throws"] = '_coconut.typing.Tuple[int, int, int]'  #59 (line in Coconut source)
# TODO
    conditional_st_modifiers = ()  # type: _coconut.typing.Tuple[str, ...]  #61 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #61 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #61 (line in Coconut source)
    __annotations__["conditional_st_modifiers"] = '_coconut.typing.Tuple[str, ...]'  #61 (line in Coconut source)
    melee = ()  # type: _coconut.typing.Tuple[int, ...]  #62 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #62 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #62 (line in Coconut source)
    __annotations__["melee"] = '_coconut.typing.Tuple[int, ...]'  #62 (line in Coconut source)
    ranged = ()  # type: _coconut.typing.Tuple[int, ...]  #63 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #63 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #63 (line in Coconut source)
    __annotations__["ranged"] = '_coconut.typing.Tuple[int, ...]'  #63 (line in Coconut source)
    weapons = field(default_factory=dict)  # type: dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]  #64 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #64 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #64 (line in Coconut source)
    __annotations__["weapons"] = 'dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]'  #64 (line in Coconut source)
    ranged_weapons = field(default_factory=dict)  # type: dict[str, dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]]  #65 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #65 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #65 (line in Coconut source)
    __annotations__["ranged_weapons"] = 'dict[str, dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]]'  #65 (line in Coconut source)
    cmb = ()  # type: dict[str, int]  #66 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #66 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #66 (line in Coconut source)
    __annotations__["cmb"] = 'dict[str, int]'  #66 (line in Coconut source)
    cmd = ()  # type: dict[str, int]  #67 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #67 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #67 (line in Coconut source)
    __annotations__["cmd"] = 'dict[str, int]'  #67 (line in Coconut source)
    spell_resistance = 0  # type: int  #68 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #68 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #68 (line in Coconut source)
    __annotations__["spell_resistance"] = 'int'  #68 (line in Coconut source)
    languages = ()  # type: _coconut.typing.Tuple[str, ...]  #69 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #69 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #69 (line in Coconut source)
    __annotations__["languages"] = '_coconut.typing.Tuple[str, ...]'  #69 (line in Coconut source)
    gold = 0  # type: int  #70 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #70 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #70 (line in Coconut source)
    __annotations__["gold"] = 'int'  #70 (line in Coconut source)
    curr_gold = 0  # type: int  #71 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #71 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #71 (line in Coconut source)
    __annotations__["curr_gold"] = 'int'  #71 (line in Coconut source)
    ac_bonus = 0  # type: int  #72 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #72 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #72 (line in Coconut source)
    __annotations__["ac_bonus"] = 'int'  #72 (line in Coconut source)
    initiative = 0  # type: int  #73 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #73 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #73 (line in Coconut source)
    __annotations__["initiative"] = 'int'  #73 (line in Coconut source)
    resistances = field(default_factory=dict)  # type: _coconut.typing.Tuple[str, ...]  #74 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #74 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #74 (line in Coconut source)
    __annotations__["resistances"] = '_coconut.typing.Tuple[str, ...]'  #74 (line in Coconut source)
    immunities = field(default_factory=dict)  # type: set[str]  #75 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #75 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #75 (line in Coconut source)
    __annotations__["immunities"] = 'set[str]'  #75 (line in Coconut source)
    spells = field(default_factory=list)  # type: list[Spell]  #76 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #76 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #76 (line in Coconut source)
    __annotations__["spells"] = 'list[Spell]'  #76 (line in Coconut source)
    weapon_proficiencies = ''  # type: str  #77 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #77 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #77 (line in Coconut source)
    __annotations__["weapon_proficiencies"] = 'str'  #77 (line in Coconut source)
    feats = ()  # type: _coconut.typing.Tuple[_coconut.typing.Tuple[str, str], ...]  #78 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #78 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #78 (line in Coconut source)
    __annotations__["feats"] = '_coconut.typing.Tuple[_coconut.typing.Tuple[str, str], ...]'  #78 (line in Coconut source)
    spell_like_abilities = ""  # type: str  #79 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #79 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #79 (line in Coconut source)
    __annotations__["spell_like_abilities"] = 'str'  #79 (line in Coconut source)
    special_abilities = ()  # type: _coconut.typing.Tuple[str, ...]  #80 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #80 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #80 (line in Coconut source)
    __annotations__["special_abilities"] = '_coconut.typing.Tuple[str, ...]'  #80 (line in Coconut source)
    special_attacks = ()  # type: _coconut.typing.Tuple[str,]  #81 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #81 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #81 (line in Coconut source)
    __annotations__["special_attacks"] = '_coconut.typing.Tuple[str,]'  #81 (line in Coconut source)

_coconut_call_set_names(Character)  #82 (line in Coconut source)
