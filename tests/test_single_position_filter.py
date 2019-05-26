# Don't forget to write tests (python nose is installed)

import position_filter
import nose

def test_filter_solution_1():
    genome_data = [[5, "G"], [6, "A"], [7, "T"], [15, "G"], [19, "T"],
                   [20, "C"], [22, "T"]]
    filter_data = [[6, 7], [15, 20]]
    assert position_filter.filter_solution_1(
        genome_data, filter_data) == [[6, "A"], [15, "G"], [19, "T"]]


def test_filter_solution_2():
    genome_data = [[5, "GAT"], [15, "G"], [19, "TC"], [22, "T"]]
    filter_data = [[6, 7], [15, 20]]
    assert position_filter.filter_solution_2(
        genome_data, filter_data) == [[5, "GAT"], [15, "G"], [19, "TC"]]


def test_filter_solution_3():
    genome_data = [[5, "GAT"], [15, "G"], [19, "TC"], [22, "T"]]
    filter_data = [[6, 7], [15, 20]]
    assert position_filter.filter_solution_3(
        genome_data, filter_data) == [[6, "A"], [15, "G"], [19, "T"]]


def test_filter_solution_4():
    genome_data = [[5, "G"], [5, "T"], [10, "GTC"], [11, "AT"], [13, "ACA"]]
    filter_data = [[6, 7], [11, 13],[15, 20]]
    assert position_filter.filter_solution_4(
        genome_data, filter_data) == [[11, "T"], [11, "A"], [12, "C"], [12, "T"], [15, "A"]]
