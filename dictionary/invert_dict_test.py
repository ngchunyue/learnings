import pytest
from invert_dict import lunch_option

class test_is_inverted_dictionary():
    @pytest.mark.parametrize("input_dictionary, output",
                               [
                                   (lunch_option.keys(),invert_dict.inverted_lunch_option.values(), True)
                               ],
                               )
    
    def test_is_inverted(self, input_dictionary: dict, output: bool):
        assert invert_dict.lunch_option.keys() == output
                               