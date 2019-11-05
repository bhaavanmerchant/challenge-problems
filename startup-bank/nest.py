import argparse
import json
import logging
import sys

import transformer

stdin_input = sys.stdin.read()
logging.info(stdin_input)
input_dict = json.loads(stdin_input)

parser = argparse.ArgumentParser(description='Process a json and parse it.')
parser.add_argument('keys', type=str, nargs='+',
                    help='a list of nesting keys', action='append')

nesting_keys = parser.parse_args().keys[0]
logging.info(nesting_keys)

tr = transformer.Transformer()
print(json.dumps(tr.nested_transformer(input_dict, nesting_keys), indent=4, sort_keys=True))