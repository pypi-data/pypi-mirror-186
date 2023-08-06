import pytest

import utils

def test_logging():
    # just ensure there is no error, I don't know how to write tests for this
    parser = utils.logging.basic_parser()
    args = parser.parse_args([])
    utils.logging.basic_config(**vars(args))