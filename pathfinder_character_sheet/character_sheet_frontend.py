#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc0a1581b

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
    print("LONG REST")  #48 (line in Coconut source)
    for checkbox in self.checkboxes:  #49 (line in Coconut source)
        checkbox.checked = False  #50 (line in Coconut source)
    self.hp_input.value = "{_coconut_format_0}".format(_coconut_format_0=(char.max_hp))  #51 (line in Coconut source)


def make_checkbox_cell(reset_button, num_checkboxes):  #53 (line in Coconut source)
    checkbox_div = jp.Div(classes=checkbox_div_classes, style=checkbox_div_style)  #54 (line in Coconut source)
    if num_checkboxes == "At Will":  #55 (line in Coconut source)
        return checkbox_div, None  #56 (line in Coconut source)
    for i in range(int(num_checkboxes)):  #57 (line in Coconut source)
        checkbox = jp.Input(type="checkbox", classes=checkbox_classes, style=checkbox_style, checked=False)  #58 (line in Coconut source)
        reset_button.checkboxes.append(checkbox)  #59 (line in Coconut source)
        checkbox_div.add(checkbox)  #60 (line in Coconut source)
    return checkbox_div, reset_button  #61 (line in Coconut source)


def make_title_row(char, reset_button):  #63 (line in Coconut source)
    title_row = make_row_flex_div()  #64 (line in Coconut source)
    name_box = make_title_box("50px", "1/8", char.name)  #65 (line in Coconut source)
    class_str = "{_coconut_format_0}".format(_coconut_format_0=(', '.join(char.char_classes)))  #66 (line in Coconut source)
    if char.archetypes:  #67 (line in Coconut source)
        class_str += ": " + ", ".join(char.archetypes)  #68 (line in Coconut source)
    class_box = make_title_box("50px", "1/4", class_str)  #69 (line in Coconut source)
    level_box = make_title_box("50px", "1/8", "Level " + str(char.level))  #70 (line in Coconut source)
    title_row.add(name_box, class_box, level_box)  #71 (line in Coconut source)
    title_row.add(reset_button)  #72 (line in Coconut source)
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


def make_useful_info_row(upper_container, reset_button, char, rng):  #89 (line in Coconut source)
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
    roll_modal = make_roll_modal(upper_container, modifier=[char.initiative,], rng=rng)  #110 (line in Coconut source)
    initiative_data = make_roll_cell(rng, roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[char.initiative,]), text=make_mod_text([char.initiative,]))  #111 (line in Coconut source)
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


def make_abilities_box(upper_container, char, rng):  #134 (line in Coconut source)
    ability_row = make_col_flex_div()  #135 (line in Coconut source)

    table, table_body = make_table(["Ability", "Score", "Modifier"])  #137 (line in Coconut source)
    ability_row.add(table)  #138 (line in Coconut source)

    for ability in Stats:  #140 (line in Coconut source)
        table_row = jp.Tr()  #141 (line in Coconut source)
        table_body.add(table_row)  #142 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[get_stat_modifier(char.stats[ability.value]),], rng=rng)  #143 (line in Coconut source)
        ability_name = make_roll_cell(rng, roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[get_stat_modifier(char.stats[ability.value]),]), text=ability.name)  #144 (line in Coconut source)
        table_row.add(ability_name)  #149 (line in Coconut source)
        score = make_cell_div(text=str(char.stats[ability.value]))  #150 (line in Coconut source)
        table_row.add(score)  #151 (line in Coconut source)
        modifier = make_cell_div(text=make_mod_text([get_stat_modifier(char.stats[ability.value]),]))  #152 (line in Coconut source)
        table_row.add(modifier)  #153 (line in Coconut source)
    return ability_row  #154 (line in Coconut source)


def make_weapons_box(upper_container, char, rng) -> dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]:  #156 (line in Coconut source)
    weapons_row = make_col_flex_div()  #157 (line in Coconut source)

    table, table_body = make_table(["Weapon", "Attack Bonus", "Damage", "Crit Multiplier"])  #159 (line in Coconut source)
    weapons_row.add(table)  #160 (line in Coconut source)

    for weapon, (attack_bonus, damage, multiplier) in char.weapons.items():  #162 (line in Coconut source)
        table_row = jp.Tr()  #163 (line in Coconut source)
        table_body.add(table_row)  #164 (line in Coconut source)
        num_dice, die, modifier = get_attack_info(damage)  #165 (line in Coconut source)
        attack_roll_modal = make_roll_modal(upper_container, modifier=[*attack_bonus,], rng=rng)  #166 (line in Coconut source)
        weapon_name = make_roll_cell(rng, attack_roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[*attack_bonus,]), text=weapon)  #167 (line in Coconut source)
        table_row.add(weapon_name)  #172 (line in Coconut source)
        attack_bonus_cell = make_cell_div(text=make_mod_text(attack_bonus))  #173 (line in Coconut source)
        table_row.add(attack_bonus_cell)  #174 (line in Coconut source)
        damage_roll_modal = make_roll_modal(upper_container, modifier=[int(modifier),], die=int(die), num_dice=int(num_dice), rng=rng)  #175 (line in Coconut source)
        damage_cell = make_roll_cell(rng, damage_roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[int(modifier),], die=int(die), num_dice=int(num_dice)), text=damage)  #176 (line in Coconut source)
        table_row.add(damage_cell)  #181 (line in Coconut source)
        multiplier_cell = make_cell_div(text=multiplier)  #182 (line in Coconut source)
        table_row.add(multiplier_cell)  #183 (line in Coconut source)

    return weapons_row  #185 (line in Coconut source)


def make_ranged_weapons_box(upper_container, char, rng):  #187 (line in Coconut source)
    weapons_row = make_col_flex_div(overflow=True)  #188 (line in Coconut source)
    for weapon_name, weapon_info in char.ranged_weapons.items():  #189 (line in Coconut source)
        headers = [weapon_name,]  #190 (line in Coconut source)
        attack_bonus = ["",]  #191 (line in Coconut source)
        damage = ["",]  #192 (line in Coconut source)
        crit = ["",]  #193 (line in Coconut source)

        for distance, (curr_attack_bonus, curr_damage, curr_crit) in weapon_info.items():  #195 (line in Coconut source)
            headers.append(distance)  #196 (line in Coconut source)
            attack_bonus.append(curr_attack_bonus)  #197 (line in Coconut source)
            damage.append(curr_damage)  #198 (line in Coconut source)
            crit.append(curr_crit)  #199 (line in Coconut source)

        table, table_body = make_table(headers)  #201 (line in Coconut source)
        weapons_row.add(table)  #202 (line in Coconut source)
        attack_bonus_row = jp.Tr()  #203 (line in Coconut source)
        damage_row = jp.Tr()  #204 (line in Coconut source)
        table_body.add(attack_bonus_row, damage_row)  #205 (line in Coconut source)

        for i in range(len(headers)):  #207 (line in Coconut source)
            if i > 0:  #208 (line in Coconut source)
                attack_bonus_modal = make_roll_modal(upper_container, modifier=attack_bonus[i], rng=rng)  #209 (line in Coconut source)
                attack_bonus_cell = make_roll_cell(rng, attack_bonus_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=attack_bonus[i]), text=make_mod_text(attack_bonus[i]))  #210 (line in Coconut source)
                attack_bonus_row.add(attack_bonus_cell)  #215 (line in Coconut source)

                num_dice, die_type, modifier = get_attack_info(damage[i])  #217 (line in Coconut source)
                damage_roll_modal = make_roll_modal(upper_container, modifier=[int(modifier),], die=int(die_type), num_dice=int(num_dice), rng=rng)  #218 (line in Coconut source)
                damage_cell = make_roll_cell(rng, damage_roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[int(modifier),], die=int(die_type), num_dice=int(num_dice)), text=damage[i])  #220 (line in Coconut source)
                damage_row.add(damage_cell)  #225 (line in Coconut source)
            else:  #226 (line in Coconut source)
                attack_bonus_cell = make_cell_div(text="")  #227 (line in Coconut source)
                attack_bonus_row.add(attack_bonus_cell)  #228 (line in Coconut source)
                damage_cell = make_cell_div(text="")  #229 (line in Coconut source)
                damage_row.add(damage_cell)  #230 (line in Coconut source)

    return weapons_row  #232 (line in Coconut source)


def make_special_attacks_box(char):  #234 (line in Coconut source)
    attacks_row = make_col_flex_div()  #235 (line in Coconut source)

    table, table_body = make_table(["Special Attacks",])  #237 (line in Coconut source)
    attacks_row.add(table)  #238 (line in Coconut source)

    for attack in char.special_attacks:  #240 (line in Coconut source)
        table_row = jp.Tr()  #241 (line in Coconut source)
        table_body.add(table_row)  #242 (line in Coconut source)
        next_row = jp.Tr()  #243 (line in Coconut source)
        table_body.add(next_row)  #244 (line in Coconut source)
        attack_cell = make_collapsible_comp(table_row, attack.name, attack.description)  #245 (line in Coconut source)
        next_row.add(attack_cell)  #246 (line in Coconut source)
    return attacks_row  #247 (line in Coconut source)


def make_special_qualities_box(char):  #249 (line in Coconut source)
    qualities_row = make_col_flex_div()  #250 (line in Coconut source)

    table, table_body = make_table(["Special Qualities",])  #252 (line in Coconut source)
    qualities_row.add(table)  #253 (line in Coconut source)

    for quality in char.special_abilities:  #255 (line in Coconut source)
        table_row = jp.Tr()  #256 (line in Coconut source)
        table_body.add(table_row)  #257 (line in Coconut source)
        next_row = jp.Tr()  #258 (line in Coconut source)
        table_body.add(next_row)  #259 (line in Coconut source)
        quality_cell = make_collapsible_comp(table_row, quality.name, quality.description)  #260 (line in Coconut source)
        next_row.add(quality_cell)  #261 (line in Coconut source)
    return qualities_row  #262 (line in Coconut source)


def make_roll_cell(rng, roll_modal, click, text=""):  #264 (line in Coconut source)
    cell = jp.Td(text=text, classes=roll_cell_classes, style=roll_cell_style, click=click)  #265 (line in Coconut source)
    cell.roll_modal = roll_modal  #271 (line in Coconut source)
    return cell  #272 (line in Coconut source)


def make_collapsible_button_cell(click, text=""):  #274 (line in Coconut source)
    cell = jp.Td(text=text, classes=collapse_button_classes, style=collapse_button_style, click=click)  #275 (line in Coconut source)
    return cell  #281 (line in Coconut source)


def make_save_text(save_type: str) -> str:  #283 (line in Coconut source)
    save_dict = {"fort": "Fortitude", "ref": "Reflex", "will": "Will"}  #284 (line in Coconut source)
    return save_dict[save_type]  #285 (line in Coconut source)


def make_saves_box(upper_container, char, rng):  #287 (line in Coconut source)
    save_row = make_col_flex_div()  #288 (line in Coconut source)

    table, table_body = make_table(["Saving Throws", "Total"])  #290 (line in Coconut source)
    save_row.add(table)  #291 (line in Coconut source)

    for throw in SavingThrows:  #293 (line in Coconut source)
        table_row = jp.Tr()  #294 (line in Coconut source)
        table_body.add(table_row)  #295 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[char.saving_throws[throw.value],], rng=rng)  #296 (line in Coconut source)
        button = make_roll_cell(rng, roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[char.saving_throws[throw.value],]), text=make_save_text(throw.name))  #297 (line in Coconut source)
        table_row.add(button)  #302 (line in Coconut source)
        total = make_cell_div(text=make_mod_text([char.saving_throws[throw.value],]))  #303 (line in Coconut source)
        table_row.add(total)  #304 (line in Coconut source)
    if char.conditional_st_modifiers:  #305 (line in Coconut source)
        table_row = jp.Tr()  #306 (line in Coconut source)
        table_body.add(table_row)  #307 (line in Coconut source)
        print(char.conditional_st_modifiers)  #308 (line in Coconut source)
        conditional_modifier_row = make_cell_div(text="<br>".join(char.conditional_st_modifiers))  #309 (line in Coconut source)
        table_row.add(conditional_modifier_row)  #310 (line in Coconut source)
        table_row.add(make_button_div())  #311 (line in Coconut source)
    return save_row  #312 (line in Coconut source)


def make_lang_box(char):  #314 (line in Coconut source)
    lang_row = make_col_flex_div()  #315 (line in Coconut source)

    table, table_body = make_table(["Languages",])  #317 (line in Coconut source)
    lang_row.add(table)  #318 (line in Coconut source)

    for lang in char.languages:  #320 (line in Coconut source)
        table_row = jp.Tr()  #321 (line in Coconut source)
        table_body.add(table_row)  #322 (line in Coconut source)
        if lang == "Xenophobic":  #323 (line in Coconut source)
            lang = "Glorbon"  #324 (line in Coconut source)
        language = make_cell_div(text=lang)  #325 (line in Coconut source)
        table_row.add(language)  #326 (line in Coconut source)

    return lang_row  #328 (line in Coconut source)


@_coconut_tco  #330 (line in Coconut source)
def make_spell_text(spell: Spell) -> str:  #330 (line in Coconut source)
    return _coconut_tail_call("<b>DC:</b> {_coconut_format_0} | <b>Save:</b> {_coconut_format_1} | <b>Casting Time:</b> {_coconut_format_2} | <b>Target:</b> {_coconut_format_3} | <b>Range:</b> {_coconut_format_4} | <b>Duration:</b> {_coconut_format_5}<br><br>{_coconut_format_6}".format, _coconut_format_0=(spell.dc), _coconut_format_1=(spell.save_info), _coconut_format_2=(spell.casting_time), _coconut_format_3=(spell.target), _coconut_format_4=(spell.spell_range), _coconut_format_5=(spell.duration), _coconut_format_6=(spell.effect))  #331 (line in Coconut source)


def toggle_collapsible_content(self, msg):  #333 (line in Coconut source)
    if 'hidden' in self.content.classes:  #334 (line in Coconut source)
        self.content.remove_class('hidden')  #335 (line in Coconut source)
    else:  #336 (line in Coconut source)
        self.content.set_class('hidden')  #337 (line in Coconut source)


def make_collapsible_comp(upper_container, button_name="", inner_text=""):  #339 (line in Coconut source)
    content = jp.Div(inner_html=inner_text, classes='border p-4 hidden')  #340 (line in Coconut source)
    button = make_collapsible_button_cell(click=toggle_collapsible_content, text=button_name)  #341 (line in Coconut source)
    button.content = content  #342 (line in Coconut source)
    upper_container.add(button)  #343 (line in Coconut source)

    return content  #345 (line in Coconut source)


def make_spells_box(reset_button, char):  #347 (line in Coconut source)
    spells_row = make_col_flex_div()  #348 (line in Coconut source)
    table, table_body = make_table(["Spell", "Casts", "Level"])  #349 (line in Coconut source)
    reset_button.checkboxes = []  #350 (line in Coconut source)

    spells_row.add(table)  #352 (line in Coconut source)
    button = reset_button  #353 (line in Coconut source)
    for spell in char.spells:  #354 (line in Coconut source)
        table_row = jp.Tr()  #355 (line in Coconut source)
        table_body.add(table_row)  #356 (line in Coconut source)
        next_row = jp.Tr()  #357 (line in Coconut source)
        table_body.add(next_row)  #358 (line in Coconut source)
        spell_cell = make_collapsible_comp(table_row, spell.name, make_spell_text(spell))  #359 (line in Coconut source)
        next_row.add(spell_cell)  #360 (line in Coconut source)
        num_checkboxes = spell.times_memorized  #361 (line in Coconut source)
        if spell.level == "0":  #362 (line in Coconut source)
            num_checkboxes = 0  #363 (line in Coconut source)
        checkboxes, interim_button = make_checkbox_cell(reset_button, num_checkboxes=num_checkboxes)  #364 (line in Coconut source)
        if interim_button:  #365 (line in Coconut source)
            button = interim_button  #366 (line in Coconut source)
        table_row.add(checkboxes)  #367 (line in Coconut source)
        table_row.add(make_cell_div(text=spell.level))  #368 (line in Coconut source)

    return spells_row, button  #370 (line in Coconut source)


def make_spell_like_abilities_box(char):  #372 (line in Coconut source)
    spell_like_abilities_row = make_col_flex_div()  #373 (line in Coconut source)
    table, table_body = make_table(["Spell-like Abilities",])  #374 (line in Coconut source)

    spell_like_abilities_row.add(table)  #376 (line in Coconut source)

    table_row = jp.Tr()  #378 (line in Coconut source)
    table_body.add(table_row)  #379 (line in Coconut source)

    table_row.add(make_cell_div(text=char.spell_like_abilities))  #381 (line in Coconut source)

    return spell_like_abilities_row  #383 (line in Coconut source)


def make_skills_box(upper_container, char, rng):  #385 (line in Coconut source)
    skills_row = make_col_flex_div()  #386 (line in Coconut source)

    table, table_body = make_table(["Skill", "Modifier"])  #388 (line in Coconut source)
    skills_row.add(table)  #389 (line in Coconut source)

    for skill, modifier in char.skills.items():  #391 (line in Coconut source)
        table_row = jp.Tr()  #392 (line in Coconut source)
        table_body.add(table_row)  #393 (line in Coconut source)
        roll_modal = make_roll_modal(upper_container, modifier=[modifier,], rng=rng)  #394 (line in Coconut source)
        skill_name = make_roll_cell(rng, roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[modifier,]), text=skill)  #395 (line in Coconut source)
        table_row.add(skill_name)  #400 (line in Coconut source)
        modifier_cell = make_cell_div(text=make_mod_text([modifier,]))  #401 (line in Coconut source)
        table_row.add(modifier_cell)  #402 (line in Coconut source)

    return skills_row  #404 (line in Coconut source)


def make_feats_box(char):  #406 (line in Coconut source)
    feats_row = make_col_flex_div()  #407 (line in Coconut source)
    table, table_body = make_table(["Feats",])  #408 (line in Coconut source)

    feats_row.add(table)  #410 (line in Coconut source)

    for feat in char.feats:  #412 (line in Coconut source)
        table_row = jp.Tr()  #413 (line in Coconut source)
        table_body.add(table_row)  #414 (line in Coconut source)
        next_row = jp.Tr()  #415 (line in Coconut source)
        table_body.add(next_row)  #416 (line in Coconut source)
        feat_cell = make_collapsible_comp(table_row, feat.feat_name, feat.feat_benefit)  #417 (line in Coconut source)
        next_row.add(feat_cell)  #418 (line in Coconut source)

    return feats_row  #420 (line in Coconut source)


def make_proficiencies_box(char):  #422 (line in Coconut source)
    prof_row = make_col_flex_div()  #423 (line in Coconut source)
    table, table_body = make_table(["Weapon Proficiencies",])  #424 (line in Coconut source)

    prof_row.add(table)  #426 (line in Coconut source)

    table_row = jp.Tr()  #428 (line in Coconut source)
    table_body.add(table_row)  #429 (line in Coconut source)
    prof_cell = make_cell_div(text=char.weapon_proficiencies)  #430 (line in Coconut source)
    table_row.add(prof_cell)  #431 (line in Coconut source)

    return prof_row  #433 (line in Coconut source)


def make_cmb_and_cmd_box(upper_container, char, rng):  #435 (line in Coconut source)
    cm_row = make_col_flex_div(overflow=True)  #436 (line in Coconut source)
    headers = ["",]  #437 (line in Coconut source)
    cmb = ["CMB",]  #438 (line in Coconut source)
    cmd = ["CMD",]  #439 (line in Coconut source)

    for cmb_name, value in char.cmb.items():  #441 (line in Coconut source)
        table_header = cmb_name.split("_")[0]  #442 (line in Coconut source)
        cmd_name = table_header + "_defense"  #443 (line in Coconut source)
        headers.append(table_header)  #444 (line in Coconut source)
        cmb.append(value)  #445 (line in Coconut source)
        cmd.append(char.cmd[cmd_name])  #446 (line in Coconut source)

    table, table_body = make_table(headers)  #448 (line in Coconut source)
    cm_row.add(table)  #449 (line in Coconut source)
    cmb_row = jp.Tr()  #450 (line in Coconut source)
    cmd_row = jp.Tr()  #451 (line in Coconut source)
    table_body.add(cmb_row, cmd_row)  #452 (line in Coconut source)

    for i in range(len(headers)):  #454 (line in Coconut source)
        if i != 0:  #455 (line in Coconut source)
            cmd_cell = make_cell_div(text=cmd[i])  #456 (line in Coconut source)
            cmd_row.add(cmd_cell)  #457 (line in Coconut source)
            cmb_roll_modal = make_roll_modal(upper_container, modifier=[int(cmb[i]),], rng=rng)  #458 (line in Coconut source)
            cmb_cell = make_roll_cell(rng, cmb_roll_modal, click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[int(cmb[i]),]), text=make_mod_text([cmb[i],]))  #459 (line in Coconut source)
            cmb_row.add(cmb_cell)  #464 (line in Coconut source)
        else:  #465 (line in Coconut source)
            cmd_cell = make_cell_div(text="<b>{_coconut_format_0}</b>".format(_coconut_format_0=(cmd[i])))  #466 (line in Coconut source)
            cmd_row.add(cmd_cell)  #467 (line in Coconut source)
            cmb_cell = make_cell_div(text="<b>{_coconut_format_0}</b>".format(_coconut_format_0=(cmb[i])))  #468 (line in Coconut source)
            cmb_row.add(cmb_cell)  #469 (line in Coconut source)

    return cm_row  #471 (line in Coconut source)


def make_large_row(upper_container, reset_button, char, rng):  #473 (line in Coconut source)
    main_row = make_row_flex_div()  #474 (line in Coconut source)

    cm_box = make_cmb_and_cmd_box(upper_container, char, rng)  #476 (line in Coconut source)

    special_qualities_box = make_special_qualities_box(char)  #478 (line in Coconut source)

    left_col = make_one_third_col_div()  #480 (line in Coconut source)
    abilities_box = make_abilities_box(upper_container, char, rng)  #481 (line in Coconut source)
    weapons_box = make_weapons_box(upper_container, char, rng)  #482 (line in Coconut source)
    left_col.add(abilities_box, weapons_box)  #483 (line in Coconut source)
    if char.ranged_weapons:  #484 (line in Coconut source)
        left_col.add(make_ranged_weapons_box(upper_container, char, rng))  #485 (line in Coconut source)
    if char.spells:  #486 (line in Coconut source)
        left_col.add(cm_box)  #487 (line in Coconut source)
    if char.special_attacks:  #488 (line in Coconut source)
        left_col.add(make_special_attacks_box(char))  #489 (line in Coconut source)
    if char.special_abilities and char.spells:  #490 (line in Coconut source)
        left_col.add(special_qualities_box)  #491 (line in Coconut source)
    left_col.add(make_feats_box(char))  #492 (line in Coconut source)

# saves, langs, proficiencies, spells
    middle_col = make_one_third_col_div()  #495 (line in Coconut source)
    saves_box = make_saves_box(upper_container, char, rng)  #496 (line in Coconut source)
    spell_like_abilities_box = make_spell_like_abilities_box(char)  #497 (line in Coconut source)
    spells_box, button = make_spells_box(reset_button, char)  #498 (line in Coconut source)
    middle_col.add(saves_box)  #499 (line in Coconut source)

    if not char.spells:  #501 (line in Coconut source)
        middle_col.add(cm_box)  #502 (line in Coconut source)

    if char.spell_like_abilities:  #504 (line in Coconut source)
        middle_col.add(spell_like_abilities_box)  #505 (line in Coconut source)

    if char.spells:  #507 (line in Coconut source)
        middle_col.add(spells_box)  #508 (line in Coconut source)

    if not char.spells and char.special_abilities:  #510 (line in Coconut source)
        middle_col.add(special_qualities_box)  #511 (line in Coconut source)

    right_col = make_one_third_col_div()  #513 (line in Coconut source)
    right_col.add(make_skills_box(upper_container, char, rng), make_lang_box(char), make_proficiencies_box(char))  #514 (line in Coconut source)

    main_row.add(left_col, middle_col, right_col)  #516 (line in Coconut source)
    return main_row, button  #517 (line in Coconut source)


def toggle_roll_modal(self, msg, rng, die=20, num_dice=1, modifier=0):  #519 (line in Coconut source)
    if not self.roll_modal.show:  #520 (line in Coconut source)
        rolls = roll_dice(rng, die_type=int(die), num_dice=int(num_dice), num_rolls=len(modifier))  #521 (line in Coconut source)
        self.roll_modal.content.inner_html = make_roll_result_text(rolls, modifier)  #522 (line in Coconut source)
    self.roll_modal.show = not self.roll_modal.show  #523 (line in Coconut source)


def make_roll_modal(upper_container, rng, modifier=0, die=20, num_dice=1):  #525 (line in Coconut source)
    modal_backdrop = jp.Div(classes="fixed w-full h-full top-0 left-0 flex items-center justify-center bg-black bg-opacity-50", show=False)  #526 (line in Coconut source)
    upper_container.add(modal_backdrop)  #528 (line in Coconut source)

    modal_content = jp.Div(classes="bg-white rounded shadow-lg w-1/3 p-8 m-4 relative")  #530 (line in Coconut source)
    modal_backdrop.add(modal_content)  #531 (line in Coconut source)
    modal_title = jp.H1(text="Roll", classes="text-xl font-bold mb-4")  #532 (line in Coconut source)
    modal_content.add(modal_title)  #533 (line in Coconut source)
    rolls = roll_dice(rng, die_type=int(die), num_dice=int(num_dice), num_rolls=len(modifier))  #534 (line in Coconut source)
    modal_text = jp.P(text=make_roll_result_text(rolls, modifier), classes="mb-4")  #535 (line in Coconut source)
    modal_content.add(modal_text)  #536 (line in Coconut source)
    modal_backdrop.content = modal_text  #537 (line in Coconut source)

# Close button inside the modal
    close_button = jp.Button(text="Close", classes="bg-red-500 text-white px-4 py-2", click=_coconut.functools.partial(toggle_roll_modal, rng=rng, modifier=[modifier,]))  #540 (line in Coconut source)
    close_button.roll_modal = modal_backdrop  #544 (line in Coconut source)
    modal_content.add(close_button)  #545 (line in Coconut source)

    return modal_backdrop  #547 (line in Coconut source)
