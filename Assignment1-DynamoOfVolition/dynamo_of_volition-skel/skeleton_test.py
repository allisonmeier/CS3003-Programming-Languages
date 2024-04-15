import unittest
import skeleton_test
import dynamic_scope

if __name__ == "__main__":

    # EVERYTHING COMMENTED OUT: helpful guidance for how everything flows and interacts. \
        # Doesn't need to be uncommented or used.

    # d = dynamic_scope.DynamicScope()

    # d["teststring"] = 3
    # print(d["teststring"])

    # for r in d:
    #     print(r)


    # def alpha():
    #     a = 1
    #     f = dynamic_scope.get_dynamic_re()
    #     for i in f:
    #         print(i)
    #         print(f[i])
    # def beta():
    #     b = 2
    #     alpha()
    # def theta():     
    #     a =9    
    #     beta()
    
    # theta()

    suite = unittest.findTestCases(skeleton_test)
    result = unittest.TestResult()
    suite.run(result, debug=True)
    print(f"{result=}")


# if it's correct, it'll print:
    # result=<unittest.result.TestResult run=0 errors=0 failures=0>