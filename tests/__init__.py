import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

## CONSTANTS
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, ".."))
FILE_ROOT_DIR = os.path.join(PROJECT_DIR, "output")
