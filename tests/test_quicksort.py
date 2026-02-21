import copy

from src.quicksort_deterministic import quicksort as det_quicksort
from src.quicksort_randomized import randomized_quicksort

def test_sorted_array():
    arr = [5, 3, 1, 4, 2]
    expected = sorted(arr)
    det_arr = copy.deepcopy(arr)
    rand_arr = copy.deepcopy(arr)
    det_quicksort(det_arr, 0, len(det_arr) - 1)
    randomized_quicksort(rand_arr, 0, len(rand_arr) - 1)
    assert det_arr == expected
    assert rand_arr == expected

def test_empty_array():
    arr = []
    expected = []
    det_arr = copy.deepcopy(arr)
    rand_arr = copy.deepcopy(arr)
    det_quicksort(det_arr, 0, len(det_arr) - 1)
    randomized_quicksort(rand_arr, 0, len(rand_arr) - 1)
    assert det_arr == expected
    assert rand_arr == expected

def test_single_element():
    arr = [42]
    expected = [42]
    det_arr = copy.deepcopy(arr)
    rand_arr = copy.deepcopy(arr)
    det_quicksort(det_arr, 0, len(det_arr) - 1)
    randomized_quicksort(rand_arr, 0, len(rand_arr) - 1)
    assert det_arr == expected
    assert rand_arr == expected