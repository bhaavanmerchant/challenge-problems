import unittest

import transformer

class TestTransformer(unittest.TestCase):


    def test__is_terminal_element_failure(self):
        self.assertFalse(transformer.Transformer()._is_terminal_element(['1','2','3'], '1'))

    def test__is_terminal_element_success(self):
        self.assertTrue(transformer.Transformer()._is_terminal_element(['1','2','3'], '3'))

    def test__is_terminal_element_exception(self):
        with self.assertRaises(IndexError):
            transformer.Transformer()._is_terminal_element([], '1')

    def test__get_cherry_picked_dict_success(self):
        dictionary = {
            'singer': 'Ed Sheeran',
            'song': 'Shape of You'
        }
        res = {
            'singer': dictionary['singer']
        }
        self.assertEqual(transformer.Transformer()._get_cherry_picked_dict(dictionary, ['singer']), res)

    def test_nested_transformer_example_given(self):
        input_list = [
            {'country': 'US', 'city': 'Boston', 'currency': 'USD', 'amount': 100},
            {'country': 'FR', 'city': 'Paris', 'currency': 'EUR', 'amount': 20},
            {'country': 'FR', 'city': 'Lyon', 'currency': 'EUR', 'amount': 11.4},
            {'country': 'ES', 'city': 'Madrid', 'currency': 'EUR', 'amount': 8.9},
            {'country': 'UK', 'city': 'London', 'currency': 'GBP', 'amount': 12.2},
            {'country': 'UK', 'city': 'London', 'currency': 'FBP', 'amount': 10.9}
        ]
        nest_keys = ['currency', 'country', 'city']
        res = {
            'USD': {'US': {'Boston': [{'amount': 100}]}},
            'EUR': {'FR': {'Paris': [{'amount': 20}], 'Lyon': [{'amount': 11.4}]}, 'ES': {'Madrid': [{'amount': 8.9}]}},
            'GBP': {'UK': {'London': [{'amount': 12.2}]}},
            'FBP': {'UK': {'London': [{'amount': 10.9}]}}
        }
        self.assertEqual(transformer.Transformer().nested_transformer(input_list, nest_keys), res)

    def test_nested_transformer_example_random(self):
        input_list = [
            {'country': 'US', 'city': 'Boston', 'currency': 'USD', 'amount': 100},
            {'country': 'FR', 'city': 'Paris', 'currency': 'EUR', 'amount': 20},
            {'country': 'FR', 'city': 'Lyon', 'currency': 'EUR', 'amount': 11.4},
            {'country': 'ES', 'city': 'Madrid', 'currency': 'EUR', 'amount': 8.9},
            {'country': 'UK', 'city': 'London', 'currency': 'GBP', 'amount': 12.2},
            {'country': 'UK', 'city': 'London', 'currency': 'FBP', 'amount': 10.9}
        ]
        nest_keys = ['city', 'amount']
        res = {
            'Boston': {100: [{'currency': 'USD', 'country': 'US'}]},
            'Paris': {20: [{'currency': 'EUR', 'country': 'FR'}]},
            'Lyon': {11.4: [{'currency': 'EUR', 'country': 'FR'}]},
            'Madrid': {8.9: [{'currency': 'EUR', 'country': 'ES'}]},
            'London': {12.2: [{'currency': 'GBP', 'country': 'UK'}], 10.9: [{'currency': 'FBP', 'country': 'UK'}]}
        }
        self.assertEqual(transformer.Transformer().nested_transformer(input_list, nest_keys), res)


    def test_nested_transformer_example_duplicates(self):
        input_list = [
            {'country': 'UK', 'city': 'London', 'currency': 'EUR', 'amount': 11.4},
            {'country': 'UK', 'city': 'London', 'currency': 'EUR', 'amount': 8.9},
            {'country': 'UK', 'city': 'London', 'currency': 'GBP', 'amount': 12.2},
            {'country': 'UK', 'city': 'London', 'currency': 'FBP', 'amount': 10.9}
        ]
        nest_keys = ['currency', 'country', 'city']
        res = {
            'EUR': {'UK': {'London': [{'amount': 11.4}, {'amount': 8.9}]}},
            'GBP': {'UK': {'London': [{'amount': 12.2}]}},
            'FBP': {'UK': {'London': [{'amount': 10.9}]}}
        }

        self.assertEqual(transformer.Transformer().nested_transformer(input_list, nest_keys), res)



if __name__ == '__main__':
    unittest.main()