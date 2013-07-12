#!/usr/bin/python2.4

import pytest
from support_files.diff_match_patch import diff_match_patch

ref =  open("ref.geo", 'r')
test = open("tester.geo", 'r')


def test_geo():
  diffcheck = diff_match_patch()
  diffs = diffcheck.diff_main(ref.read(), test.read())
  not_zeroes = [i for i, v in enumerate(diffs) if v[0] != 0]
  assert (not not_zeroes)

def updateParam(referring, tester):
	ref.close()
	test.close()
	global ref 
	ref = open(referring, 'r')
	global test 
	test = open(tester, 'r') 
	test_geo()


  

def func(x):
  return x+1
  
def test_func():
	assert func(3) ==5
  	


