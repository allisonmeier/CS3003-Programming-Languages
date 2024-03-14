import unittest
import skeleton_test

if __name__ == "__main__":
    suite = unittest.findTestCases(skeleton_test)
    result = unittest.TestResult()
    suite.run(result, debug=True)
    print(f"{result=}")


# if it's correct, it'll print:
    # result=<unittest.result.TestResult run=0 errors=0 failures=0>