#!/usr/bin/python2.4

import pytest

def func(x):
  return x + 1

class Test_Sample:

  def test_square(self):
    x =3
    assert x**2 == 9
    
  def test_simple(self):
    x =4
    assert x==5

  def test_answer(self):
    assert func(3) == 5

