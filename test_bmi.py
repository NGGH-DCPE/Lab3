from Lab2 import bmi


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 50)  # low weight
    assert result == -1


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 65)  # normal range
    assert result == 0


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75, 90)  # high weight
    assert result == 1