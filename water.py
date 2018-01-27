#!/usr/bin/env python3

import time, sys
from itertools import permutations as perm
from collections import defaultdict


class WaterCapacity:
  def __init__(self):
    self.water_capacity = (0, 8), (0, 34), (0, 3)
    self.expects = [(0, 8), (1, 14)]
    self.limits = []

    self.bottles, self.capacity = zip(*self.water_capacity)
    if not self.check():
      raise ValueError("Arguments Error")
    self.solution_count = 0
    
    self.cache_history = {self.bottles}
    self.cache_current = defaultdict(set)
    self.run_bottles = defaultdict(set)
    self.run_bottles[self.bottles].add(tuple())
    
    self.actions = self.get_actions()
    self.start_time = time.time()

  def check(self):
    return all((
      # check water_capacity
      all(0 <= a <= b and a == int(a) and b == int(b)
          for a, b in self.water_capacity),
      # check expects
      all(i in range(len(self.water_capacity)) and v == int(v)
          and 0 <= v <= self.capacity[i] for i, v in self.expects),
      # check limits
      all(i in range(len(self.water_capacity)) for i in self.limits),
    ))

  def get_actions(self):
    actions = perm(tuple(range(len(self.water_capacity))) + (None, ), 2)
    return tuple(action for action in actions if action[0] not in self.limits)    

  def is_finished(self, bottles):
    return all(bottles[i] == v for i, v in self.expects)

  def pour(self, a, b, bottles):
    _bottles = list(bottles)
    if a is None:
      _bottles[b] = self.capacity[b]
    elif b is None:
      _bottles[a] = 0
    else:
      n = min(_bottles[a], self.capacity[b] - _bottles[b])
      if n > 0:
        _bottles[a] -= n
        _bottles[b] += n
    return tuple(_bottles)

  def run(self):
    while True:
      if not self.run_bottles:
        self.cache_history |= set(self.cache_current)
        self.run_bottles = self.cache_current.copy()
        self.cache_current.clear()
      if not self.run_bottles:
        break
      bottles, steps = self.run_bottles.popitem()
      for i, action in enumerate(self.actions):
        _bottles = self.pour(*action, bottles)
        if _bottles not in self.cache_history:
          for step in steps:
            self.cache_current[_bottles].add(step + (i, ))
          if self.is_finished(_bottles):
            self.end_time = time.time()
            self.display(_bottles)
            self.start_time = time.time()

  def display(self, bottles):
    for steps in self.cache_current[bottles]:
      self.solution_count += 1
      bottles = tuple(self.bottles)
      print('Solution %d:' % (self.solution_count))
      for i, step in enumerate(steps, 1):
        a, b = self.actions[step]
        if a is None:
          result = 'Fill  Bottle %2d' % (b + 1)
        elif b is None:
          result = 'Clear Bottle %2d' % (a + 1)
        else:
          result = 'Pour  %2d  To %2d' % (a + 1, b + 1)
        bottles = self.pour(a, b, bottles)
        print('%2d: %s, Result is %s' % (i, result, bottles))
      print('Time Used %s' % self.timeformat(self.end_time - self.start_time))
      input()

  def timeformat(self, seconds):
    if seconds <= 10 ** -6:
      return '%.4f ns' % (seconds * 10 ** 9)
    elif seconds <= 10 ** -3:
      return '%.4f μs' % (seconds * 10 ** 6)
    elif seconds <= 1:
      return '%.4f ms' % (seconds * 10 ** 3)
    else:
      return '%.4f s' % seconds


wc = WaterCapacity()
wc.run()
