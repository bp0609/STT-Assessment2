# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dp.combination_sum as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.combination_sum_bottom_up(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    object_0 = module_1.object(*list_0)
    module_0.combination_sum_bottom_up(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.combination_sum_topdown(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.combination_sum_topdown(bool_0, bool_0)
    assert var_0 == 1
    assert module_0.DP == [1]
    object_0 = module_1.object()
    object_1 = module_1.object()
    module_0.combination_sum_topdown(object_0, object_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.combination_sum_topdown(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.combination_sum_bottom_up(list_0, bool_0)
    assert var_0 == 3
    assert module_0.DP == [1, -1]
    none_type_0 = None
    module_0.combination_sum_topdown(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    none_type_0 = None
    bytes_0 = b"\x87\x89\x87\x15k\x92?Ad\tM"
    bool_1 = True
    var_0 = module_0.combination_sum_topdown(bytes_0, bool_1)
    assert var_0 == 0
    assert module_0.DP == [1, 0]
    module_0.combination_sum_bottom_up(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    var_0 = module_0.helper_topdown(bool_0, bool_0)
    assert var_0 == 1
    tuple_0 = (var_0,)
    var_1 = module_0.combination_sum_topdown(tuple_0, var_0)
    assert var_1 == 1
    assert module_0.DP == [1, 1]
    module_0.combination_sum_topdown(var_0, var_0)
