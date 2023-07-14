import pytest
from invert_dict import lunch_option
from invert_dict import inverted_dictionary

class test_is_inverted_dictionary():
    @pytest.mark.parametrize("input, output",
                               [(lunch_option.values(), inverted_dictionary.keys()),
                                (lunch_option.keys(), inverted_dictionary.values()),
                                (lunch_option[i for i in range(len(lunch_option))], inverted_dictionary)
                               ],
                               )
    
    def test_is_inverted(self, input, output):
        assert isinstance(input, output)


                               