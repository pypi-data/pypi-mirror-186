import logging

import utils

def basic_config(level='INFO', format='%(levelname)s: %(name)s: %(message)s'):
    logging.basicConfig(level=getattr(logging, level), format='%(levelname)s: %(name)s: %(message)s')
    
def basic_parser(**kwargs):
    parser = utils.argparse.default_parser(basic_config, configs={
        'level': dict(opt_str=['--ll', '--log-level'], choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
        'format': dict(opt_str=['--lf', '--log-format']),
    }, **kwargs)
    return parser