# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import algorithms.dp.buy_sell_stock as module_1
# import buy_sell_stock as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    list_0 = [object_0, object_0, object_0, object_0]
    module_1.max_profit_naive(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd4`\xcf"
    var_0 = module_1.max_profit_optimized(bytes_0)
    assert var_0 == 111
    dict_0 = {var_0: var_0, var_0: bytes_0}
    var_1 = module_1.max_profit_naive(dict_0)
    assert var_1 == 0
    module_1.max_profit_optimized(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "YL7<=v`Cp=tz\t"
    module_1.max_profit_optimized(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x8ci\xaf\xa1\xe1\xdap?n\xa5"
    var_0 = module_1.max_profit_optimized(bytes_0)
    assert var_0 == 120
    str_0 = "\x0b\t[o\tR6\x0b-;8"
    module_1.max_profit_optimized(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1878
    module_1.max_profit_naive(int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\nq\xe7\xe1\xd1\xa7"
    var_0 = module_1.max_profit_optimized(bytes_0)
    assert var_0 == 221
    var_1 = module_1.max_profit_optimized(bytes_0)
    assert var_1 == 221
    var_2 = module_1.max_profit_naive(bytes_0)
    assert var_2 == 221
    var_3 = module_1.max_profit_optimized(bytes_0)
    assert var_3 == 221
    module_1.max_profit_naive(var_1)
