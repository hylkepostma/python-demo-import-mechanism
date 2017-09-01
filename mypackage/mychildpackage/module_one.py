import sys
import os


if getattr(sys, 'frozen', False):
    # running as an executable
    print("running as an executable")
    bundle_dir = sys._MEIPASS

else:
    # running as an .py
    print("running as a .py")
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

print('running' if __name__ == '__main__' else 'imported', "mychildpackage.module_one")
print('')
print('bundle dir is', bundle_dir)
print('sys.argv[0] is', sys.argv[0])
print('sys.executable is', sys.executable)
print('os.getcwd is', os.getcwd())
print('')


class Test:

    def __init__(self):
        print("init test class")

    def test(self):
        print("method printing test")


if __name__ == '__main__':

    test_object = Test()
    test_object.test()
