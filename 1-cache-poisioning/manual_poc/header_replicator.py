import os
import importlib

# Define the input file
source_file = 'some_library/some_file.py'

# 1st DWORD: Magic Number
# Version reference: https://github.com/python/cpython/blob/3.11/Lib/importlib/_bootstrap_external.py#L420
# Keep in mind that this will grab the runtime interpreter, can also ask explicitly with an integer
MAGIC_NUMBER = importlib.util.MAGIC_NUMBER

# 2nd DWORD: Bit Field "determinism"
# Structure reference: https://github.com/python/cpython/blob/3.11/Lib/py_compile.py#L66
# This defaults to Timestamp if not set as SIPHASH: https://github.com/python/cpython/blob/3.11/Lib/py_compile.py#L160
BIT_FIELD = (0).to_bytes(4, 'little')

# 4rd DWORD: Timestamp or SIP-Hash
# Timestamp code comes from here: https://github.com/python/cpython/blob/f4c03484da59049eb62a9bf7777b963e2267d187/Lib/importlib/_bootstrap_external.py#L632
BYTECODE_TIMESTAMP = ((int(os.stat(source_file).st_mtime)) & 0xFFFFFFFF).to_bytes(4, 'little')

# File Size (forth DWORD)
# nathaniel@singer.cloud TODO: FIND SOURCE
FILE_SIZE = os.stat(source_file).st_size.to_bytes(4, 'little')

# Show Real Header
with open(r"some_library/__pycache__/some_file.cpython-310.pyc", "rb") as f: metadata = f.read(16)
print(f'actual    {metadata.hex()}')

# Show generated header
print(f'generated {MAGIC_NUMBER.hex()}{BIT_FIELD.hex()}{BYTECODE_TIMESTAMP.hex()}{FILE_SIZE.hex()}')
