import pytest
import argparse

import utils

def func_0(a, b: int, hi_bye: str = 'hibye', hell_o: float = 0.3, debug=False):
    return a, b, hi_bye, hell_o
    
def func_1(d, e: float, f: str = 'bye'):
    return d, e, f
   
@pytest.fixture
def parser_0():
    parser = utils.argparse.default_parser(func_0, configs={
            'a': dict(opt_str=['-a'], type=int),
            'b': dict(opt_str=['-b']),
            'hi_bye': dict(opt_str=['--hi', '--hi-bye']),
            'hell_o': dict(opt_str=['--hell', '--hell-o'], nargs='+'),
            'debug': dict(action='store_true'),
        },
        add_help=False
    )
    return parser

@pytest.fixture
def parser_1():
    parser = utils.argparse.default_parser(func_1, configs={
            'e': dict(choices=[0.5,0.7,0.9]),
        },
        add_help=False,
    )
    return parser

@pytest.mark.parametrize('args, expected_0, expected_1', [
    ('-a 1 -b 2 --hi hi --hell 0.3 0.4 -f hihi blah 0.5'.split(),
     {'a': 1, 'b': 2, 'hi_bye': 'hi', 'hell_o': [0.3,0.4], 'debug': False},
     {'d': 'blah', 'e': 0.5, 'f': 'hihi'}),
    ('blah 0.5 -a 1 -b 2 --hi hi --hell 0.3 0.4 -f hihi'.split(),
     {'a': 1, 'b': 2, 'hi_bye': 'hi', 'hell_o': [0.3,0.4], 'debug': False},
     {'d': 'blah', 'e': 0.5, 'f': 'hihi'}),
    ('-a 1 -b 2 --hi hi --hell 0.3 0.4 -f hihi blah 0.5 --debug'.split(),
     {'a': 1, 'b': 2, 'hi_bye': 'hi', 'hell_o': [0.3,0.4], 'debug': True},
     {'d': 'blah', 'e': 0.5, 'f': 'hihi'}),
    ('-a 1 -b 2 -f hihi blah 0.5 --debug'.split(),
     {'a': 1, 'b': 2, 'hi_bye': 'hibye', 'hell_o': 0.3, 'debug': True},
     {'d': 'blah', 'e': 0.5, 'f': 'hihi'}),
])
def test_multi_parse(parser_0, parser_1, args, expected_0, expected_1):
    args_0, args_1 = utils.argparse.multi_parse([parser_0, parser_1], args=args)
    assert vars(args_0) == expected_0
    assert vars(args_1) == expected_1
    
    
@pytest.mark.parametrize('args, expected_0, expected_1', [
    ('-a 1 -b 2 --hi hi --hell 0.3 0.4 -f hihi blah 0.6'.split(),
     {'a': 1, 'b': 2, 'hi_bye': 'hi', 'hell_o': [0.3,0.4], 'debug': False},
     {'d': 'blah', 'e': 0.6, 'f': 'hihi'}),
])
def test_multi_parse_bad_choice(parser_0, parser_1, args, expected_0, expected_1):
    with pytest.raises(SystemExit):
        args_0, args_1 = utils.argparse.multi_parse([parser_0, parser_1], args=args)
        
def test_multi_parse_help(parser_0, parser_1):
    with pytest.raises(SystemExit):
        utils.argparse.multi_parse([parser_0, parser_1], args=['-h'])