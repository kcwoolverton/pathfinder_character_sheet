#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7a7a351b

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

try:  #1 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #1 (line in Coconut source)
except _coconut.NameError:  #1 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #1 (line in Coconut source)
sys = _coconut_sys  #1 (line in Coconut source)
if sys.version_info >= (3, 4):  #1 (line in Coconut source)
    from enum import Enum  #1 (line in Coconut source)
else:  #1 (line in Coconut source)
    from aenum import Enum  #1 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #1 (line in Coconut source)
    sys = _coconut_sys_0  #1 (line in Coconut source)
from dataclasses import dataclass  #2 (line in Coconut source)
from random import Random  #3 (line in Coconut source)

class Stats(Enum):  #5 (line in Coconut source)
    STRENGTH = 0  #6 (line in Coconut source)
    DEXTERITY = 1  #7 (line in Coconut source)
    CONSTITUTION = 2  #8 (line in Coconut source)
    INTELLIGENCE = 3  #9 (line in Coconut source)
    WISDOM = 4  #10 (line in Coconut source)
    CHARISMA = 5  #11 (line in Coconut source)


_coconut_call_set_names(Stats)  #14 (line in Coconut source)
@dataclass  #14 (line in Coconut source)
class ClassInfo(_coconut.object):  #15 (line in Coconut source)
    primary_stats = ()  # type: tuple[Stats, ...]  #16 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #16 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #16 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #16 (line in Coconut source)
    secondary_stats = ()  # type: tuple[Stats, ...]  #17 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #17 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #17 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #17 (line in Coconut source)
    tertiary_stat = None  # type: _coconut.typing.Union[Stats, None]  #18 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #18 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #18 (line in Coconut source)
    __annotations__["tertiary_stat"] = '_coconut.typing.Union[Stats, None]'  #18 (line in Coconut source)
    neutral_stats = ()  # type: tuple[Stats, ...]  #19 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #19 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #19 (line in Coconut source)
    __annotations__["neutral_stats"] = 'tuple[Stats, ...]'  #19 (line in Coconut source)
    dump_stats = ()  # type: tuple[Stats, ...]  #20 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #20 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #20 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #20 (line in Coconut source)


_coconut_call_set_names(ClassInfo)  #23 (line in Coconut source)
@dataclass  #23 (line in Coconut source)
class Wizard(ClassInfo):  #24 (line in Coconut source)
    primary_stats = (Stats.INTELLIGENCE,)  # type: tuple[Stats, ...]  #25 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #25 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #25 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #25 (line in Coconut source)
    secondary_stats = (Stats.DEXTERITY, Stats.CONSTITUTION)  # type: tuple[Stats, ...]  #26 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #26 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #26 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #26 (line in Coconut source)
    tertiary_stat = Stats.WISDOM  # type: Stats  #27 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #27 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #27 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #27 (line in Coconut source)
    dump_stats = (Stats.STRENGTH, Stats.CHARISMA)  # type: tuple[Stats, ...]  #28 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #28 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #28 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #28 (line in Coconut source)

_coconut_call_set_names(Wizard)  #30 (line in Coconut source)
@dataclass  #30 (line in Coconut source)
class Cleric(ClassInfo):  #31 (line in Coconut source)
    primary_stats = (Stats.WISDOM,)  # type: tuple[Stats, ...]  #32 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #32 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #32 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #32 (line in Coconut source)
    secondary_stats = (Stats.DEXTERITY, Stats.CONSTITUTION)  # type: tuple[Stats, ...]  #33 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #33 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #33 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #33 (line in Coconut source)
    tertiary_stat = Stats.CHARISMA  # type: Stats  #34 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #34 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #34 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #34 (line in Coconut source)
    neutral_stats = (Stats.STRENGTH, Stats.INTELLIGENCE)  # type: tuple[Stats, ...]  #35 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #35 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #35 (line in Coconut source)
    __annotations__["neutral_stats"] = 'tuple[Stats, ...]'  #35 (line in Coconut source)
    dump_stats = ()  # type: tuple[Stats, ...]  #36 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #36 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #36 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #36 (line in Coconut source)

_coconut_call_set_names(Cleric)  #38 (line in Coconut source)
@dataclass  #38 (line in Coconut source)
class Fighter(ClassInfo):  #39 (line in Coconut source)
    primary_stats = ()  # type: tuple[Stats, ...]  #40 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #40 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #40 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #40 (line in Coconut source)
    secondary_stats = (Stats.STRENGTH, Stats.DEXTERITY)  # type: tuple[Stats, ...]  #41 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #41 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #41 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #41 (line in Coconut source)
    tertiary_stat = Stats.CONSTITUTION  # type: Stats  #42 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #42 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #42 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #42 (line in Coconut source)
    neutral_stats = (Stats.INTELLIGENCE, Stats.WISDOM)  # type: tuple[Stats, ...]  #43 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #43 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #43 (line in Coconut source)
    __annotations__["neutral_stats"] = 'tuple[Stats, ...]'  #43 (line in Coconut source)
    dump_stats = (Stats.CHARISMA,)  # type: tuple[Stats, ...]  #44 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #44 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #44 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #44 (line in Coconut source)

_coconut_call_set_names(Fighter)  #46 (line in Coconut source)
@dataclass  #46 (line in Coconut source)
class Sorcerer(ClassInfo):  #47 (line in Coconut source)
    primary_stats = (Stats.CHARISMA,)  # type: tuple[Stats, ...]  #48 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #48 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #48 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #48 (line in Coconut source)
    secondary_stats = (Stats.DEXTERITY, Stats.CONSTITUTION)  # type: tuple[Stats, ...]  #49 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #49 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #49 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #49 (line in Coconut source)
    tertiary_stat = Stats.INTELLIGENCE  # type: Stats  #50 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #50 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #50 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #50 (line in Coconut source)
    dump_stats = (Stats.STRENGTH, Stats.WISDOM, Stats.INTELLIGENCE)  # type: tuple[Stats, ...]  #51 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #51 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #51 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #51 (line in Coconut source)

_coconut_call_set_names(Sorcerer)  #53 (line in Coconut source)
@dataclass  #53 (line in Coconut source)
class Rogue(ClassInfo):  #54 (line in Coconut source)
    primary_stats = (Stats.DEXTERITY,)  # type: tuple[Stats, ...]  #55 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #55 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #55 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #55 (line in Coconut source)
    secondary_stats = (Stats.STRENGTH, Stats.CONSTITUTION)  # type: tuple[Stats, ...]  #56 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #56 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #56 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #56 (line in Coconut source)
    tertiary_stat = Stats.WISDOM  # type: Stats  #57 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #57 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #57 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #57 (line in Coconut source)
    dump_stats = (Stats.CHARISMA, Stats.INTELLIGENCE)  # type: tuple[Stats, ...]  #58 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #58 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #58 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #58 (line in Coconut source)

_coconut_call_set_names(Rogue)  #60 (line in Coconut source)
@dataclass  #60 (line in Coconut source)
class Paladin(ClassInfo):  #61 (line in Coconut source)
    primary_stats = ()  # type: tuple[Stats, ...]  #62 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #62 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #62 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #62 (line in Coconut source)
    secondary_stats = (Stats.STRENGTH, Stats.CHARISMA)  # type: tuple[Stats, ...]  #63 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #63 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #63 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #63 (line in Coconut source)
    tertiary_stat = Stats.CONSTITUTION  # type: Stats  #64 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #64 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #64 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #64 (line in Coconut source)
    neutral_stats = (Stats.DEXTERITY,)  # type: tuple[Stats, ...]  #65 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #65 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #65 (line in Coconut source)
    __annotations__["neutral_stats"] = 'tuple[Stats, ...]'  #65 (line in Coconut source)
    dump_stats = (Stats.INTELLIGENCE, Stats.WISDOM)  # type: tuple[Stats, ...]  #66 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #66 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #66 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #66 (line in Coconut source)

_coconut_call_set_names(Paladin)  #68 (line in Coconut source)
@dataclass  #68 (line in Coconut source)
class Alchemist(ClassInfo):  #69 (line in Coconut source)
    primary_stats = (Stats.INTELLIGENCE,)  # type: tuple[Stats, ...]  #70 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #70 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #70 (line in Coconut source)
    __annotations__["primary_stats"] = 'tuple[Stats, ...]'  #70 (line in Coconut source)
    secondary_stats = (Stats.DEXTERITY,)  # type: tuple[Stats, ...]  #71 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #71 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #71 (line in Coconut source)
    __annotations__["secondary_stats"] = 'tuple[Stats, ...]'  #71 (line in Coconut source)
    tertiary_stat = Stats.CONSTITUTION  # type: Stats  #72 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #72 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #72 (line in Coconut source)
    __annotations__["tertiary_stat"] = 'Stats'  #72 (line in Coconut source)
    neutral_stats = (Stats.STRENGTH, Stats.WISDOM)  # type: tuple[Stats, ...]  #73 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #73 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #73 (line in Coconut source)
    __annotations__["neutral_stats"] = 'tuple[Stats, ...]'  #73 (line in Coconut source)
    dump_stats = (Stats.CHARISMA,)  # type: tuple[Stats, ...]  #74 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #74 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #74 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #74 (line in Coconut source)


_coconut_call_set_names(Alchemist)  #77 (line in Coconut source)
@dataclass  #77 (line in Coconut source)
class CharStats(_coconut.object):  #78 (line in Coconut source)
    strength = 10  # type: int  #79 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #79 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #79 (line in Coconut source)
    __annotations__["strength"] = 'int'  #79 (line in Coconut source)
    dexterity = 10  # type: int  #80 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #80 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #80 (line in Coconut source)
    __annotations__["dexterity"] = 'int'  #80 (line in Coconut source)
    constitution = 10  # type: int  #81 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #81 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #81 (line in Coconut source)
    __annotations__["constitution"] = 'int'  #81 (line in Coconut source)
    intelligence = 10  # type: int  #82 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #82 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #82 (line in Coconut source)
    __annotations__["intelligence"] = 'int'  #82 (line in Coconut source)
    wisdom = 10  # type: int  #83 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #83 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #83 (line in Coconut source)
    __annotations__["wisdom"] = 'int'  #83 (line in Coconut source)
    charisma = 10  # type: int  #84 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #84 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #84 (line in Coconut source)
    __annotations__["charisma"] = 'int'  #84 (line in Coconut source)

    def get_stats_tuple(self):  #86 (line in Coconut source)
        return (self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)  #87 (line in Coconut source)

# type: ignore
_coconut_call_set_names(CharStats)  # type: ignore  #89 (line in Coconut source)
@_coconut_tco  # type: ignore  #89 (line in Coconut source)
def roll_4d6(rng  # type: Random  # type: ignore  #89 (line in Coconut source)
    ):  # type: ignore  #89 (line in Coconut source)
# type: (...) -> int  # type: ignore
    return _coconut_tail_call((sum), ((sorted)((map)(lambda _=None: rng.randint(1, 6), range(4))))[_coconut.slice(1, None)])  # type: ignore  #89 (line in Coconut source)


def cost_to_add(curr_val  # type: int  #97 (line in Coconut source)
    ):  #97 (line in Coconut source)
# type: (...) -> int
# TODO: Surely there is a better formula
    if curr_val == 9 or curr_val == 10:  #99 (line in Coconut source)
        return 1  #100 (line in Coconut source)
    return abs(curr_val - 9) // 2 + (curr_val < 10)  #101 (line in Coconut source)


def get_gained_points(stats):  #103 (line in Coconut source)
    num_points_gained_per_stat = 0  #104 (line in Coconut source)
    for stat in stats:  #105 (line in Coconut source)
        while stat < 10:  #106 (line in Coconut source)
            num_points_gained_per_stat += cost_to_add(stat)  #107 (line in Coconut source)
            stat += 1  #108 (line in Coconut source)
    return num_points_gained_per_stat  #109 (line in Coconut source)


@_coconut_tco  #111 (line in Coconut source)
def point_buy_from_floor_stats(points,  # type: int  #111 (line in Coconut source)
    floor_stat,  # type: int  #111 (line in Coconut source)
    rng  # type: Random  #111 (line in Coconut source)
    ):  #111 (line in Coconut source)
# type: (...) -> CharStats
    stats = [floor_stat,] * 6  #112 (line in Coconut source)
    points += get_gained_points(stats)  #113 (line in Coconut source)
    full_stats = set()  # type: set[int]  #114 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #114 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #114 (line in Coconut source)
    __annotations__["full_stats"] = 'set[int]'  #114 (line in Coconut source)
    while len(full_stats) < 6:  #115 (line in Coconut source)
        print(stats)  #116 (line in Coconut source)
        stat_to_increase = rng.randint(0, 5)  #117 (line in Coconut source)
        cost = cost_to_add(stats[stat_to_increase])  #118 (line in Coconut source)
        if cost > points:  #119 (line in Coconut source)
            full_stats.add(stat_to_increase)  #120 (line in Coconut source)
            continue  #121 (line in Coconut source)
        print(points)  #122 (line in Coconut source)
        points -= cost  #123 (line in Coconut source)
        print(cost)  #124 (line in Coconut source)
        stats[stat_to_increase] += 1  #125 (line in Coconut source)
    return _coconut_tail_call(CharStats, *stats)  #126 (line in Coconut source)



@_coconut_tco  #129 (line in Coconut source)
def point_buy_for_class(points,  # type: int  #129 (line in Coconut source)
    class_info,  # type: ClassInfo  #129 (line in Coconut source)
    floor_stat=7, max_buy=18):  #129 (line in Coconut source)
# type: (...) -> CharStats
    stats = [10,] * 6  #130 (line in Coconut source)

# Dump relevant stats
    dump_stats = class_info.dump_stats  # type: tuple[Stats, ...]  #133 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #133 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #133 (line in Coconut source)
    __annotations__["dump_stats"] = 'tuple[Stats, ...]'  #133 (line in Coconut source)
    for stat in dump_stats:  #134 (line in Coconut source)
        stats[stat.value] = floor_stat  #135 (line in Coconut source)

# Determine point count
    points += get_gained_points(stats)  #138 (line in Coconut source)

# Put max points in primary stats
    primary_stats = class_info.primary_stats  #141 (line in Coconut source)
    for stat in primary_stats:  #142 (line in Coconut source)
        while stats[stat.value] < max_buy:  #143 (line in Coconut source)
            cost = cost_to_add(stats[stat.value])  #144 (line in Coconut source)
            if cost > points:  #145 (line in Coconut source)
                break  #146 (line in Coconut source)
            points -= cost  #147 (line in Coconut source)
            stats[stat.value] += 1  #148 (line in Coconut source)

# Put points in secondary stats (two at a time, even is good). Inherently preferences Stats earlier in the list.
    secondary_stats = class_info.secondary_stats  #151 (line in Coconut source)
    points_remain = True  #152 (line in Coconut source)
    maxxed_stats = set()  # type: set[int]  #153 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #153 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #153 (line in Coconut source)
    __annotations__["maxxed_stats"] = 'set[int]'  #153 (line in Coconut source)
    while points_remain:  #154 (line in Coconut source)
        if len(maxxed_stats) == len(secondary_stats):  #155 (line in Coconut source)
            break  #156 (line in Coconut source)

        for stat in secondary_stats:  #158 (line in Coconut source)
            if len(maxxed_stats) == len(secondary_stats):  #159 (line in Coconut source)
                break  #160 (line in Coconut source)
            cost = cost_to_add(stats[stat.value]) + cost_to_add(stats[stat.value] + 1)  #161 (line in Coconut source)
            if cost > points:  #162 (line in Coconut source)
                points_remain = False  #163 (line in Coconut source)
                break  #164 (line in Coconut source)
            if stats[stat.value] >= max_buy:  #165 (line in Coconut source)
                maxxed_stats.add(stat.value)  #166 (line in Coconut source)
                continue  #167 (line in Coconut source)
            points -= cost  #168 (line in Coconut source)
            stats[stat.value] += 2  #169 (line in Coconut source)

# Put remaining points in tertiary skill
    tertiary_stat = class_info.tertiary_stat  #172 (line in Coconut source)
    if tertiary_stat:  #173 (line in Coconut source)
        while True:  #174 (line in Coconut source)
            cost = cost_to_add(stats[tertiary_stat.value])  #175 (line in Coconut source)
            if cost > points:  #176 (line in Coconut source)
                break  #177 (line in Coconut source)
            points -= cost  #178 (line in Coconut source)
            stats[tertiary_stat.value] += 1  #179 (line in Coconut source)

    return _coconut_tail_call(CharStats, *stats)  #181 (line in Coconut source)



@_coconut_tco  #184 (line in Coconut source)
def pathfinder_stats_roll(rng  # type: Random  #184 (line in Coconut source)
    ):  #184 (line in Coconut source)
# type: (...) -> CharStats
    return _coconut_tail_call(CharStats, *(roll_4d6(rng) for _ in range(6)))  #185 (line in Coconut source)


@_coconut_tco  #187 (line in Coconut source)
def pathfinder_stats_roll_for_class(class_info,  # type: ClassInfo  #187 (line in Coconut source)
    rng  # type: Random  #187 (line in Coconut source)
    ):  #187 (line in Coconut source)
# type: (...) -> CharStats
    rolls = sorted([roll_4d6(rng) for _ in range(6)], reverse=True)  #188 (line in Coconut source)
    stats = [None,] * 6  #189 (line in Coconut source)
    for stat in class_info.dump_stats:  #190 (line in Coconut source)
        stats[stat.value] = rolls.pop()  #191 (line in Coconut source)

    if class_info.tertiary_stat not in class_info.dump_stats and class_info.tertiary_stat not in class_info.secondary_stats:  #193 (line in Coconut source)
        stats[class_info.tertiary_stat.value] = rolls.pop()  #194 (line in Coconut source)

    for stat in _coconut_flatten(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: reversed(class_info.secondary_stats), lambda: reversed(class_info.primary_stats)))):  #196 (line in Coconut source)
        stats[stat.value] = rolls.pop()  #197 (line in Coconut source)

    return _coconut_tail_call(CharStats, *stats)  #199 (line in Coconut source)



@_coconut_tco  #202 (line in Coconut source)
def add_racial_stat_bonuses(stats,  # type: tuple[int, ...]  #202 (line in Coconut source)
    racial_bonuses  # type: tuple[int, ...]  #202 (line in Coconut source)
    ):  #202 (line in Coconut source)
    return _coconut_tail_call((tuple), map((_coconut.operator.add), stats, racial_bonuses, strict=True))  #202 (line in Coconut source)


def get_stat_modifier(stat_value):  #206 (line in Coconut source)
    return (stat_value - 10) // 2  #207 (line in Coconut source)


@dataclass  #209 (line in Coconut source)
class CharRace(_coconut.object):  #210 (line in Coconut source)
    name = ''  # type: str  #211 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #211 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #211 (line in Coconut source)
    __annotations__["name"] = 'str'  #211 (line in Coconut source)
    stat_modifiers = (0, 0, 0, 0, 0, 0)  # type: tuple[int]  #212 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #212 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #212 (line in Coconut source)
    __annotations__["stat_modifiers"] = 'tuple[int]'  #212 (line in Coconut source)

_coconut_call_set_names(CharRace)  #214 (line in Coconut source)
class HesperianDevil(_coconut.object):  #214 (line in Coconut source)
    name = 'Hesperian Devil'  # type: str  #215 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #215 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #215 (line in Coconut source)
    __annotations__["name"] = 'str'  #215 (line in Coconut source)
    stat_modifiers = (2, 0, 0, 4, 2, 4)  # type: tuple[int]  #216 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #216 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #216 (line in Coconut source)
    __annotations__["stat_modifiers"] = 'tuple[int]'  #216 (line in Coconut source)

_coconut_call_set_names(HesperianDevil)  #218 (line in Coconut source)
@dataclass  #218 (line in Coconut source)
class Character(_coconut.object):  #219 (line in Coconut source)
    char_class = ClassInfo()  # type: ClassInfo  #220 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #220 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #220 (line in Coconut source)
    __annotations__["char_class"] = 'ClassInfo'  #220 (line in Coconut source)
    char_stats = CharStats()  # type: CharStats  #221 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #221 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #221 (line in Coconut source)
    __annotations__["char_stats"] = 'CharStats'  #221 (line in Coconut source)
    char_level = 1  # type: int  #222 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #222 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #222 (line in Coconut source)
    __annotations__["char_level"] = 'int'  #222 (line in Coconut source)
    char_race = CharRace()  # type: CharRace  #223 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #223 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #223 (line in Coconut source)
    __annotations__["char_race"] = 'CharRace'  #223 (line in Coconut source)

    @property  #225 (line in Coconut source)
    def armor_class(self):  #226 (line in Coconut source)
        return (get_stat_modifier(self.char_stats.dexterity) + 10, get_stat_modifier(self.char_stats.dexterity) + 10, 10)  #227 (line in Coconut source)


    def generate_stats(self, optimize=False,  # type: bool  #229 (line in Coconut source)
        point_buy=0,  # type: int  #229 (line in Coconut source)
        floor_stat=7,  # type: int  #229 (line in Coconut source)
        max_buy=18,  # type: int  #229 (line in Coconut source)
        random=True,):  #229 (line in Coconut source)
# type: (...) -> None
        if point_buy < 0:  #237 (line in Coconut source)
            raise ValueError("Point buy must be greater than or equal to 0.")  #238 (line in Coconut source)

        if random:  #240 (line in Coconut source)
            rng = Random()  #241 (line in Coconut source)
        else:  #242 (line in Coconut source)
            rng = Random(1)  #243 (line in Coconut source)

        if optimize:  #245 (line in Coconut source)
            if point_buy == 0:  #246 (line in Coconut source)
                self.char_stats = add_racial_stat_bonuses(pathfinder_stats_roll_for_class(self.char_class, rng).get_stats_tuple(), self.char_race.stat_modifiers)  #247 (line in Coconut source)
            else:  #251 (line in Coconut source)
                self.char_stats = add_racial_stat_bonuses(point_buy_for_class(point_buy, self.char_class, floor_stat, max_buy).get_stats_tuple(), self.char_race.stat_modifiers)  #252 (line in Coconut source)
        elif point_buy > 0:  #256 (line in Coconut source)
            self.char_stats = add_racial_stat_bonuses(point_buy_from_floor_stats(point_buy, floor_stat, rng).get_stats_tuple(), self.char_race.stat_modifiers)  #257 (line in Coconut source)
        else:  #261 (line in Coconut source)
            self.char_stats = add_racial_stat_bonuses(pathfinder_stats_roll(rng).get_stats_tuple(), self.char_race.stat_modifiers)  #262 (line in Coconut source)


_coconut_call_set_names(Character)  #267 (line in Coconut source)
