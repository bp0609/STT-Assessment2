# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dp.hosoya_triangle as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.hosoya(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.hosoya_testing(bool_0)
    module_0.hosoya_testing(var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.hosoya(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.hosoya(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.hosoya(var_0, var_0)
    assert var_1 == 1
    var_2 = module_0.print_hosoya(var_0)
    var_3 = module_0.print_hosoya(bool_0)
    var_4 = module_0.hosoya(bool_0, bool_0)
    assert var_4 == 1
    var_5 = module_0.hosoya_testing(bool_0)
    module_0.print_hosoya(var_3)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -193
    var_0 = module_0.print_hosoya(int_0)
    module_0.hosoya_testing(var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -412
    none_type_0 = None
    var_0 = module_0.hosoya_testing(int_0)
    module_0.print_hosoya(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    set_0 = set()
    module_0.hosoya_testing(set_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    none_type_0 = None
    module_0.hosoya(none_type_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    var_0 = module_0.hosoya(bool_0, bool_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.hosoya(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = True
    bool_1 = False
    var_0 = module_0.hosoya(bool_1, bool_0)
    assert var_0 == 0
    var_1 = module_0.hosoya(bool_0, bool_0)
    assert var_1 == 1
    str_0 = "mci:6\rjK\x0cawmr"
    module_0.hosoya_testing(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    int_0 = 5571
    int_1 = 3063
    module_0.hosoya(int_0, int_1)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "=L\x0c;$CQ~4Y>pOv{"
    module_0.hosoya(str_0, str_0)
