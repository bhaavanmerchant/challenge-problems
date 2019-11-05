import logging

class Transformer:

    def nested_transformer(self, input_list, nest_keys):
        logging.debug(input_list)
        logging.debug(nest_keys)
        output = {}
        for input_entry in input_list:
            parent = output
            stripped_leaf = self._get_cherry_picked_dict(input_entry, input_entry.keys() - nest_keys)
            for nest_key in nest_keys:
                nest_value = input_entry[nest_key]
                if self._is_terminal_element(nest_keys, nest_key) and nest_value not in parent:
                    parent[nest_value] = [stripped_leaf]
                elif self._is_terminal_element(nest_keys, nest_key):
                    parent[nest_value].append(stripped_leaf)
                elif nest_value not in parent:
                    parent[nest_value] = {}
                parent = parent[nest_value]
        logging.debug(output)
        return output

    def _get_cherry_picked_dict(self, input_dict, key_list):
        return {key:input_dict[key] for key in key_list}

    def _is_terminal_element(self, elements, element):
        if len(elements) == 0:
            raise IndexError('elements cannot be empty')
        return elements[-1] == element
