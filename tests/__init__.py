import os.path

DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(DIR)
TESTS = os.path.join(REPO, 'tests')
SAMPLE_WHITELISTS = os.path.join('tests', 'test-data', 'sample-whitelists')
