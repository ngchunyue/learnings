import pytest

from .invert_dict import lunch_option
from .invert_dict import inverted_dictionary

# class test_is_inverted_dictionary():
#     @pytest.mark.parametrize("input, output",
#                              [(lunch_option.keys(), inverted_dictionary.values()),
#                               (lunch_option.values(), inverted_dictionary.keys())])
    
#     def test_is_inverted(self, input, output):
#         assert input == output


# @pytest.mark.parametrize("input, output",
#                          [(lunch_option, inverted_dictionary)]
#                           )

# class TestIsInverted():
#     def is_inverted(self, input, output):
#         assert input.keys() == output.values()

class test_is_inverted_dictionary():
    @pytest.mark.parametrize("input, output",
                             [(lunch_option, inverted_dictionary)])
    
    def TestIsInverted(self, input, output):
        assert input.keys() == output.values()