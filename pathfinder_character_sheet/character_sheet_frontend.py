#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x81535b2d

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
from random import Random  #2 (line in Coconut source)

import justpy as jp  #4 (line in Coconut source)
from pathfinder_character_sheet.character_sheet_parser import *  #5 (line in Coconut source)
from pathfinder_character_sheet.character import *  #6 (line in Coconut source)
from pathfinder_character_sheet.utils import *  #7 (line in Coconut source)
from pathfinder_character_sheet.styles import *  #8 (line in Coconut source)

# Fix vision
# Make look not bad
# Readme

def make_table(headers, classes=table_classes):  #14 (line in Coconut source)
    table = jp.Table(classes=classes, style=table_style)  #15 (line in Coconut source)

    table_header = jp.Thead(classes=header_row_classes)  #17 (line in Coconut source)
    table.add(table_header)  #18 (line in Coconut source)
    header_row = jp.Tr()  #19 (line in Coconut source)
    table_header.add(header_row)  #20 (line in Coconut source)

    for header in headers:  #22 (line in Coconut source)
        th = jp.Th(classes=header_cell_classes, text=header)  #23 (line in Coconut source)
        header_row.add(th)  #24 (line in Coconut source)

# Table body
    table_body = jp.Tbody()  #27 (line in Coconut source)
    table.add(table_body)  #28 (line in Coconut source)

    return table, table_body  #30 (line in Coconut source)


def make_cell_style_class():  #32 (line in Coconut source)
    return cell_classes  #33 (line in Coconut source)


@_coconut_tco  #35 (line in Coconut source)
def make_button_div():  #35 (line in Coconut source)
    return _coconut_tail_call(jp.Td, classes=make_cell_style_class(), style=cell_style)  #36 (line in Coconut source)


@_coconut_tco  #38 (line in Coconut source)
def make_cell_div(text):  #38 (line in Coconut source)
    return _coconut_tail_call(jp.Td, classes=make_cell_style_class(), style=cell_style, inner_html=text)  #39 (line in Coconut source)


@_coconut_tco  #41 (line in Coconut source)
def make_row_flex_div():  #41 (line in Coconut source)
    return _coconut_tail_call(jp.Div, classes=flex_row_classes, style=flex_row_style)  #42 (line in Coconut source)


@_coconut_tco  #44 (line in Coconut source)
def make_one_third_col_div():  #44 (line in Coconut source)
    return _coconut_tail_call(jp.Div, classes=one_third_col_classes)  #45 (line in Coconut source)


def long_rest_click(self, msg, char):  #47 (line in Coconut source)
    for checkbox in self.checkboxes:  #48 (line in Coconut source)
        checkbox.checked = False  #49 (line in Coconut source)
    self.hp_input.value = "{_coconut_format_0}".format(_coconut_format_0=(char.max_hp))  #50 (line in Coconut source)


def make_checkbox_cell(reset_button, num_checkboxes):  #52 (line in Coconut source)
    checkbox_div = jp.Div(classes=checkbox_div_classes, style=checkbox_div_style)  #53 (line in Coconut source)
    if num_checkboxes == "At Will":  #54 (line in Coconut source)
        return checkbox_div, None  #55 (line in Coconut source)
    for i in range(int(num_checkboxes)):  #56 (line in Coconut source)
        checkbox = jp.Input(type="checkbox", classes=checkbox_classes, style=checkbox_style, checked=False)  #57 (line in Coconut source)
        reset_button.checkboxes.append(checkbox)  #58 (line in Coconut source)
        checkbox_div.add(checkbox)  #59 (line in Coconut source)
    return checkbox_div, reset_button  #60 (line in Coconut source)


def make_title_row(char, reset_button, history_box):  #62 (line in Coconut source)
    title_row = make_row_flex_div()  #63 (line in Coconut source)
    name_box = make_title_box("50px", "1/8", char.name)  #64 (line in Coconut source)
    class_str = "{_coconut_format_0}".format(_coconut_format_0=(', '.join(char.char_classes)))  #65 (line in Coconut source)
    if char.archetypes:  #66 (line in Coconut source)
        class_str += ": " + ", ".join(char.archetypes)  #67 (line in Coconut source)
    class_box = make_title_box("50px", "1/4", class_str)  #68 (line in Coconut source)
    level_box = make_title_box("50px", "1/8", "Level " + str(char.level))  #69 (line in Coconut source)
    title_row.add(name_box, class_box, level_box)  #70 (line in Coconut source)
    title_row.add(reset_button)  #71 (line in Coconut source)
    title_row.add(history_box)  #72 (line in Coconut source)
    return title_row  #73 (line in Coconut source)


def make_ac_cell(char):  #75 (line in Coconut source)
    table, table_body = make_table([], ac_classes)  #76 (line in Coconut source)

    total_data = make_cell_div(text="Total: {_coconut_format_0}".format(_coconut_format_0=(char.ac.total)))  #78 (line in Coconut source)
    touch_data = make_cell_div(text="Touch: {_coconut_format_0}".format(_coconut_format_0=(char.ac.touch)))  #79 (line in Coconut source)
    flat_data = make_cell_div(text="Flat: {_coconut_format_0}".format(_coconut_format_0=(char.ac.flat)))  #80 (line in Coconut source)

    table_row = jp.Tr()  #82 (line in Coconut source)
    table_row.add(total_data, touch_data, flat_data)  #83 (line in Coconut source)

    table_body.add(table_row)  #85 (line in Coconut source)

    return table  #87 (line in Coconut source)


def make_useful_info_row(upper_container, reset_button, char, rng, history_box):  #89 (line in Coconut source)
    useful_info_row = make_col_flex_div()  #90 (line in Coconut source)

    headers = ["Hit Points", "Initiative", "Armor Class"]  #92 (line in Coconut source)
    if char.immunities:  #93 (line in Coconut source)
        headers.append("Immunities")  #94 (line in Coconut source)
    if char.resistances:  #95 (line in Coconut source)
        headers.append("Resistances")  #96 (line in Coconut source)
    if char.damage_reduction:  #97 (line in Coconut source)
        headers.append("Dmg Reduction")  #98 (line in Coconut source)
    table, table_body = make_table(headers)  #99 (line in Coconut source)
    useful_info_row.add(table)  #100 (line in Coconut source)

    hit_points_data = jp.Input(type='number', classes=hit_points_classes, style=hit_points_style, min="-{_coconut_format_0}".format(_coconut_format_0=(char.max_hp)), value="{_coconut_format_0}".format(_coconut_format_0=(char.max_hp)))  #102 (line in Coconut source)
    reset_button.hp_input = hit_points_data  #109 (line in Coconut source)
    roll_modal = make_roll_modal(upper_container, modifier=[char.initiative,], rng=rng, history_box=history_box)  #110 (line in Coconut source)
    initiative_data = make_roll_cell(rng, roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[char.initiative,], roll_type='Initiative'), text=make_mod_text([char.initiative,]))  #111 (line in Coconut source)
# ac_data = make_ac_cell(char)
    ac_data = make_cell_div(text="Total: {_coconut_format_0}   |   Touch: {_coconut_format_1}   |   Flat: {_coconut_format_2}".format(_coconut_format_0=(char.ac.total), _coconut_format_1=(char.ac.touch), _coconut_format_2=(char.ac.flat)))  #117 (line in Coconut source)

    table_row = jp.Tr()  #119 (line in Coconut source)
    table_body.add(table_row)  #120 (line in Coconut source)

    table_row.add(hit_points_data, initiative_data, ac_data)  #122 (line in Coconut source)
    if char.immunities:  #123 (line in Coconut source)
        immunity_data = make_cell_div(text="<br>".join(char.immunities))  #124 (line in Coconut source)
        table_row.add(immunity_data)  #125 (line in Coconut source)
    if char.resistances:  #126 (line in Coconut source)
        resistance_data = make_cell_div(text="<br>".join(char.resistances))  #127 (line in Coconut source)
        table_row.add(resistance_data)  #128 (line in Coconut source)
    if char.damage_reduction:  #129 (line in Coconut source)
        reduction_data = make_cell_div(text="<br>".join(char.damage_reduction))  #130 (line in Coconut source)
        table_row.add(reduction_data)  #131 (line in Coconut source)
    return useful_info_row  #132 (line in Coconut source)


def make_abilities_box(upper_container, char, rng, history_box):  #134 (line in Coconut source)
    ability_row = make_col_flex_div()  #135 (line in Coconut source)

    table, table_body = make_table(["Ability", "Score", "Modifier"])  #137 (line in Coconut source)
    ability_row.add(table)  #138 (line in Coconut source)

    for ability in Stats:  #140 (line in Coconut source)
        table_row = jp.Tr()  #141 (line in Coconut source)
        table_body.add(table_row)  #142 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[get_stat_modifier(char.stats[ability.value]),], rng=rng, history_box=history_box)  #143 (line in Coconut source)
        ability_name = make_roll_cell(rng, roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[get_stat_modifier(char.stats[ability.value]),], roll_type=ability.name), text=ability.name)  #149 (line in Coconut source)
        table_row.add(ability_name)  #154 (line in Coconut source)
        score = make_cell_div(text=str(char.stats[ability.value]))  #155 (line in Coconut source)
        table_row.add(score)  #156 (line in Coconut source)
        modifier = make_cell_div(text=make_mod_text([get_stat_modifier(char.stats[ability.value]),]))  #157 (line in Coconut source)
        table_row.add(modifier)  #158 (line in Coconut source)
    return ability_row  #159 (line in Coconut source)


def make_base_attack_box(upper_container, char, rng, history_box):  #161 (line in Coconut source)
    attack_row = make_col_flex_div()  #162 (line in Coconut source)
    table, table_body = make_table(["Base Attack", "Attack Bonus"])  #163 (line in Coconut source)
    attack_row.add(table)  #164 (line in Coconut source)

    melee_row = jp.Tr()  #166 (line in Coconut source)
    table_body.add(melee_row)  #167 (line in Coconut source)

    melee_modal = make_roll_modal(upper_container, modifier=char.melee, rng=rng, history_box=history_box)  #169 (line in Coconut source)
    melee_button = make_roll_cell(rng, melee_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=char.melee, roll_type="Base Melee"), text="Melee")  #170 (line in Coconut source)
    melee_row.add(melee_button)  #175 (line in Coconut source)
    melee_row.add(make_cell_div(text=make_mod_text(char.melee)))  #176 (line in Coconut source)

    ranged_row = jp.Tr()  #178 (line in Coconut source)
    table_body.add(ranged_row)  #179 (line in Coconut source)

    ranged_modal = make_roll_modal(upper_container, modifier=char.ranged, rng=rng, history_box=history_box)  #181 (line in Coconut source)
    ranged_button = make_roll_cell(rng, ranged_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=char.ranged, roll_type="Base Ranged"), text="Ranged")  #182 (line in Coconut source)
    ranged_row.add(ranged_button)  #187 (line in Coconut source)
    ranged_row.add(make_cell_div(text=make_mod_text(char.ranged)))  #188 (line in Coconut source)

    return attack_row  #190 (line in Coconut source)


def make_weapons_box(upper_container, char, rng, history_box):  #192 (line in Coconut source)
# type: (...) -> dict[str, (_coconut.typing.Tuple[(_coconut.typing.Tuple[int, ...]), str, str])]
    weapons_row = make_col_flex_div()  #193 (line in Coconut source)

    table, table_body = make_table(["Weapon", "Attack Bonus", "Damage", "Crit Multiplier"])  #195 (line in Coconut source)
    weapons_row.add(table)  #196 (line in Coconut source)

    for weapon, (attack_bonus, damage, multiplier) in char.weapons.items():  #198 (line in Coconut source)
        table_row = jp.Tr()  #199 (line in Coconut source)
        table_body.add(table_row)  #200 (line in Coconut source)
        num_dice, die, modifier = get_attack_info(damage)  #201 (line in Coconut source)
        attack_roll_modal = make_roll_modal(upper_container, modifier=_coconut.list(_coconut.itertools.chain(attack_bonus)), rng=rng, history_box=history_box)  #202 (line in Coconut source)
        weapon_name = make_roll_cell(rng, attack_roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=_coconut.list(_coconut.itertools.chain(attack_bonus)), roll_type=weapon), text=weapon)  #203 (line in Coconut source)
        table_row.add(weapon_name)  #208 (line in Coconut source)
        attack_bonus_cell = make_cell_div(text=make_mod_text(attack_bonus))  #209 (line in Coconut source)
        table_row.add(attack_bonus_cell)  #210 (line in Coconut source)
        damage_roll_modal = make_roll_modal(upper_container, modifier=[int(modifier),], die=int(die), num_dice=int(num_dice), rng=rng, history_box=history_box)  #211 (line in Coconut source)
        damage_cell = make_roll_cell(rng, damage_roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[int(modifier),], die=int(die), num_dice=int(num_dice), roll_type="{_coconut_format_0} Damage".format(_coconut_format_0=(weapon))), text=damage)  #219 (line in Coconut source)
        table_row.add(damage_cell)  #230 (line in Coconut source)
        multiplier_cell = make_cell_div(text=multiplier)  #231 (line in Coconut source)
        table_row.add(multiplier_cell)  #232 (line in Coconut source)

    return weapons_row  #234 (line in Coconut source)


def make_ranged_weapons_box(upper_container, char, rng, history_box):  #236 (line in Coconut source)
    weapons_row = make_col_flex_div(overflow=True)  #237 (line in Coconut source)
    for weapon_name, weapon_info in char.ranged_weapons.items():  #238 (line in Coconut source)
        headers = [weapon_name,]  #239 (line in Coconut source)
        attack_bonus = ["",]  #240 (line in Coconut source)
        damage = ["",]  #241 (line in Coconut source)
        crit = ["",]  #242 (line in Coconut source)

        for distance, (curr_attack_bonus, curr_damage, curr_crit) in weapon_info.items():  #244 (line in Coconut source)
            headers.append(distance)  #245 (line in Coconut source)
            attack_bonus.append(curr_attack_bonus)  #246 (line in Coconut source)
            damage.append(curr_damage)  #247 (line in Coconut source)
            crit.append(curr_crit)  #248 (line in Coconut source)

        table, table_body = make_table(headers)  #250 (line in Coconut source)
        weapons_row.add(table)  #251 (line in Coconut source)
        attack_bonus_row = jp.Tr()  #252 (line in Coconut source)
        damage_row = jp.Tr()  #253 (line in Coconut source)
        table_body.add(attack_bonus_row, damage_row)  #254 (line in Coconut source)

        for i in range(len(headers)):  #256 (line in Coconut source)
            if i > 0:  #257 (line in Coconut source)
                attack_bonus_modal = make_roll_modal(upper_container, modifier=attack_bonus[i], rng=rng, history_box=history_box)  #258 (line in Coconut source)
                attack_bonus_cell = make_roll_cell(rng, attack_bonus_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=attack_bonus[i], roll_type=weapon_name), text=make_mod_text(attack_bonus[i]))  #259 (line in Coconut source)
                attack_bonus_row.add(attack_bonus_cell)  #264 (line in Coconut source)

                num_dice, die_type, modifier = get_attack_info(damage[i])  #266 (line in Coconut source)
                damage_roll_modal = make_roll_modal(upper_container, modifier=[int(modifier),], die=int(die_type), num_dice=int(num_dice), rng=rng, history_box=history_box)  #267 (line in Coconut source)
                damage_cell = make_roll_cell(rng, damage_roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[int(modifier),], die=int(die_type), num_dice=int(num_dice), roll_type="{_coconut_format_0} Damage".format(_coconut_format_0=(weapon_name))), text=damage[i])  #275 (line in Coconut source)
                damage_row.add(damage_cell)  #286 (line in Coconut source)
            else:  #287 (line in Coconut source)
                attack_bonus_cell = make_cell_div(text="")  #288 (line in Coconut source)
                attack_bonus_row.add(attack_bonus_cell)  #289 (line in Coconut source)
                damage_cell = make_cell_div(text="")  #290 (line in Coconut source)
                damage_row.add(damage_cell)  #291 (line in Coconut source)

    return weapons_row  #293 (line in Coconut source)


def make_special_attacks_box(char):  #295 (line in Coconut source)
    attacks_row = make_col_flex_div()  #296 (line in Coconut source)

    table, table_body = make_table(["Special Attacks",])  #298 (line in Coconut source)
    attacks_row.add(table)  #299 (line in Coconut source)

    for attack in char.special_attacks:  #301 (line in Coconut source)
        table_row = jp.Tr()  #302 (line in Coconut source)
        table_body.add(table_row)  #303 (line in Coconut source)
        next_row = jp.Tr()  #304 (line in Coconut source)
        table_body.add(next_row)  #305 (line in Coconut source)
        attack_cell = make_collapsible_comp(table_row, attack.name, attack.description)  #306 (line in Coconut source)
        next_row.add(attack_cell)  #307 (line in Coconut source)
    return attacks_row  #308 (line in Coconut source)


def make_special_qualities_box(char):  #310 (line in Coconut source)
    qualities_row = make_col_flex_div()  #311 (line in Coconut source)

    table, table_body = make_table(["Special Qualities",])  #313 (line in Coconut source)
    qualities_row.add(table)  #314 (line in Coconut source)

    for quality in char.special_abilities:  #316 (line in Coconut source)
        table_row = jp.Tr()  #317 (line in Coconut source)
        table_body.add(table_row)  #318 (line in Coconut source)
        next_row = jp.Tr()  #319 (line in Coconut source)
        table_body.add(next_row)  #320 (line in Coconut source)
        quality_cell = make_collapsible_comp(table_row, quality.name, quality.description)  #321 (line in Coconut source)
        next_row.add(quality_cell)  #322 (line in Coconut source)
    return qualities_row  #323 (line in Coconut source)


def make_roll_cell(rng, roll_modal, click, text=""):  #325 (line in Coconut source)
    click = _coconut_base_compose(_coconut_partial(safe_call, click), (print, 0, False))  #326 (line in Coconut source)
    cell = jp.Td(text=text, classes=roll_cell_classes, style=roll_cell_style, click=click)  #327 (line in Coconut source)
    cell.roll_modal = roll_modal  #333 (line in Coconut source)
    return cell  #334 (line in Coconut source)


def make_collapsible_button_cell(click, text=""):  #336 (line in Coconut source)
    cell = jp.Td(text=text, classes=collapse_button_classes, style=collapse_button_style, click=click)  #337 (line in Coconut source)
    return cell  #343 (line in Coconut source)


def make_save_text(save_type  # type: str  #345 (line in Coconut source)
    ):  #345 (line in Coconut source)
# type: (...) -> str
    save_dict = _coconut.dict((("fort", "Fortitude"), ("ref", "Reflex"), ("will", "Will")))  #346 (line in Coconut source)
    return save_dict[save_type]  #347 (line in Coconut source)


def make_saves_box(upper_container, char, rng, history_box):  #349 (line in Coconut source)
    save_row = make_col_flex_div()  #350 (line in Coconut source)

    table, table_body = make_table(["Saving Throws", "Total"])  #352 (line in Coconut source)
    save_row.add(table)  #353 (line in Coconut source)

    for throw in SavingThrows:  #355 (line in Coconut source)
        table_row = jp.Tr()  #356 (line in Coconut source)
        table_body.add(table_row)  #357 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[char.saving_throws[throw.value],], rng=rng, history_box=history_box)  #358 (line in Coconut source)
        button = make_roll_cell(rng, roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[char.saving_throws[throw.value],], roll_type=make_save_text(throw.name)), text=make_save_text(throw.name))  #359 (line in Coconut source)
        table_row.add(button)  #364 (line in Coconut source)
        total = make_cell_div(text=make_mod_text([char.saving_throws[throw.value],]))  #365 (line in Coconut source)
        table_row.add(total)  #366 (line in Coconut source)
    if char.conditional_st_modifiers:  #367 (line in Coconut source)
        table_row = jp.Tr()  #368 (line in Coconut source)
        table_body.add(table_row)  #369 (line in Coconut source)
        conditional_modifier_row = make_cell_div(text="<br>".join(char.conditional_st_modifiers))  #370 (line in Coconut source)
        table_row.add(conditional_modifier_row)  #371 (line in Coconut source)
        table_row.add(make_button_div())  #372 (line in Coconut source)
    return save_row  #373 (line in Coconut source)


def make_lang_box(char):  #375 (line in Coconut source)
    lang_row = make_col_flex_div()  #376 (line in Coconut source)

    table, table_body = make_table(["Languages",])  #378 (line in Coconut source)
    lang_row.add(table)  #379 (line in Coconut source)

    for lang in char.languages:  #381 (line in Coconut source)
        table_row = jp.Tr()  #382 (line in Coconut source)
        table_body.add(table_row)  #383 (line in Coconut source)
        if lang == "Xenophobic":  #384 (line in Coconut source)
            lang = "Glorbon"  #385 (line in Coconut source)
        language = make_cell_div(text=lang)  #386 (line in Coconut source)
        table_row.add(language)  #387 (line in Coconut source)

    return lang_row  #389 (line in Coconut source)


@_coconut_tco  #391 (line in Coconut source)
def make_spell_text(spell  # type: Spell  #391 (line in Coconut source)
    ):  #391 (line in Coconut source)
# type: (...) -> str
    return _coconut_tail_call("<b>DC:</b> {_coconut_format_0} | <b>Save:</b> {_coconut_format_1} | <b>Casting Time:</b> {_coconut_format_2} | <b>Target:</b> {_coconut_format_3} | <b>Range:</b> {_coconut_format_4} | <b>Duration:</b> {_coconut_format_5}<br><br>{_coconut_format_6}".format, _coconut_format_0=(spell.dc), _coconut_format_1=(spell.save_info), _coconut_format_2=(spell.casting_time), _coconut_format_3=(spell.target), _coconut_format_4=(spell.spell_range), _coconut_format_5=(spell.duration), _coconut_format_6=(spell.effect))  #392 (line in Coconut source)


def toggle_collapsible_content(self, msg):  #394 (line in Coconut source)
    if 'hidden' in self.content.classes:  #395 (line in Coconut source)
        self.content.remove_class('hidden')  #396 (line in Coconut source)
    else:  #397 (line in Coconut source)
        self.content.set_class('hidden')  #398 (line in Coconut source)


def make_collapsible_comp(upper_container, button_name="", inner_text=""):  #400 (line in Coconut source)
    content = jp.Div(inner_html=inner_text, classes='border p-4 hidden')  #401 (line in Coconut source)
    button = make_collapsible_button_cell(click=toggle_collapsible_content, text=button_name)  #402 (line in Coconut source)
    button.content = content  #403 (line in Coconut source)
    upper_container.add(button)  #404 (line in Coconut source)

    return content  #406 (line in Coconut source)


def make_spells_box(reset_button, char):  #408 (line in Coconut source)
    spells_row = make_col_flex_div()  #409 (line in Coconut source)
    table, table_body = make_table(["Spell", "Casts", "Level"])  #410 (line in Coconut source)
    reset_button.checkboxes = []  #411 (line in Coconut source)

    spells_row.add(table)  #413 (line in Coconut source)
    button = reset_button  #414 (line in Coconut source)
    for spell in char.spells:  #415 (line in Coconut source)
        table_row = jp.Tr()  #416 (line in Coconut source)
        table_body.add(table_row)  #417 (line in Coconut source)
        next_row = jp.Tr()  #418 (line in Coconut source)
        table_body.add(next_row)  #419 (line in Coconut source)
        spell_cell = make_collapsible_comp(table_row, spell.name, make_spell_text(spell))  #420 (line in Coconut source)
        next_row.add(spell_cell)  #421 (line in Coconut source)
        num_checkboxes = spell.times_memorized  #422 (line in Coconut source)
        if spell.level == "0":  #423 (line in Coconut source)
            num_checkboxes = 0  #424 (line in Coconut source)
        checkboxes, interim_button = make_checkbox_cell(reset_button, num_checkboxes=num_checkboxes)  #425 (line in Coconut source)
        if interim_button:  #426 (line in Coconut source)
            button = interim_button  #427 (line in Coconut source)
        table_row.add(checkboxes)  #428 (line in Coconut source)
        table_row.add(make_cell_div(text=spell.level))  #429 (line in Coconut source)

    return spells_row, button  #431 (line in Coconut source)


def make_spell_like_abilities_box(char):  #433 (line in Coconut source)
    spell_like_abilities_row = make_col_flex_div()  #434 (line in Coconut source)
    table, table_body = make_table(["Spell-like Abilities",])  #435 (line in Coconut source)

    spell_like_abilities_row.add(table)  #437 (line in Coconut source)

    table_row = jp.Tr()  #439 (line in Coconut source)
    table_body.add(table_row)  #440 (line in Coconut source)

    table_row.add(make_cell_div(text=char.spell_like_abilities))  #442 (line in Coconut source)

    return spell_like_abilities_row  #444 (line in Coconut source)


def make_skills_box(upper_container, char, rng, history_box):  #446 (line in Coconut source)
    skills_row = make_col_flex_div()  #447 (line in Coconut source)

    table, table_body = make_table(["Skill", "Modifier"])  #449 (line in Coconut source)
    skills_row.add(table)  #450 (line in Coconut source)

    for skill, modifier in char.skills.items():  #452 (line in Coconut source)
        table_row = jp.Tr()  #453 (line in Coconut source)
        table_body.add(table_row)  #454 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[modifier,], rng=rng, history_box=history_box)  #455 (line in Coconut source)
        skill_name = make_roll_cell(rng, roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[modifier,], roll_type=skill), text=skill)  #456 (line in Coconut source)
        table_row.add(skill_name)  #461 (line in Coconut source)
        modifier_cell = make_cell_div(text=make_mod_text([modifier,]))  #462 (line in Coconut source)
        table_row.add(modifier_cell)  #463 (line in Coconut source)

    return skills_row  #465 (line in Coconut source)


def make_feats_box(char):  #467 (line in Coconut source)
    feats_row = make_col_flex_div()  #468 (line in Coconut source)
    table, table_body = make_table(["Feats",])  #469 (line in Coconut source)

    feats_row.add(table)  #471 (line in Coconut source)

    for feat in char.feats:  #473 (line in Coconut source)
        table_row = jp.Tr()  #474 (line in Coconut source)
        table_body.add(table_row)  #475 (line in Coconut source)
        next_row = jp.Tr()  #476 (line in Coconut source)
        table_body.add(next_row)  #477 (line in Coconut source)
        feat_cell = make_collapsible_comp(table_row, feat.feat_name, feat.feat_benefit)  #478 (line in Coconut source)
        next_row.add(feat_cell)  #479 (line in Coconut source)

    return feats_row  #481 (line in Coconut source)


def make_proficiencies_box(char):  #483 (line in Coconut source)
    prof_row = make_col_flex_div()  #484 (line in Coconut source)
    table, table_body = make_table(["Weapon Proficiencies",])  #485 (line in Coconut source)

    prof_row.add(table)  #487 (line in Coconut source)

    table_row = jp.Tr()  #489 (line in Coconut source)
    table_body.add(table_row)  #490 (line in Coconut source)
    prof_cell = make_cell_div(text=char.weapon_proficiencies)  #491 (line in Coconut source)
    table_row.add(prof_cell)  #492 (line in Coconut source)

    return prof_row  #494 (line in Coconut source)


def make_cmb_and_cmd_box(upper_container, char, rng, history_box):  #496 (line in Coconut source)
    cm_row = make_col_flex_div(overflow=True)  #497 (line in Coconut source)
    headers = ["",]  #498 (line in Coconut source)
    cmb = ["CMB",]  #499 (line in Coconut source)
    cmd = ["CMD",]  #500 (line in Coconut source)

    for cmb_name, value in char.cmb.items():  #502 (line in Coconut source)
        table_header = cmb_name.split("_")[0]  #503 (line in Coconut source)
        cmd_name = table_header + "_defense"  #504 (line in Coconut source)
        headers.append(table_header)  #505 (line in Coconut source)
        cmb.append(value)  #506 (line in Coconut source)
        cmd.append(char.cmd[cmd_name])  #507 (line in Coconut source)

    table, table_body = make_table(headers)  #509 (line in Coconut source)
    cm_row.add(table)  #510 (line in Coconut source)
    cmb_row = jp.Tr()  #511 (line in Coconut source)
    cmd_row = jp.Tr()  #512 (line in Coconut source)
    table_body.add(cmb_row, cmd_row)  #513 (line in Coconut source)

    for i in range(len(headers)):  #515 (line in Coconut source)
        if i != 0:  #516 (line in Coconut source)
            cmd_cell = make_cell_div(text=cmd[i])  #517 (line in Coconut source)
            cmd_row.add(cmd_cell)  #518 (line in Coconut source)
            cmb_roll_modal = make_roll_modal(upper_container, modifier=[int(cmb[i]),], rng=rng, history_box=history_box)  #519 (line in Coconut source)
            cmb_cell = make_roll_cell(rng, cmb_roll_modal, click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[int(cmb[i]),], roll_type="CMB"), text=make_mod_text([cmb[i],]))  #520 (line in Coconut source)
            cmb_row.add(cmb_cell)  #525 (line in Coconut source)
        else:  #526 (line in Coconut source)
            cmd_cell = make_cell_div(text="<b>{_coconut_format_0}</b>".format(_coconut_format_0=(cmd[i])))  #527 (line in Coconut source)
            cmd_row.add(cmd_cell)  #528 (line in Coconut source)
            cmb_cell = make_cell_div(text="<b>{_coconut_format_0}</b>".format(_coconut_format_0=(cmb[i])))  #529 (line in Coconut source)
            cmb_row.add(cmb_cell)  #530 (line in Coconut source)

    return cm_row  #532 (line in Coconut source)


def make_large_row(upper_container, reset_button, char, rng, history_box):  #534 (line in Coconut source)
    main_row = make_row_flex_div()  #535 (line in Coconut source)

    cm_box = make_cmb_and_cmd_box(upper_container, char, rng, history_box)  #537 (line in Coconut source)

    special_qualities_box = make_special_qualities_box(char)  #539 (line in Coconut source)

    left_col = make_one_third_col_div()  #541 (line in Coconut source)
    abilities_box = make_abilities_box(upper_container, char, rng, history_box)  #542 (line in Coconut source)
    weapons_box = make_weapons_box(upper_container, char, rng, history_box)  #543 (line in Coconut source)
    left_col.add(abilities_box, make_base_attack_box(upper_container, char, rng, history_box), weapons_box)  #544 (line in Coconut source)
    if char.ranged_weapons:  #545 (line in Coconut source)
        left_col.add(make_ranged_weapons_box(upper_container, char, rng, history_box))  #546 (line in Coconut source)
    if char.spells:  #547 (line in Coconut source)
        left_col.add(cm_box)  #548 (line in Coconut source)
    if char.special_attacks:  #549 (line in Coconut source)
        left_col.add(make_special_attacks_box(char))  #550 (line in Coconut source)
    if char.special_abilities and char.spells:  #551 (line in Coconut source)
        left_col.add(special_qualities_box)  #552 (line in Coconut source)
    left_col.add(make_feats_box(char))  #553 (line in Coconut source)

# saves, langs, proficiencies, spells
    middle_col = make_one_third_col_div()  #556 (line in Coconut source)
    saves_box = make_saves_box(upper_container, char, rng, history_box)  #557 (line in Coconut source)
    spell_like_abilities_box = make_spell_like_abilities_box(char)  #558 (line in Coconut source)
    spells_box, button = make_spells_box(reset_button, char)  #559 (line in Coconut source)
    middle_col.add(saves_box)  #560 (line in Coconut source)

    if not char.spells:  #562 (line in Coconut source)
        middle_col.add(cm_box)  #563 (line in Coconut source)

    if char.spell_like_abilities:  #565 (line in Coconut source)
        middle_col.add(spell_like_abilities_box)  #566 (line in Coconut source)

    if char.spells:  #568 (line in Coconut source)
        middle_col.add(spells_box)  #569 (line in Coconut source)

    if not char.spells and char.special_abilities:  #571 (line in Coconut source)
        middle_col.add(special_qualities_box)  #572 (line in Coconut source)

    right_col = make_one_third_col_div()  #574 (line in Coconut source)
    right_col.add(make_skills_box(upper_container, char, rng, history_box), make_lang_box(char), make_proficiencies_box(char))  #575 (line in Coconut source)

    main_row.add(left_col, middle_col, right_col)  #577 (line in Coconut source)
    return main_row, button  #578 (line in Coconut source)


def toggle_roll_modal(self, msg, rng, die=20, num_dice=1, modifier=[0,], roll_type=""):  #580 (line in Coconut source)
    if not self.roll_modal.show:  #581 (line in Coconut source)
        rolls = roll_dice(rng, die_type=int(die), num_dice=int(num_dice), num_rolls=len(modifier))  #582 (line in Coconut source)
        self.roll_modal.content.inner_html = make_roll_result_text(rolls, modifier)  #583 (line in Coconut source)
        print(self.roll_modal.history_box.inner_html)  #584 (line in Coconut source)
        current_history = self.roll_modal.history_box.inner_html.split('<br>')  #585 (line in Coconut source)
        for i in range(len(rolls)):  #586 (line in Coconut source)
            current_history.append("{_coconut_format_0}: {_coconut_format_1} + {_coconut_format_2}".format(_coconut_format_0=(roll_type), _coconut_format_1=(rolls[i]), _coconut_format_2=(modifier[i])))  #587 (line in Coconut source)
        self.roll_modal.history_box.inner_html = '<br>'.join(current_history).removeprefix("<br>")  #588 (line in Coconut source)
        print(self.roll_modal.history_box.inner_html)  #589 (line in Coconut source)
    self.roll_modal.show = not self.roll_modal.show  #590 (line in Coconut source)


def make_roll_modal(upper_container, rng, modifier=[0,], die=20, num_dice=1, history_box=None):  #592 (line in Coconut source)
    modal_backdrop = jp.Div(classes="fixed w-full h-full top-0 left-0 flex items-center justify-center bg-black bg-opacity-50", show=False)  #593 (line in Coconut source)
    upper_container.add(modal_backdrop)  #595 (line in Coconut source)

    modal_content = jp.Div(classes="bg-white rounded shadow-lg w-1/3 p-8 m-4 relative")  #597 (line in Coconut source)
    modal_backdrop.add(modal_content)  #598 (line in Coconut source)
    modal_title = jp.H1(text="Roll", classes="text-xl font-bold mb-4")  #599 (line in Coconut source)
    modal_content.add(modal_title)  #600 (line in Coconut source)
    rolls = roll_dice(rng, die_type=int(die), num_dice=int(num_dice), num_rolls=len(modifier))  #601 (line in Coconut source)
    modal_text = jp.P(text=make_roll_result_text(rolls, modifier), classes="mb-4")  #602 (line in Coconut source)
    modal_content.add(modal_text)  #603 (line in Coconut source)
    modal_backdrop.content = modal_text  #604 (line in Coconut source)
    modal_backdrop.history_box = history_box  #605 (line in Coconut source)

# Close button inside the modal
    close_button = jp.Button(text="Close", classes="bg-red-500 text-white px-4 py-2", click=_coconut_partial(toggle_roll_modal, rng=rng, modifier=[modifier,]))  #608 (line in Coconut source)
    close_button.roll_modal = modal_backdrop  #612 (line in Coconut source)
    modal_content.add(close_button)  #613 (line in Coconut source)

    return modal_backdrop  #615 (line in Coconut source)
