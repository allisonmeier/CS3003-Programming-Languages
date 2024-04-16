from stimpl.expression import BooleanLiteral
from stimpl.robustness import run_stimpl_robustness_tests
from stimpl.test import run_stimpl_sanity_tests
from stimpl.test_state import test_state_implementation

if __name__=='__main__':
  # working
  test_state_implementation()
  # working
  run_stimpl_sanity_tests()
  # not
  run_stimpl_robustness_tests()



# When everything works, I should see in terminal:
  # All tests ran successfully!