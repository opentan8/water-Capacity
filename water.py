#!/usr/bin/env python3

import time, sys
from itertools import permutations as perm

def args_compose(args=sys.argv[1:]):
  args = tuple(map(eval, args))
  limit = [abs(item) for item in args if item < 0]
  args = tuple(map(abs, args))
  leng = args[0]+1
  bottles = args[1:leng]
  targets = [(args[i], bottles.index(args[i+1])) for i in range(leng,len(args),2)]
  limit = [bottles.index(item) for item in limit]
  if not (limit and targets): raise ValueError('Arguments not correct.')
  return bottles, targets, limit

def puring(pure):
  for src, dest in perm(ITER, 2):
    if src in LIMIT: continue
    num = min(pure[src], BOTTLES[dest] - pure[dest])
    if num == 0: continue
    pure_copy = pure[:]
    pure_copy[src] -= num
    pure_copy[dest] += num
    if pure_copy in CURR:
      ind = DUMP.index(pure_copy)
    elif pure_copy not in DUMP:
      ind = len(DUMP)
      DUMP.append(pure_copy)
    else:
      continue
    yield [src, dest, ind]

def repeat(pures):
  CURR = []
  for pure in pures:
    pure_copy = DUMP[pure[-1]]
    for item in puring(pure_copy):
      yield pure + item
      
def resolve(default, targets):
  pures = [default]
  result = []
  while pures:
    result = []
    for pure in repeat(pures):
      for target in targets:
        if DUMP[pure[-1]][target[1]] != target[0]:
          result.append(pure)
          break
      else:
        yield pure
    pures = result[:]

def output(result):
  extra = result[3:]
  cnt = 0
  while extra:
    src, dest, ind, *extra = extra
    cnt += 1
    print('%3d: %3s --> %3s:  %s' % (cnt, BOTTLES_OUT[src], BOTTLES_OUT[dest], DUMP[ind][:-1]))

def counter(start=0):
  cnt = [start]
  def count():
    cnt[0] += 1
    return cnt[0]
  return count

def main():
  cnt = 0
  start = START 
  for result in resolve(DEFAULT, TARGETS):
    cnt += 1
    print('Solution %d:' % cnt)
    output(result)
    print('Time Used: %d μs' % ((10**6)*(time.time() - start)))
    input()
    start = time.time()

if __name__ == '__main__':
  START = time.time()
  NAN = 10000
  DEFAULT = [None, None, -1]
  try: BOTTLES, TARGETS, LIMIT = args_compose(sys.argv[1:])
  except Exception as e: print(e); exit()
  CURR = []
  DUMP = [[0 for i in BOTTLES] + [NAN]]
  BOTTLES_OUT = BOTTLES + ('N/A',)
  BOTTLES += (NAN,)
  ITER = range(len(BOTTLES))
  try: main()
  except KeyboardInterrupt: print('Exit Successful.')
