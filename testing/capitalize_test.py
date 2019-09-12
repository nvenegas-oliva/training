
import capitalize
import pytest


def test_capital_case():
    assert capitalize.capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capitalize.capital_case(9)
