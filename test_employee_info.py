import employee_info

def test_calculate_average_salary():
    result = 60166
    avg = employee_info.calculate_average_salary()
    assert result == avg