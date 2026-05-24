import employee_info

def test_calculate_average_salary():
    result = 60166
    avg = employee_info.calculate_average_salary()
    assert result == avg

def test_get_employees_by_dept():
    result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    dept = employee_info.get_employees_by_dept("Sales")
    assert result == dept

def test_get_employees_by_age_range():
    result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
              {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
              {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
              ]
    range = employee_info.get_employees_by_age_range(26,36)
    assert range == result