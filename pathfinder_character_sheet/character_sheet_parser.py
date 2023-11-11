#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x503ad768

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

from dataclasses import dataclass  #1 (line in Coconut source)
import xml.etree.ElementTree as ET  #2 (line in Coconut source)
import argparse  #3 (line in Coconut source)
from enum import Enum  #4 (line in Coconut source)
from dataclasses import field  #5 (line in Coconut source)

from pathfinder_character_sheet.character import *  #7 (line in Coconut source)
from pathfinder_character_sheet.utils import *  #8 (line in Coconut source)

@_coconut_tco  #10 (line in Coconut source)
def parse_hp(root: ET.Element) -> int:  #10 (line in Coconut source)
    return _coconut_tail_call(int, root.find('hit_points/points').text)  #11 (line in Coconut source)


@_coconut_tco  #13 (line in Coconut source)
def parse_damage_reduction(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #13 (line in Coconut source)
    return _coconut_tail_call(tuple, (x.text for x in root.findall('hit_points/damage_reduction') if x.text))  #14 (line in Coconut source)


@_coconut_tco  #16 (line in Coconut source)
def parse_ac(root: ET.Element) -> _coconut.typing.Tuple[int, int, int]:  #16 (line in Coconut source)
    return _coconut_tail_call(_coconut_mk_anon_namedtuple(('total', 'flat', 'touch')), int(root.find('armor_class/total').text), int(root.find('armor_class/flat').text), int(root.find('armor_class/touch').text))  #17 (line in Coconut source)


def parse_name(root: ET.Element) -> str:  #23 (line in Coconut source)
    return root.find('basics/name').text  #24 (line in Coconut source)


@_coconut_tco  #26 (line in Coconut source)
def parse_initiative(root: ET.Element) -> int:  #26 (line in Coconut source)
    return _coconut_tail_call(int, root.find('initiative/total').text)  #27 (line in Coconut source)


@_coconut_tco  #29 (line in Coconut source)
def parse_spell_resistance(root: ET.Element) -> int:  #29 (line in Coconut source)
    return _coconut_tail_call(int, root.find('initiative/spell_resistance').text)  #30 (line in Coconut source)


@_coconut_tco  #32 (line in Coconut source)
def parse_classes(root: ET.Element):  #32 (line in Coconut source)
    return _coconut_tail_call(tuple, (c.find("name").text for c in root.findall('basics/classes/class')))  #33 (line in Coconut source)


@_coconut_tco  #35 (line in Coconut source)
def parse_skills(root: ET.Element) -> dict[str, int]:  #35 (line in Coconut source)
    return _coconut_tail_call((dict), (map)(lambda skill: (skill.find("name").text, (int)(skill.find("skill_mod").text)), (root).findall('skills/skill')))  #36 (line in Coconut source)


def parse_alignment(root: ET.Element) -> str:  #45 (line in Coconut source)
    return root.find('basics/alignment/long').text  #46 (line in Coconut source)


@_coconut_tco  #48 (line in Coconut source)
def parse_level(root: ET.Element) -> int:  #48 (line in Coconut source)
    return _coconut_tail_call(int, root.find('basics/classes/levels_total').text)  #49 (line in Coconut source)


@_coconut_tco  #51 (line in Coconut source)
def parse_archetypes(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #51 (line in Coconut source)
    return _coconut_tail_call(tuple, (archetype.find("name").text for archetype in root.findall('basics/archetypes/archetype')))  #52 (line in Coconut source)


@_coconut_tco  #54 (line in Coconut source)
def parse_languages(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #54 (line in Coconut source)
    return _coconut_tail_call(tuple, (lang.text for lang in root.findall('basics/languages/language') if lang.text))  #55 (line in Coconut source)


@_coconut_tco  #57 (line in Coconut source)
def parse_movement(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #57 (line in Coconut source)
    movement_values = [0,] * len(Movement)  #58 (line in Coconut source)
    for movement in root.findall('basics/move/move'):  #59 (line in Coconut source)
        movement_values[Movement[movement.find("name").text].value] = int(movement.find("squares").text) * 5  #60 (line in Coconut source)
    return _coconut_tail_call(tuple, movement_values)  #61 (line in Coconut source)


@_coconut_tco  #63 (line in Coconut source)
def parse_vision(root: ET.Element) -> list[str]:  #63 (line in Coconut source)
    return _coconut_tail_call(tuple, (vision.text for vision in root.findall('basics/vision/vision')))  #64 (line in Coconut source)


@_coconut_tco  #66 (line in Coconut source)
def parse_gold(root: ET.Element) -> int:  #66 (line in Coconut source)
    return _coconut_tail_call(int, root.find('basics/gold').text)  #67 (line in Coconut source)


@_coconut_tco  #69 (line in Coconut source)
def parse_stats(root: ET.Element) -> _coconut.typing.Tuple[_coconut.typing.Tuple[int, int], ...]:  #69 (line in Coconut source)
    stat_values = [None,] * len(Stats)  #70 (line in Coconut source)
    for stat in root.findall('abilities/ability'):  #71 (line in Coconut source)
        stat_values[Stats[stat.find("name/short").text].value] = int(stat.find('score').text)  #72 (line in Coconut source)
    return _coconut_tail_call(tuple, stat_values)  #73 (line in Coconut source)


@_coconut_tco  #75 (line in Coconut source)
def parse_saving_throws(root: ET.Element) -> _coconut.typing.Tuple[int, int, int]:  #75 (line in Coconut source)
    throw_values = [None,] * len(SavingThrows)  #76 (line in Coconut source)
    for throw in root.findall('saving_throws/saving_throw'):  #77 (line in Coconut source)
        throw_values[SavingThrows[throw.find("name/short").text].value] = int(throw.find('total').text)  #78 (line in Coconut source)
    return _coconut_tail_call(tuple, throw_values)  #79 (line in Coconut source)


@_coconut_tco  #81 (line in Coconut source)
def parse_melee(root: ET.Element) -> _coconut.typing.Tuple[int, ...]:  #81 (line in Coconut source)
    return _coconut_tail_call(tuple, map(int, root.find('attack/melee/total').text.split('/')))  #82 (line in Coconut source)


@_coconut_tco  #84 (line in Coconut source)
def parse_ranged(root: ET.Element) -> _coconut.typing.Tuple[int, ...]:  #84 (line in Coconut source)
    return _coconut_tail_call(tuple, map(int, root.find('attack/ranged/total').text.split('/')))  #85 (line in Coconut source)


def parse_cmb(root: ET.Element) -> dict[str, int]:  #87 (line in Coconut source)
    cmb_map = {}  #88 (line in Coconut source)
    cm_names = ['grapple_attack', 'trip_attack', 'disarm_attack', 'sunder_attack', 'bullrush_attack', 'overrun_attack']  #89 (line in Coconut source)
    for name in cm_names:  #90 (line in Coconut source)
        cmb_map[name] = int(root.find('attack/cmb/' + name).text)  #91 (line in Coconut source)
    return cmb_map  #92 (line in Coconut source)


def parse_cmd(root: ET.Element) -> dict[str, int]:  #94 (line in Coconut source)
    cmd_map = {}  #95 (line in Coconut source)
    cm_names = ['grapple_defense', 'trip_defense', 'disarm_defense', 'sunder_defense', 'bullrush_defense', 'overrun_defense']  #96 (line in Coconut source)
    for name in cm_names:  #97 (line in Coconut source)
        cmd_map[name] = int(root.find('attack/cmb/' + name).text)  #98 (line in Coconut source)
    return cmd_map  #99 (line in Coconut source)


def parse_weapons(root: ET.Element) -> dict[str, (_coconut.typing.Tuple[int, ...], str, str)]:  #101 (line in Coconut source)
    weapons = {}  #102 (line in Coconut source)
    unarmed_node = root.find('weapons/unarmed')  #103 (line in Coconut source)
    weapons['Unarmed'] = (tuple(map(int, unarmed_node.find('total').text.split('/'))), unarmed_node.find('damage').text, unarmed_node.find('critical').text)  #104 (line in Coconut source)
    for weapon in root.findall('weapons/weapon'):  #109 (line in Coconut source)
        if 'Ranged' in weapon.find('common/category').text:  #110 (line in Coconut source)
            continue  #111 (line in Coconut source)
        damage = weapon.find('common/damage').text  #112 (line in Coconut source)
        attack_bonus = tuple(map(int, weapon.find('common/to_hit/total_hit').text.split('/')))  #113 (line in Coconut source)
        critical = weapon.find('common/critical/range').text + '/x' + weapon.find('common/critical/multiplier').text  #114 (line in Coconut source)
        weapons[weapon.find('common/name/short').text.removeprefix('*')] = (_coconut_mk_anon_namedtuple(('attack_bonus', 'damage', 'critical'))(attack_bonus, damage, critical))  #115 (line in Coconut source)
    return weapons  #116 (line in Coconut source)


def parse_ranged_weapons(root: ET.Element) -> dict[str, dict[str, _coconut.typing.Tuple[_coconut.typing.Tuple[int, ...], str, str]]]:  #118 (line in Coconut source)
    weapons = {}  #119 (line in Coconut source)
    for weapon in root.findall('weapons/weapon'):  #120 (line in Coconut source)
        if not 'Ranged' in weapon.find('common/category').text:  #121 (line in Coconut source)
            continue  #122 (line in Coconut source)
        ranges = {}  #123 (line in Coconut source)
        for distance in weapon.findall('ranges/range'):  #124 (line in Coconut source)
            damage = distance.find('damage').text  #125 (line in Coconut source)
            attack_bonus = tuple(map(int, distance.find('to_hit').text.split('/')))  #126 (line in Coconut source)
            critical = weapon.find('common/critical/range').text + '/' + weapon.find('common/critical/multiplier').text  #127 (line in Coconut source)
            ranges[distance.find('distance').text] = (_coconut_mk_anon_namedtuple(('attack_bonus', 'damage', 'crit'))(attack_bonus, damage, critical))  #128 (line in Coconut source)
        weapons[weapon.find('common/name/long').text.removeprefix('*')] = ranges  #129 (line in Coconut source)
    return weapons  #130 (line in Coconut source)


@_coconut_tco  #132 (line in Coconut source)
def parse_special_attacks(root: ET.Element) -> _coconut.typing.Tuple[_coconut.typing.Tuple[str, str], ...]:  #132 (line in Coconut source)
    return _coconut_tail_call(tuple, ((_coconut_mk_anon_namedtuple(('name', 'description'))(attack.find('name').text, attack.find('description').text)) for attack in root.findall('special_attacks/special_attack')))  #133 (line in Coconut source)


@_coconut_tco  #137 (line in Coconut source)
def parse_conditional_st_modifier(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #137 (line in Coconut source)
    return _coconut_tail_call((tuple), (map)(_coconut.operator.attrgetter("text"), (flatten)((map)(_coconut.operator.methodcaller("findall", 'savebonus/description'), (filter)(ident, (root).findall('saving_throws/conditional_modifiers'))))))  #138 (line in Coconut source)


@_coconut_tco  #148 (line in Coconut source)
def create_spell_from_node(spell_node: ET.Element, **kwargs) -> Spell:  #148 (line in Coconut source)
    effect_text = ""  #149 (line in Coconut source)
    if spell_node.findall('effect/para'):  #150 (line in Coconut source)
        for para in spell_node.findall('effect/para'):  #151 (line in Coconut source)
            effect_text += para.text + "<br><br>"  #152 (line in Coconut source)
        effect_text.removesuffix("<br><br>")  #153 (line in Coconut source)
    else:  #154 (line in Coconut source)
        effect_text = spell_node.find('effect').text  #155 (line in Coconut source)
    return _coconut_tail_call(Spell, name=spell_node.find("name").text, times_memorized=spell_node.find("times_memorized").text, spell_range=spell_node.find("range").text, casting_time=spell_node.find("castingtime").text, effect=effect_text, time_units=spell_node.find("times_unit").text, dc=spell_node.find("dc").text, target=spell_node.find("target").text, save_info=spell_node.find("saveinfo").text, duration=spell_node.find("duration").text, **kwargs)  #156 (line in Coconut source)


def parse_spells(root: ET.Element) -> list[Spell]:  #170 (line in Coconut source)
    spell_list = [create_spell_from_node(node) for node in _coconut_flatten(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: root.findall('spells/memorized_spells/racial_innate_memorized/spell'), lambda: root.findall('spells/memorized_spells/class_innate_memorized/spell'))))]  #171 (line in Coconut source)
    for spell_level_node in root.findall('spells/memorized_spells/spellbook/class/level'):  #175 (line in Coconut source)
        level = spell_level_node.attrib["number"]  #176 (line in Coconut source)
        for spell_node in spell_level_node.findall('spell'):  #177 (line in Coconut source)
            spell = create_spell_from_node(spell_node, level=level)  #178 (line in Coconut source)
            spell_list.append(spell)  #179 (line in Coconut source)
    return spell_list  #180 (line in Coconut source)


@_coconut_tco  #182 (line in Coconut source)
def parse_feats(root: ET.Element) -> _coconut.typing.Tuple[_coconut.typing.Tuple[str, str], ...]:  #182 (line in Coconut source)
    feats = []  #183 (line in Coconut source)
    for feat in root.findall('feats/feat'):  #184 (line in Coconut source)
        if feat.find('hidden').text == "F":  #185 (line in Coconut source)
            benefit = ""  #186 (line in Coconut source)
            if feat.find('benefit').text:  #187 (line in Coconut source)
                benefit = feat.find('benefit').text  #188 (line in Coconut source)
            else:  #189 (line in Coconut source)
                if feat.findall('description/para'):  #190 (line in Coconut source)
                    for para in feat.findall('description/para'):  #191 (line in Coconut source)
                        benefit += para.text + "<br><br>"  #192 (line in Coconut source)
                    benefit.removesuffix("<br><br>")  #193 (line in Coconut source)
                else:  #194 (line in Coconut source)
                    benefit = feat.find('description').text  #195 (line in Coconut source)
            feats.append((_coconut_mk_anon_namedtuple(('feat_name', 'feat_benefit'))(feat.find('name').text, benefit)))  #196 (line in Coconut source)
    return _coconut_tail_call(tuple, feats)  #197 (line in Coconut source)


@_coconut_tco  #199 (line in Coconut source)
def parse_resistances(root: ET.Element) -> _coconut.typing.Tuple[str, ...]:  #199 (line in Coconut source)
    resistances = []  #200 (line in Coconut source)
    for resistance in root.findall('resistances/resistance'):  #201 (line in Coconut source)
        resistances.append(resistance.text)  #202 (line in Coconut source)
    return _coconut_tail_call(tuple, resistances)  #203 (line in Coconut source)


def parse_special_qualities(root: ET.Element) -> _coconut.typing.Tuple[str, set(str), _coconut.typing.Tuple[str, str]]:  #205 (line in Coconut source)
    immunities = []  #206 (line in Coconut source)
    special_qualities = []  #207 (line in Coconut source)
    spell_like_abilities = ""  #208 (line in Coconut source)
    skipped_qualities = ['Bonus Feats', 'Outsider Traits', 'Resistance to']  #209 (line in Coconut source)
    for quality in root.findall('special_qualities/special_quality'):  #210 (line in Coconut source)
        name = quality.find('name').text  #211 (line in Coconut source)

        skip = False  #213 (line in Coconut source)
        for skipped_quality in skipped_qualities:  #214 (line in Coconut source)
            if skipped_quality in name:  #215 (line in Coconut source)
                skip = True  #216 (line in Coconut source)
        if skip:  #217 (line in Coconut source)
            continue  #218 (line in Coconut source)

        if 'Immunity to ' in name:  #220 (line in Coconut source)
            immunities.append(quality.find('aspect').text.removeprefix('Immunity: '))  #221 (line in Coconut source)
        elif 'Spell-Like Abilities' in name:  #222 (line in Coconut source)
            spell_like_abilities = quality.find('description').text  #223 (line in Coconut source)
        else:  #224 (line in Coconut source)
            text = ""  #225 (line in Coconut source)
            if quality.findall('description/para'):  #226 (line in Coconut source)
                for para in quality.findall('description/para'):  #227 (line in Coconut source)
                    text += para.text + "<br><br>"  #228 (line in Coconut source)
                text.removesuffix("<br><br>")  #229 (line in Coconut source)
            else:  #230 (line in Coconut source)
                text = quality.find('description').text  #231 (line in Coconut source)
            special_qualities.append((_coconut_mk_anon_namedtuple(('name', 'description'))(name, text)))  #232 (line in Coconut source)
    return spell_like_abilities, immunities, special_qualities  #233 (line in Coconut source)


def parse_weapon_proficiences(root: ET.Element) -> str:  #235 (line in Coconut source)
    return root.find("weapon_proficiencies").text  #236 (line in Coconut source)


def parse_xml(input_file) -> Character:  #238 (line in Coconut source)
    tree = ET.parse(input_file)  #239 (line in Coconut source)
    root = tree.getroot()  #240 (line in Coconut source)
    spell_like_abilities, immunities, special_qualities = parse_special_qualities(root)  #241 (line in Coconut source)
    char = Character(name=parse_name(root), alignment=parse_alignment(root), archetypes=parse_archetypes(root), char_classes=parse_classes(root), languages=parse_languages(root), movement=parse_movement(root), gold=parse_gold(root), curr_gold=parse_gold(root), stats=parse_stats(root), max_hp=parse_hp(root), current_hp=parse_hp(root), ac=parse_ac(root), initiative=parse_initiative(root), spell_resistance=parse_spell_resistance(root), skills=parse_skills(root), saving_throws=parse_saving_throws(root), melee=parse_melee(root), ranged=parse_ranged(root), cmb=parse_cmb(root), cmd=parse_cmd(root), weapons=parse_weapons(root), ranged_weapons=parse_ranged_weapons(root), damage_reduction=parse_damage_reduction(root), spells=parse_spells(root), level=parse_level(root), feats=parse_feats(root), resistances=parse_resistances(root), spell_like_abilities=spell_like_abilities, immunities=immunities, special_abilities=special_qualities, special_attacks=parse_special_attacks(root), weapon_proficiencies=parse_weapon_proficiences(root), conditional_st_modifiers=parse_conditional_st_modifier(root))  #242 (line in Coconut source)
    return char  #278 (line in Coconut source)
