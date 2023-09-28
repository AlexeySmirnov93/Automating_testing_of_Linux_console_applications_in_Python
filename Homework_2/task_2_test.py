from task_1_check import checkout
import pytest

folderin = "/home/test/user/test" 
folderout = "/home/test/user/out"
folderext = "/home/test/user/folder"

def test_step1():
    assert checkout(f"cd {folderin};7z a {folderout}/arch1", "Everything is Ok"), "test_step1 FAIL"

def test_step2():
    assert checkout(f"7z d {folderout}/arch1.7z" , "Everything is Ok"), "test_step2 FAIL" 

def test_step3():
    assert checkout(f"cd {folderext}; 7z u {folderout}/arch1.7z", "Everything is Ok") , "test_step3 FAIL" 
    
def test_step4():
    assert checkout(f"7z l {folderout}/arch1.7z", "2 files") , "test_step3 FAIL" 
    
def test_step5():
    assert checkout(f"cd {folderext}; 7z x {folderout}/arch1.7z -y", "Everything is Ok") , "test_step3 FAIL" 

def test_step6():
    assert checkout(f"crc32 {folderout}/arch1.7z", "a304c2a6") , "test_step3 FAIL" 

if __name__ == "__main__":
    pytest.main(["-vv"])