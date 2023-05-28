from random import random

from factory import Factory
import pandas as pd
import factory


class CompanyFactory(Factory):
    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int', min=24, max=50)
    position = factory.Faker('random_element', elements=('Software Engineer', 'Software Developer', 'Product Manager',
                                                         'Project Manager', 'Data Analysts', 'Python Developer',
                                                         'Front End Developer', 'QA Engineer'))
    salary = factory.Faker('random_int', min=500, max=5500)
    work_experience = factory.Faker('random_int', min=1, max=15)


num_rows = 50

employees = CompanyFactory.create_batch(num_rows)

for employee in employees:
    if random() < 0.1:
        employee['first_name'] = None
    if random() < 0.1:
        employee['position'] = None
    if random() < 0.1:
        employee['salary'] = -1 * employee['salary']

df = pd.DataFrame(employees)

df.to_csv('employee_record.csv', index=False)

print(df)