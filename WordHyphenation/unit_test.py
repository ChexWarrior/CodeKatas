from main import *
import pytest

def test_scrub_pattern():
    
    assert(scrub_pattern("hello") == "hello")