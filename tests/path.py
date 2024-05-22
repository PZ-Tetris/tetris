import importlib.util
import sys

spec = importlib.util.spec_from_file_location("App", "D:\AGH\testris\tetris\app.py")
foo = importlib.util.module_from_spec(spec)
sys.modules["App"] = foo
spec.loader.exec_module(foo)
foo.MyClass()