import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Let's retrieve the column `salary`
    employees_salary = employees['salary']
    # The employee ID must be odd number, so we calculate the modulo (remainder) of each value in the
    # "employee_id" column.
    employees_id = (employees['employee_id'] % 2)
    # At the same time, the employee's name does not start with the character 'M',
    employees_name = (employees['name'].str.startswith('M') == False)
    # We filter rows in a DataFrame called employees based on a condition related to the "name" column. So we
    # need  a Boolean Series where each element is True if the corresponding employee's name does not start with
    #   'M,' and False if it starts with 'M'.
    employees['bonus'] = employees_salary * employees_id * employees_name
    # Then, we  sort the values in the "employee_id" column in ascending order.
    sorted_employees = employees.sort_values('employee_id')
    # Finally, we retrieve only the "employee_id" and "bonus" columns from the DataFrame and displays those
    # columns as a new DataFrame or Series
    new_bonus = sorted_employees[['employee_id', 'bonus']]

    return new_bonus


data = [
    [2, 'Meir', 3000],
    [3, 'Michael', 3800],
    [7, 'Addilyn', 7400],
    [8, 'Juan', 6100],
    [9, 'Kannon', 7700]
]
employees = (
    pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).
    astype({'employee_id': 'int64', 'name': 'object', 'salary': 'int64'}))

print(calculate_special_bonus(employees))
