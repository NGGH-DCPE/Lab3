import price_info

def test_total_cost_shopping():
    actual_cost = 46.75
    total_cost = price_info.total_cost_shopping()
    assert float(actual_cost) == float(total_cost)

def test_cost_of_fruit():
    test_cost = 12.0
    act_cost = price_info.cost_of_fruits('apple', 10)
    assert float(act_cost) == float(test_cost)
