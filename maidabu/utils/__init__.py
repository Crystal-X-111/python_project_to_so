import numpy as np
import struct

__all__ = [
    'raise_error'
]

def print_key_msg():
    print(__file__)

def raise_error(msg):
    print_key_msg()
    raise Exception(msg) from None



