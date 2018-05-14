import argparse

import psutil


parser = argparse.ArgumentParser(description='Script prints basic information about your OS to console.')
parser.add_argument('kind', metavar='kind', choices=['cpu', 'mem'], help='Accept two params <cpu> or <mem>')

args = parser.parse_args()


if args.kind == 'cpu':
    cpu = psutil.cpu_times()

    print('idle   ', cpu.idle)
    print('user   ', cpu.user)
    print('guest  ', cpu.guest)
    print('iowait ', cpu.iowait)
    print('stolen ', cpu.steal)
    print('system ', cpu.system)
else:
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print('mem.total  ', mem.total)
    print('mem.used   ', mem.used)
    print('mem.free   ', mem.free)
    print('mem.shared ', mem.shared)
    print('swap.total ', swap.total)
    print('swap.used  ', swap.used)
    print('swap.free  ', swap.free)
