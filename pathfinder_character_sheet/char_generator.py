#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x72cad5a5

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

from enum import Enum  #1 (line in Coconut source)
from dataclasses import dataclass  #2 (line in Coconut source)
from random import Random  #3 (line in Coconut source)

class Stats(Enum):  #5 (line in Coconut source)
    STRENGTH = 0  #6 (line in Coconut source)
    DEXTERITY = 1  #7 (line in Coconut source)
    CONSTITUTION = 2  #8 (line in Coconut source)
    INTELLIGENCE = 3  #9 (line in Coconut source)
    WISDOM = 4  #10 (line in Coconut source)
    CHARISMA = 5  #11 (line in Coconut source)


@dataclass  #14 (line in Coconut source)
class ClassInfo():  #15 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = ()  #16 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = ()  #17 (line in Coconut source)
    tertiary_stat: Stats | None = None  #18 (line in Coconut source)
    neutral_stats: tuple[Stats, ...] = ()  #19 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = ()  #20 (line in Coconut source)


@dataclass  #23 (line in Coconut source)
class Wizard(ClassInfo):  #24 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = (Stats.INTELLIGENCE,)  #25 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.DEXTERITY, Stats.CONSTITUTION)  #26 (line in Coconut source)
    tertiary_stat: Stats = Stats.WISDOM  #27 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.CHARISMA)  #28 (line in Coconut source)

@dataclass  #30 (line in Coconut source)
class Cleric(ClassInfo):  #31 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = (Stats.WISDOM,)  #32 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.DEXTERITY, Stats.CONSTITUTION)  #33 (line in Coconut source)
    tertiary_stat: Stats = Stats.CHARISMA  #34 (line in Coconut source)
    neutral_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.INTELLIGENCE)  #35 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = ()  #36 (line in Coconut source)

@dataclass  #38 (line in Coconut source)
class Fighter(ClassInfo):  #39 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = ()  #40 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.DEXTERITY)  #41 (line in Coconut source)
    tertiary_stat: Stats = Stats.CONSTITUTION  #42 (line in Coconut source)
    neutral_stats: tuple[Stats, ...] = (Stats.INTELLIGENCE, Stats.WISDOM)  #43 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.CHARISMA,)  #44 (line in Coconut source)

@dataclass  #46 (line in Coconut source)
class Sorcerer(ClassInfo):  #47 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = (Stats.CHARISMA,)  #48 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.DEXTERITY, Stats.CONSTITUTION)  #49 (line in Coconut source)
    tertiary_stat: Stats = Stats.INTELLIGENCE  #50 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.WISDOM, Stats.INTELLIGENCE)  #51 (line in Coconut source)

@dataclass  #53 (line in Coconut source)
class Rogue(ClassInfo):  #54 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = (Stats.DEXTERITY,)  #55 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.CONSTITUTION)  #56 (line in Coconut source)
    tertiary_stat: Stats = Stats.WISDOM  #57 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.CHARISMA, Stats.INTELLIGENCE)  #58 (line in Coconut source)

@dataclass  #60 (line in Coconut source)
class Paladin(ClassInfo):  #61 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = ()  #62 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.CHARISMA)  #63 (line in Coconut source)
    tertiary_stat: Stats = Stats.CONSTITUTION  #64 (line in Coconut source)
    neutral_stats: tuple[Stats, ...] = (Stats.DEXTERITY,)  #65 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.INTELLIGENCE, Stats.WISDOM)  #66 (line in Coconut source)

@dataclass  #68 (line in Coconut source)
class Alchemist(ClassInfo):  #69 (line in Coconut source)
    primary_stats: tuple[Stats, ...] = (Stats.INTELLIGENCE,)  #70 (line in Coconut source)
    secondary_stats: tuple[Stats, ...] = (Stats.DEXTERITY,)  #71 (line in Coconut source)
    tertiary_stat: Stats = Stats.CONSTITUTION  #72 (line in Coconut source)
    neutral_stats: tuple[Stats, ...] = (Stats.STRENGTH, Stats.WISDOM)  #73 (line in Coconut source)
    dump_stats: tuple[Stats, ...] = (Stats.CHARISMA,)  #74 (line in Coconut source)


@dataclass  #77 (line in Coconut source)
class CharStats():  #78 (line in Coconut source)
    strength: int = 10  #79 (line in Coconut source)
    dexterity: int = 10  #80 (line in Coconut source)
    constitution: int = 10  #81 (line in Coconut source)
    intelligence: int = 10  #82 (line in Coconut source)
    wisdom: int = 10  #83 (line in Coconut source)
    charisma: int = 10  #84 (line in Coconut source)

    def get_stats_tuple(self):  #86 (line in Coconut source)
        return (self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)  #87 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #89 (line in Coconut source)
def roll_4d6(rng: Random) -> int:  # type: ignore  #89 (line in Coconut source)
    return _coconut_tail_call((sum), ((sorted)((map)(lambda _=None: rng.randint(1, 6), range(4))))[_coconut.slice(1, None)])  # type: ignore  #89 (line in Coconut source)


def cost_to_add(curr_val: int) -> int:  #97 (line in Coconut source)
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
def point_buy_from_floor_stats(points: int, floor_stat: int, rng: Random) -> CharStats:  #111 (line in Coconut source)
    stats = [floor_stat,] * 6  #112 (line in Coconut source)
    points += get_gained_points(stats)  #113 (line in Coconut source)
    full_stats: set[int] = set()  #114 (line in Coconut source)
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
def point_buy_for_class(points: int, class_info: ClassInfo, floor_stat=7, max_buy=18) -> CharStats:  #129 (line in Coconut source)
    stats = [10,] * 6  #130 (line in Coconut source)

# Dump relevant stats
    dump_stats: tuple[Stats, ...] = class_info.dump_stats  #133 (line in Coconut source)
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
    maxxed_stats: set[int] = set()  #153 (line in Coconut source)
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
def pathfinder_stats_roll(rng: Random) -> CharStats:  #184 (line in Coconut source)
    return _coconut_tail_call(CharStats, *(roll_4d6(rng) for _ in range(6)))  #185 (line in Coconut source)


@_coconut_tco  #187 (line in Coconut source)
def pathfinder_stats_roll_for_class(class_info: ClassInfo, rng: Random) -> CharStats:  #187 (line in Coconut source)
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
def add_racial_stat_bonuses(stats: tuple[int, ...], racial_bonuses: tuple[int, ...]):  #202 (line in Coconut source)
    return _coconut_tail_call((tuple), map((_coconut.operator.add), stats, racial_bonuses, strict=True))  #202 (line in Coconut source)


def get_stat_modifier(stat_value):  #206 (line in Coconut source)
    return (stat_value - 10) // 2  #207 (line in Coconut source)


@dataclass  #209 (line in Coconut source)
class CharRace():  #210 (line in Coconut source)
    name: str = ''  #211 (line in Coconut source)
    stat_modifiers: tuple[int] = (0, 0, 0, 0, 0, 0)  #212 (line in Coconut source)

class HesperianDevil():  #214 (line in Coconut source)
    name: str = 'Hesperian Devil'  #215 (line in Coconut source)
    stat_modifiers: tuple[int] = (2, 0, 0, 4, 2, 4)  #216 (line in Coconut source)

@dataclass  #218 (line in Coconut source)
class Character():  #219 (line in Coconut source)
    char_class: ClassInfo = ClassInfo()  #220 (line in Coconut source)
    char_stats: CharStats = CharStats()  #221 (line in Coconut source)
    char_level: int = 1  #222 (line in Coconut source)
    char_race: CharRace = CharRace()  #223 (line in Coconut source)

    @property  #225 (line in Coconut source)
    def armor_class(self):  #226 (line in Coconut source)
        return (get_stat_modifier(self.char_stats.dexterity) + 10, get_stat_modifier(self.char_stats.dexterity) + 10, 10)  #227 (line in Coconut source)


    def generate_stats(self, optimize: bool=False, point_buy: int=0, floor_stat: int=7, max_buy: int=18, random=True,) -> None:  #229 (line in Coconut source)
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
