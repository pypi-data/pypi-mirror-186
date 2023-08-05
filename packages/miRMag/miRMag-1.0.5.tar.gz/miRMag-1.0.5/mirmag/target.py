#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from anytree import Node, RenderTree    # https://anytree.readthedocs.io ; https://github.com/c0fec0de/anytree
from typing import Tuple, List, Set

from mirmag.energy import Energy
from mirmag.logger import get_logger
from mirmag.utils import are_complementary


logger = get_logger(logger_name="target", log_to_console=False)


SLIDING_WINDOW = 22     # nt, максимальное расстояние между началами первой и последней спиралей в одной структуре
MAX_SHIFT = 0           # nt, максимальное отклонения начала мишени от начала микроРНК внутри микроРНК.
MAX_VARIABILITY = 2     # nt, Максимальное отклонение от "нулевой" спирали при выполнении алгоритма "вырезания" строк и столбцов.
TAU = 3                 # величина концентрации микроРНК в каждой позиции мРНК.


class Target:
    """ Класс для описания одной мишени (местоположения взаимодействия микроРНК и мРНК).

        Нумерации позиций в последовательностях с нуля, в направлении взаимодействия:
        Для микроРНК нумерация от 5' к 3' концу, для мРНК - от 3' к 5' концу.

        Пример взаимодействия:
        Номер позиции            0      ->     14
        микроРНК:           5'   xxCUGCAUACUUCxx  3'
                                 |||||||||||
        мРНК:               3'   xxGAUGUAUGAAGxx  5'
        Номер позиции            0      ->     14
    """

    def __init__(self, mirna_begin: int, mirna_end: int, mrna_rbegin: int, mrna_rend: int, energy: float, seed_type: str):
        """ Инициализация объекта параметрами (энергией и позициями в микроРНК и в мРНК).

            Важно! Нумерация позиций в микроРНК начинается с 5' края последовательности.
            Важно! Нумерация позиций в мРНК начинается с 3' края последовательности.
            Важно! Нумерация позиций - "программистская", т.е. начинается с нуля и не должна включать последнюю позицию.

        :param mirna_begin: начало мишени в микроРНК (отсчет с 5' края последовательности).
        :param mirna_end: конец мишени в микроРНК (не включая эту позицию).
        :param mrna_rbegin: начало мишени в мРНК (отсчет с 3' края последовательности).
        :param mrna_rend: конец мишени в мРНК (не включая эту позицию).
        :param energy: энергия взаимодействия мРНК и микроРНК.
        :param seed_type: offset_6mer (positions 2-8), 6mer (1-7), 7mer-a1 (A+1-7), 7mer-m8 (1-8), 8mer (A+1-8).
        """

        if mirna_begin is None or mirna_end is None or mrna_rbegin is None or mrna_rend is None:
            logger.warning(f"Выполнена инициализация объекта Target некорректными данными.\n"
                           f"mirna_begin: '{mirna_begin}', mirna_end: '{mirna_end}'"
                           f"mrna_rbegin: '{mrna_rbegin}', mrna_rend: '{mrna_rend}'.")

        self.mirna_begin = mirna_begin
        self.mirna_end = mirna_end
        self.mrna_rbegin = mrna_rbegin
        self.mrna_rend = mrna_rend
        self.energy = energy or Energy().MAX_ENERGY
        self.seed_type = seed_type or "None"

    def __str__(self):
        return f"Target: {self.mirna_begin} / {self.mirna_end} / {self.mrna_rbegin} / {self.mrna_rend} / {self.energy} / {self.seed_type}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.mirna_begin == other.mirna_begin and self.mirna_end == other.mirna_end and
                self.mrna_rbegin == other.mrna_rbegin and self.mrna_rend == other.mrna_rend and
                self.energy == other.energy and self.seed_type == other.seed_type)

    def __hash__(self):
        return hash(self.__str__())

    def shift_mrna_positions(self, i):
        self.mrna_rbegin += i
        self.mrna_rend += i

    def get_mirna_positions(self) -> Tuple[int, int]:
        """ Return tuple of begin and end of the Target in the miRNA. """
        return self.mirna_begin, self.mirna_end

    def get_mrna_positions(self) -> Tuple[int, int]:
        """ Return tuple of begin and end of the Target in the reversed mRNA. """
        return self.mrna_rbegin, self.mrna_rend

    def get_energy(self) -> float:
        return self.energy

    def get_seed_type(self) -> str:
        return self.seed_type


def get_max_target(target1: Target, target2: Target) -> Target:
    """ Сравнение позиций двух мишеней и выбор одной с наиболее широкими границами в микроРНК и мРНК??? """
    # TODO: пока непонятно как считать и что в итоге выдавать?
    return Target(-1, -1, -1, -1, 0, "")


# -------------------------------------------------------------------------------------------------------------------- #


def get_complementary_targets(mirna: str, mrna: str, seed_types: list = None, allow_gu_pairs: bool = True) -> List[Target]:
    """ Функция поиска сайтов связывания в мРНК (инвертированных участков, комплементарных сид-региону микроРНК).

        Важно! Связывание мРНК и микроРНК происходит в противоположных направлениях: 5'→3' (микроРНК) к 3'→5' (мРНК).
        Важно! Позиция в мРНК - это позиция с 3' края (позиция относительно 'конца' последовательности мРНК).
        В этой функции не считается энергия получившегося взаимодействия, задается ее фиксированное значение = MAX_ENERGY.
        В вычислении комплементарности по дефолту учитываются комплементарные GU-пары.
        The calculation is case insensitive.

        Рассматриваются разные возможные взаимодействия (типы сидов), канонический - это 6mer.
        Все варианты: offset_6mer (позиции 2-8), 6mer (1-7), 7mer-a1 (A+1-7), 7mer-m8 (1-8), 8mer (A+1-8).

    :param mirna: miRNA nucleotide sequence.
    :param mrna: mRNA nucleotide sequence.
    :param seed_types: List of the types of seeds to search or None to search without limits.
    :param allow_gu_pairs: True (consider GU pair as complementary), False (does not consider).
    :return: List of Target-objects, they contain data (mirna_begin, mirna_end, mrna_rbegin, mrna_rend, MAX_ENERGY, seed_type).
    """

    # Check input sequences
    if not mrna or not mirna:
        logger.error(f"Complementary target search was requested for empty sequence(s) or for None object(s).\n"
                     f"mRNA sequence: '{mrna}', miRNA sequence: '{mirna}'.")
        return []

    # Get inverted mRNA sequence
    inverted_mrna = mrna[::-1]

    seeds = []
    if seed_types:
        for seed in seed_types:
            if seed.lower() == "offset_6mer":
                seeds.append((2, 8, mirna[2:8], "offset_6mer"))
            if seed.lower() == "6mer":
                seeds.append((1, 7, mirna[1:7], "6mer"))
            if seed.lower() == "7mer-m8":
                seeds.append((1, 8, mirna[1:8], "7mer-m8"))
            if mirna[0] == "A" and seed.lower() == "7mer-a1":
                seeds.append((0, 7, mirna[0:7], "7mer-A1"))
            if mirna[0] == "A" and seed.lower() == "8mer":
                seeds.append((0, 8, mirna[0:8], "8mer"))
    else:
        seeds = [(2, 8, mirna[2:8], "offset_6mer"), (1, 7, mirna[1:7], "6mer"), (1, 8, mirna[1:8], "7mer-m8")]
        if mirna[0] == "A":
            seeds += [(0, 7, mirna[0:7], "7mer-A1"), (0, 8, mirna[0:8], "8mer")]

    # Calculations: get target and compare it with inverted seed
    targets = []
    for position in range(len(inverted_mrna) - 6):
        for seed in seeds:
            begin = seed[0]
            end = seed[1]
            seed_seq = seed[2]
            seed_type = seed[3]
            #
            target = inverted_mrna[position: position + len(seed_seq)]
            if are_complementary(target, seed_seq, allow_gu_pairs):
                targets.append(Target(begin, end, position, position + len(seed_seq), Energy().MAX_ENERGY, seed_type))

    #
    return targets


# -------------------------------------------------------------------------------------------------------------------- #


def get_sorted_helixes_list_with_energies(rna1: str, rna2: str) -> List[tuple]:
    """ Функция возвращает сортированный список всех возможных спиралей и их энергий для РНК1/РНК2-взаимодействия.

        Функция формирует все возможные спирали и их энергии для РНК1 (микроРНК) и РНК2 (мРНК) включая спирали длинной 1нт.
        В результат выдается список, отсортированный по позиции в РНК1 (а потом - по позиции в РНК2).
        Важно! Направление мРНК (РНК2) должно быть заранее установлено обратным направлению микроРНК (РНК1).
        GU-пары запрещены! Их нет в таблице энергий!

        1. Строится матрица всех комплементарных взаимодействий двух последовательностей:
            - ----- РНК_1 -----
            - |1000000000000000
            - |0100000000000000
            - |0010001110000000
            Р |0000000011000000
            Н |0000000000000000
            К |0000000000000000
            - |0001000000100000
            2 |0000110000010000
            - |0000011000011000
            - |0000001100000000
        2. Из матрицы выбираются все участки единиц, располагающиеся последовательно на одной диагонали (это спирали).
        3. Вычисляются данные о длине спирали и ее местоположении в РНК_1 (микроРНК) и в РНК_2 ([инвертированной] мРНК).
        4. Сортируется список спиралей, вычисляется их энергия и возвращается как результат.

    :param rna1: the first RNA sequence (miRNA).
    :param rna2: the second RNA sequence ([inverted] mRNA).
    :return: list of tuples (rna1_pos, rna2_pos, helix_length, helix_energy).
    """

    # Check input sequences
    if not rna1 or not rna2:
        logger.error(f"Sorted helixes were requested for empty sequence(s) or for None object(s).\nFirst sequence: '{rna1}', second sequence: '{rna2}'.")
        return []

    # Prepare input data to uniform view
    rna1 = rna1.upper().replace("T", "U")
    rna2 = rna2.upper().replace("T", "U")

    # Create and fill array of stems # оси X/Y выбраны таким образом, чтобы представление было как на примере выше
    m = len(rna2)
    n = len(rna1)
    arr = np.zeros((m, n), int)

    # Fill array by 1 in complementary positions
    for i in range(m):
        for j in range(n):
            if are_complementary(rna2[i], rna1[j], allow_gu_pairs=False):  # Here GU-pair DOES NOT allow!
                arr[i, j] = 1

    # print and check array
    # print(5 * "***")
    # logger.info(str(arr))
    # print(5 * "***")

    # Form list of all possible helixes: tuples (mirna_pos, mrna_pos, length)
    all_helixes = []
    for i in range(m):
        for j in range(n):
            if arr[i, j] == 1:
                length = 0      # Calculate length of a single helix
                for (ii, jj) in zip(range(i, m), range(j, n)):
                    if arr[ii, jj] == 1:
                        length += 1
                    else:
                        break
                #
                all_helixes.append((i, j, length))

    # print and check
    # logger.info(str(all_helixes))

    # Form list of non-overlapped helixes (select the ones with max length)
    result_helixes = []
    for new_hel in all_helixes:
        need_add = True
        for ind, old_hel in enumerate(result_helixes):
            if old_hel[0] - old_hel[1] == new_hel[0] - new_hel[1]:      # две спирали на одной диагонали?
                if old_hel[0] < new_hel[0] < old_hel[0] + old_hel[2]:   # кандидат является частью существующей спирали?
                    need_add = False                                    # ничего не делаем
                    break
                if new_hel[0] < old_hel[0] < new_hel[0] + new_hel[2]:   # кандидат содержит в себе существующую спираль?
                    result_helixes[ind] = new_hel                       # заменяем существующую спираль на кандидата
                    need_add = False                                    # больше ничего не делаем
                    break
        if need_add:
            result_helixes.append(new_hel)

    # print and check
    # logger.info(str(result_helixes))

    # Calculate the energies of all helixes and add them to the result_helixes
    for ind, value in enumerate(result_helixes):
        i, j, length = value
        if i + length == m or j + length == n:
            # Если спираль примыкает к границе РНК1 или РНК2 - спираль рассматривается БЕЗ +1нт от петли
            s2 = rna2[i: i + length]
            s1 = rna1[j: j + length]
        else:
            # Если спираль не примыкает к границе РНК1 или РНК2 - спираль рассматривается С +1нт от петли
            s2 = rna2[i: i + length + 1]
            s1 = rna1[j: j + length + 1]

        # Формируем результат, меняем порядок позиций РНК2 и РНК1, удаляем спирали 1нт длины, включаем энергию спирали.
        if len(s1) != 1 and len(s2) != 1:
            result_helixes[ind] = (j, i, length, Energy().get_helix_energy(s1, s2))
        else:
            result_helixes[ind] = (j, i, length, Energy().MAX_ENERGY)

    # Keep the helixes with correct energies (less than MAX_ENERGY divided by 2)
    result_helixes = [helix for helix in result_helixes if helix[3] <= Energy.MAX_ENERGY / 2.0]

    # Возврат отсортированного списка-результата
    return sorted(result_helixes)


def get_energy_of_one_structure(sorted_helixes: List[tuple]) -> float:
    """ Вычисление энергии одной структуры по её сортированному списку спиралей (и петель).

        Важно! Список спиралей должен быть отсортирован по позиции спирали [в РНК1], иначе вычисление будет некорректно.
        Важно! Спирали не должны "пересекаться", т.е. одна позиция не участвует в нескольких связях, позиции идут последовательно.

        Энергия структуры вычисляется как суммарная энергия всех спиралей, боковых и внутренних петель.
        Каждый элемент списка описывает одну спираль: (позиция в 5'→3' РНК_1, позиция в 3'→5' РНК_2, длина, энергия).
        Например: [(254, 11, 2, -4.2), (262, 18, 3, -3.17), ...]
        Стандартно, позиция в РНК_1 - отсчет ведется с 5' конца, позиция в РНК_2 - отсчет ведется с 3' конца.
        Энергия спиралей должна быть посчитана заранее и передана в явном виде.

    :param sorted_helixes: Сортированный список спиралей, описывающий структуру взаимодействия РНК_1 и РНК_2.
                           Список кортежей вида: (rna1_pos, rna2_pos, helix_length, helix_energy).
    :return: Значение полной свободной энергии вторичной структуры.
    """

    try:
        curr_helix = sorted_helixes[0]      # Информация о первой спирали
        energy = curr_helix[3]              # Энергия первой спирали

        for nxt_helix in sorted_helixes[1:]:
            energy += nxt_helix[3]
            up = nxt_helix[0] - (curr_helix[0] + curr_helix[2])
            dw = nxt_helix[1] - (curr_helix[1] + curr_helix[2])
            if up == 0 or dw == 0:
                energy += Energy().get_bulge_loop_energy(up + dw)
            else:
                energy += Energy().get_internal_loop_energy(up + dw)
            curr_helix = nxt_helix

        return energy

    except Exception:
        logger.exception(f"Ошибка при вычислении свободной энергии структуры по её списку спиралей.\nСписок спиралей для структуры: '{sorted_helixes}'.")
        return Energy().MAX_ENERGY


def get_target_from_helixes_list(sorted_helixes: List[tuple]) -> Target:
    """ Построение объекта-мишени по сортированному списку спиралей, описывающих взаимодействия микроРНК и мРНК.

        Важно! Нумерация позиций в мРНК должна начинаться с 3' края последовательности (3'→5').

    :param sorted_helixes: Список спиралей вида [(mirna_begin, mrna_rbegin, helix_length, helix_energy), ...].
    :return: Target object.
    """

    if not sorted_helixes:
        logger.error(f"Target was trying to be created with empty/none helixes list. Helixes list: '{sorted_helixes}'.")
        return Target(-1, -1, -1, -1, Energy.MAX_ENERGY, "-")

    else:
        mirna_begin = sorted_helixes[0][0]
        mrna_rbegin = sorted_helixes[0][1]
        mirna_end = sorted_helixes[-1][0] + sorted_helixes[-1][2]       # Вычисление по окончанию последней спирали
        mrna_rend = sorted_helixes[-1][1] + sorted_helixes[-1][2]       # Вычисление по окончанию последней спирали
        energy = get_energy_of_one_structure(sorted_helixes)
        return Target(mirna_begin, mirna_end, mrna_rbegin, mrna_rend, energy, "energy")


def build_tree_of_helixes(sorted_helixes: list, parent_node: Node, leafs_storage: list, store_all_leafs: bool = False, mir_pos: int = -1, m_pos: int = 0):
    """ Функция строит дерево всех возможных структур (непересекающихся спиралей) и формирует список листов этого дерева.

        Рекурсивная функция, которая строит дерево с учетом взаимной непересекаемости спиралей в структурах.
        Также заполняет список всех листьев дерева (для построения всех возможных путей от корня к листу).
        Для построения дерева используется модуль anytree: https://github.com/c0fec0de/anytree
        Важно: считается, что большие петли увеличивают энергию, поэтому добавление спиралей идет последовательно:
        к сформированным структурам добавляется ближайшая спираль и т.д.
        Важно: в дальнейшем поиск осуществляется в окне, начало микроРНК должно быть максимально близко к началу окна в мРНК.

    :param sorted_helixes: Список спиралей [(mirna_pos, mrna_rpos, helix_length, helix_energy), ...].
    :param parent_node: Родительский узел, к нему добавляются дочерние узлы (спирали).
    :param leafs_storage: Список для хранения узлов-листьев дерева.
    :param store_all_leafs: True (Считаем каждый лист конечным), False (конечный лист тот, который реально последний).
    :param mir_pos: позиция в микроРНК.
    :param m_pos: позиция в мРНК.
    :return: None. Результатом работы будет построеное дерево и список листьев-узлов.
    """

    s_part, e_part = [], []

    if sorted_helixes:
        if mir_pos == -1 and m_pos == -1:                               # Это первый шаг алгоритма
            s_part = [x for x in sorted_helixes if x[0] <= MAX_SHIFT]   # Выбор всех спиралей с началами миРНК <= MAX_SHIFT
            e_part = [x for x in sorted_helixes if x[0] > MAX_SHIFT]    # Все оставшиеся спирали, с началами миРНК > MAX_SHIFT
        else:
            s_part = [x for x in sorted_helixes if x[0] - mir_pos <= MAX_VARIABILITY and x[1] - m_pos <= MAX_VARIABILITY]
            e_part = [x for x in sorted_helixes if x[0] - mir_pos > MAX_VARIABILITY or x[1] - m_pos > MAX_VARIABILITY]

    for elm in s_part:
        nd = Node(str(elm), parent=parent_node)
        hels = [x for x in e_part if x[0] >= elm[0] + elm[2] and x[1] >= elm[1] + elm[2]]   # Взаимная непересекаемость

        if not hels:                    # Узел - конечный
            leafs_storage.append(nd)
        else:
            build_tree_of_helixes(hels, nd, leafs_storage, store_all_leafs, elm[0] + elm[2], elm[1] + elm[2])
            if store_all_leafs:         # Берем каждый промежуточный лист как конечный?
                leafs_storage.append(nd)


def get_targets_for_helixes_list(sorted_helixes: list, allowed_shift_of_helix: int = 0, use_1nt_helix: bool = True,
                                 store_all_leafs: bool = True, get_one_best_target: bool = False) -> List[Target]:
    """ Вычисление всех возможных мишеней по заданному списку спиралей.

        1. Требование не_точного совпадения начала мишени с началом (в мРНК) первой спирали.
        2. Настраиваемое использование 1нт спиралей в вычислении.
        3. Использовать только часть спиралей или все возможные вариации.
        4. Получение одной спирали с наименьшей энергией.

    :param sorted_helixes: sorted list of tuples (rna1_pos, rna2_pos, helix_length, helix_energy).
    :param allowed_shift_of_helix: Допустима первая спираль на таком расстоянии от начала rna1 (miRNA).
    :param use_1nt_helix: True (использовать в вычислении 1нт спирали), False (Не использовать).
    :param store_all_leafs: True (Считаем каждый лист конечным), False (конечный лист тот, который реально последний).
    :param get_one_best_target: True (return only the best Target withыв min energy), False (return all targets).
    :return: Список Мишеней.
    """

    # Удаление из рассмотрения тех спиралей, длина которых 1нт [Опционально]
    if not use_1nt_helix:
        sorted_helixes = [hel for hel in sorted_helixes if hel[2] > 1]

    if not sorted_helixes:
        logger.error(f"Targets was trying to be searched with 1nt/empty/none list of helixes.\nList of helixes: {sorted_helixes}.")
        return []

    # Проверка, что в позициях микроРНК <= allowed_shift_of_helix есть спираль. Иначе возвращать пустой список [Опционально]
    # print(sorted_helixes[0][0])
    if sorted_helixes[0][0] > allowed_shift_of_helix:
        logger.error(f"Начало мишени располагается далеко от начала первой спирали.\nList of helixes: {sorted_helixes}.")
        return []

    # Построение всех возможных комбинаций спиралей без взаимных пересечений и всех возможных листьев дерева
    leafs_storage = []
    root_node = Node("root_node")
    build_tree_of_helixes(sorted_helixes, root_node, leafs_storage, store_all_leafs=store_all_leafs)

    # Check: Напечатать построенное дерево и список листьев
    # for pre, fill, node in RenderTree(root_node):
    #     print("%s%s" % (pre, node.name))
    # print("leafs\t", leafs_storage)

    # Построение списка всех возможных структур, вычисляя путь в дереве от корня к каждому листу
    result = []
    for leaf in leafs_storage:
        leaf = str(leaf)[17:-2]                 # Такая форма нужна для правильного парсинга вывода str(leaf)
        a = [eval(x) for x in leaf.split("/")]
        a = get_target_from_helixes_list(a)     # convert to target and calculate energy
        result.append(a)
    logger.info(f"Все вычисленные мишени с энергиями:\t{result}")

    # Вычисление одной мишени и ее минимальной энергии связывания
    if result and get_one_best_target:
        result = [min(result, key=lambda x: x.get_energy())]

    # Return result
    return result


def get_energy_targets(mirna: str, mrna: str, energy_limit: float = Energy().MAX_ENERGY) -> Set[Target]:
    """ Поиск мишеней, энергия взаимодействия которых меньше заданного лимита.

        Для каждой позиции заданной мРНК вычисляются все взаимодействия (с энергией меньше лимита),
        которые могут быть в интервале мРНК [position, position + MAX_DISTANCE].

        Важно: последовательность мРНК должна быть инвертирована.
        Важно: допустимое отклонение начал микроРНК и части мРНК = MAX_SHIFT.

    :param mirna: miRNA sequence.
    :param mrna: mRNA sequence.
    :param energy_limit: если энергия структуры (взаимодействия с мишенью) меньше лимита - берем в результат.
    :return: список Target objects.
    """

    result = set()
    #
    for i in range(len(mrna) - SLIDING_WINDOW):
        sorted_helixes = get_sorted_helixes_list_with_energies(mirna, mrna[i: i + SLIDING_WINDOW])
        targets = get_targets_for_helixes_list(sorted_helixes=sorted_helixes, allowed_shift_of_helix=MAX_SHIFT, use_1nt_helix=True, store_all_leafs=True, get_one_best_target=False)

        for target in targets:
            if target.get_energy() < energy_limit:
                target.shift_mrna_positions(i)
                result.add(target)
    #
    return result


# -------------------------------------------------------------------------------------------------------------------- #


def get_partition_function(mirna: str, mrna: str) -> None:
    """ Вычисление энергии для каждой позиции мРНК в предположении, что миРНК начинается с этой позиции.

    :param mirna:
    :param mrna:
    :return:
    """

    # energies = []
    # for i in range(len(mrna) - SLIDING_WINDOW):
    #     sorted_helixes = get_sorted_helixes_list_with_energies(mirna, mrna[i: i + SLIDING_WINDOW])
    #     targets = get_targets_for_helixes_list(sorted_helixes=sorted_helixes, allowed_shift_of_helix=MAX_SHIFT,
    #                                            use_1nt_helix=True, store_all_leafs=True, get_one_best_target=False)
    #
    #     # TODO: учитывать позицию.
    #     if targets:
    #         ee = min(targets, key=lambda x: x.get_energy())
    #         ee.shift_mrna_positions(i)
    #         print(i, ee)
    #         energies.append(ee.get_energy())
    #     else:
    #         energies.append(Energy.MAX_ENERGY)
    #         print(i, Target(-1, -1, -1, -1, Energy().MAX_ENERGY, "energy"))

    # Подсчет энергий
    # TODO: поиск точного совпадения первых позиций миРНК и мРНК. Иначе что-то не так.
    energies = []
    #
    for i in range(len(mrna) - SLIDING_WINDOW):
        sorted_helixes = get_sorted_helixes_list_with_energies(mirna, mrna[i: i + SLIDING_WINDOW])
        targets = get_targets_for_helixes_list(sorted_helixes=sorted_helixes, allowed_shift_of_helix=MAX_SHIFT, use_1nt_helix=True, store_all_leafs=True, get_one_best_target=True)
        if targets:
            energies.append(targets[0].get_energy())
        else:
            energies.append(Energy().MAX_ENERGY)



    # Индексы 0, 1, ..., N
    # energies = 22 * [0.0] + [-1.0, -2, -2, -2, -1, 0, -10, -11, -10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] + 22 * [1.0]
    energies = [0.000001 * math.exp(-elm/(310.15 * 1.987 * 0.001)) for elm in energies] # https://en.wikipedia.org/wiki/Boltzmann_constant
    N = len(energies)
    m = len(mirna)
    
    # Correction positions to the +1
    energies = [0.0] + energies + [0.0]

    # Используемые индексы 0, 1, 2, ..., N
    F = [1] * (N + 2)
    for i in range(N + 1):
        if i < m:
            F[i] = 1
        else:
            F[i] = F[i - 1] + F[i - m] * TAU * energies[i - m + 1]

    # Используемые индексы 1, ..., N + 1
    R = [1] * (N + 2)
    for i in range(N + 1, 0, -1):
        if i <= N - m + 1:
            R[i] = R[i + 1] + R[i + m] * TAU * energies[i]
        else:
            R[i] = 1

    # Используемые индексы 1, 2, ..., N - m + 1
    P = [0] * (N + 2)
    for i in range(1, N - m + 2):
        if R[1] != 0:
            P[i] = F[i - 1] * TAU * energies[i] * R[i + m] / R[1]

    # Используемые индексы m, m + 1, ..., N - m + 1
    P_sum = [0] * (N + 2)
    for i in range(0, N + 2):
        if i < m:
            P_sum[i] = sum(P[0: i + 1])
        elif i < N - m + 2:
            P_sum[i] = sum(P[i + 1 - m: i + 1])
        else:
            P_sum[i] = sum(P[i: N+1])

    # Нарисовать суммы в качестве результата на интервале [m; N - m + 1]
    fig, axs = plt.subplots(4)
    axs[0].plot(P_sum[::-1])
    axs[1].plot(P[::-1])
    axs[2].plot(F[::-1])
    axs[2].set_yscale('log')
    axs[3].plot(R[::-1])
    axs[3].set_yscale('log')
    plt.xlabel("Позиция в мРНК")

    axs[0].xaxis.set_major_locator(ticker.MultipleLocator(50))
    axs[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
    axs[1].xaxis.set_major_locator(ticker.MultipleLocator(50))
    axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(10))

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()







if __name__ == "__main__":
    """ Examples / Use cases. """

    # # Find complementary targets
    # # +offset_6mer (positions 2-8), +6mer (1-7), +7mer-a1 (A1-7), +7mer-m8 (1-8), +8mer (A1-8)
    # mrna = "XXXXXACGUACGUYYYYYYYYACGUACGTZZZZZZZZZ"
    # mirna = "ACGTACGTXXX"   # CGUACGU | ACGTACG
    # print(*get_complementary_targets(mirna, mrna), sep="\n")
    # print("*" * 10)
    # print(*get_complementary_targets(mirna, mrna, seed_types=["offset_6mer", "7mer-a1"]), sep="\n")


    # # Find all helixes and their energies
    # inverted_mrna = "gtatatttttacctcaat"[::-1]
    # mirna = "UGAGGUAGUAGGU"
    # sorted_helixes = get_sorted_helixes_list_with_energies(mirna, inverted_mrna)
    # print(sorted_helixes)


    # # Find energy of the one structure and get Target from the helixes list
    # sorted_helixes = [(0, 0, 2, -2), (4, 2, 2, -3), (7, 5, 2, -5)]
    # print(get_energy_of_one_structure(sorted_helixes))
    # print(get_target_from_helixes_list(sorted_helixes))


    # inverted_mrna = "gtatatttttacctcaat"[::-1]
    # mirna = "UGAGGUAGUAGGU"
    # sorted_helixes = get_sorted_helixes_list_with_energies(mirna, inverted_mrna)
    # print(sorted_helixes)
    # ttt = get_targets_for_helixes_list(sorted_helixes=sorted_helixes, allowed_shift_of_helix=3, use_1nt_helix=True,
    #                                    store_all_leafs=True, get_one_best_target=False)
    # print(ttt)


    #
    #
    # print("*********")
    #
    # mrna =  "UCAUCCAUUAUCUUGGCUGUGAGCUCCUUGGGUACGGGUACCUUGUAUGUUUACUUUUAUAUCCCUAGCACAAAGCAAGUGCCUGGCACAUAGU" * 10
    # inverted_mirna = "aacccguagauccgaacuugug"[::-1]


    # import time
    # begin = time.time()
    inv_mrna = ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaagaaaatggctaataaactgtattaaatcttaaacaatgtataaagattgtactta" * 2)[::-1]
    # mirna = "CUAUACAAUCUACUGUCUUUC"
    # for val in get_energy_targets(mirna, inv_mrna, energy_limit=-7):
    #     print(val)
    # print(time.time() - begin)



    # aaatattata tttaTACCTC Atgtatattt tTACCTCAat
    #inv_mrna = ("ttcatactggaaagaaaccctacaaatgtgaagaatgtggcaaagcttttaacaattcctcaacccttaggaaacataagataatttatactgggaagaaaccatacaaatgtgaagaatgtggcaaagcttttaagcagtcctcacaccttactagacataaagcagttcatactgggg")[::-1]
    # inv_mrna = ("A" * 50 + "GGGGGGGGGGG" + "A" * 50)[::-1]
    mirna = "CUAUACAAUCUACUGUCUUUC"
    get_partition_function(mirna, inv_mrna)


    '''

    init_energy_table()
    mrna =  "AACCGGUU"
    inverted_mirna = "AACCGGUU"[::-1]
    #mrna =  "UCAUCCAUUAUCUUGGCUGUGAGCUCCUUGGGUACGGGUACCUUGUAUGUUUACUUUUAUAUCCCUAGCACAAAGCAAGUGCCUGGCACAUAGU"
    #inverted_mirna = "aacccguagauccgaacuugug"[::-1]

    print(get_sorted_helixes_list(mrna, inverted_mirna))
    

    
    for ind, val in enumerate(find_energy_targets(mrna, inverted_mirna)):
        print(ind, '\t', val)

    
    import matplotlib.pyplot as plt
    import pylab



    xax = []
    yas = []
    for ind, val in enumerate(find_energy_targets(mrna, mirna)):
        if val.energy < MAX_ENERGY / 2:
            xax.append(ind)
            if val.energy > 0:
                yas.append(0.0)
            else:
                yas.append(val.energy)


    pylab.plot(xax, yas)
    pylab.show()

    xax = []
    yas = []

    for ind, val in enumerate(get_mirna_concentration(mrna, mirna, 3)):
        xax.append(ind)
        yas.append(val)




    pylab.plot(xax, yas)
    pylab.show()
    


    print()
    print("Structure energy.")
    print("Empty list:", get_energy_of_one_structure([]))
    print("Correct list:", get_energy_of_one_structure([(0, 0, 5, -5), (10, 5, 5, -6), (20, 15, 5, -7)]))
    '''
