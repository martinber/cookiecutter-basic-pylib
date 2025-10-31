from {{ cookiecutter.__project_name_snake }} import {{ cookiecutter.__project_name_snake }}


def test_sum():
    assert {{ cookiecutter.__project_name_snake }}.sum_numbers(1, 2) == 3
