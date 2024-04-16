from typing import Any, Tuple, Optional

from stimpl.expression import *
from stimpl.types import *
from stimpl.errors import *

"""
Interpreter State
"""


class State(object):
    def __init__(self, variable_name: str, variable_value: Expr, variable_type: Type, next_state: 'State') -> None:
        self.variable_name = variable_name
        self.value = (variable_value, variable_type)
        self.next_state = next_state

    def copy(self) -> 'State':
        variable_value, variable_type = self.value
        return State(self.variable_name, variable_value, variable_type, self.next_state)

    def set_value(self, variable_name, variable_value, variable_type):
        return State(variable_name, variable_value, variable_type, self)

    def get_value(self, variable_name) -> Any:
        if self.variable_name == variable_name:
            return self.value
        else:
            return self.next_state.get_value(variable_name)

    def __repr__(self) -> str:
        return f"{self.variable_name}: {self.value}, " + repr(self.next_state)


class EmptyState(State):
    def __init__(self):
        pass

    def copy(self) -> 'EmptyState':
        return EmptyState()

    def get_value(self, variable_name) -> None:
        return None

    def __repr__(self) -> str:
        return ""


"""
Main evaluation logic!
"""


def evaluate(expression: Expr, state: State) -> Tuple[Optional[Any], Type, State]:
    match expression:
        case Ren():
            return (None, Unit(), state)

        case IntLiteral(literal=l):
            return (l, Integer(), state)

        case FloatingPointLiteral(literal=l):
            return (l, FloatingPoint(), state)

        case StringLiteral(literal=l):
            return (l, String(), state)

        case BooleanLiteral(literal=l):
            return (l, Boolean(), state)

        case Print(to_print=to_print):
            printable_value, printable_type, new_state = evaluate(to_print, state)

            match printable_type:
                case Unit():
                    print("Unit")
                case _:
                    print(f"{printable_value}")

            return (printable_value, printable_type, new_state)

        case Sequence(exprs=exprs) | Program(exprs=exprs):
            """ Match a Sequence or Program value with the same exprs (expression) value"""
            
            # dummy default empty values
            value_result = None
            value_type = Unit()
            new_state = state
            
            for expr in exprs:
                # evaluate each expr, but use updated new_state each time
                value_result, value_type, new_state = evaluate(expr, new_state)

            return (value_result, value_type, new_state)

        case Variable(variable_name=variable_name):
            value = state.get_value(variable_name)
            if value == None:
                raise InterpSyntaxError(f"Cannot read from {variable_name} before assignment.")
            variable_value, variable_type = value
            return (variable_value, variable_type, state)

        case Assign(variable=variable, value=value):

            value_result, value_type, new_state = evaluate(value, state)

            variable_from_state = new_state.get_value(variable.variable_name)
            _, variable_type = variable_from_state if variable_from_state else (
                None, None)

            if value_type != variable_type and variable_type != None:
                raise InterpTypeError(f"""Mismatched types for Assignment:
            Cannot assign {value_type} to {variable_type}""")

            new_state = new_state.set_value(
                variable.variable_name, value_result, value_type)
            return (value_result, value_type, new_state)

        case Add(left=left, right=right):
            result = 0
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types for Add:
            Cannot add {left_type} to {right_type}""")

            match left_type:
                case Integer() | String() | FloatingPoint():
                    result = left_value + right_value
                case _:
                    raise InterpTypeError(f"""Cannot add {left_type}s""")

            return (result, left_type, new_state)

        case Subtract(left=left, right=right):
            result = 0
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)
            
            # Do the two types match?
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            # Awesome, they do
            match left_type:
                # are they subtract-able types?
                case Integer() | FloatingPoint(): 
                    # if so, subtract
                    result = left_value - right_value
                case _:
                    # if not, error, see ya
                    raise InterpTypeError(f"""Un-subtract-able type ({left_type}).""")

            return (result, left_type, new_state)

        case Multiply(left=left, right=right):
            """edited by me"""
            result = 0
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)
            
            # Do the two types match?
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            # Awesome, they do
            match left_type:
                # are they multiply-able types?
                case Integer() | FloatingPoint(): 
                    # if so, multiply
                    result = left_value * right_value
                case _:
                    # if not, error, see ya
                    raise InterpTypeError(f"""Un-multiply-able type ({left_type}).""")

            return (result, left_type, new_state)

        case Divide(left=left, right=right):
            """edited by me"""
            result = 0
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)
            
            # Do the two types match?
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")
            
            # Is it mathematically valid?
            if right_value == 0:
                raise InterpMathError(f"""You can't divide by zero, fyi.""")

            match left_type:
                case FloatingPoint():
                    result = left_value / right_value
                # need seperate case for integer division since it may need to be casted to an int after division
                case Integer():
                    result = int(left_value / right_value)
                case _:
                    raise InterpTypeError(f"""Cannot divide {left_type}s""")

            return (result, left_type, new_state)

        case And(left=left, right=right):
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types for And:
            Cannot evaluate {left_type} and {right_type}""")
            match left_type:
                case Boolean():
                    result = left_value and right_value
                case _:
                    raise InterpTypeError("Cannot perform logical and on non-boolean operands.")

            return (result, left_type, new_state)

        case Or(left=left, right=right): 
            """edited by me"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            # do the types match?
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")
            
            match left_type:
                # are they booleans? aka comparable
                case Boolean():
                    # if so, compare (or)
                    result = left_value or right_value
                case _: # if it's anything else
                    # if not, error
                    raise InterpTypeError(f"Invalid type ({left_type}). Must be a boolean.")

            return (result, left_type, new_state)         

        case Not(expr=expr):
            """edited by me"""
            expr_value, expr_type, new_state = evaluate(expr, state)

            match expr_type:
                # expression = boolean type?
                case Boolean(): 
                    # if so, return the opposite boolean
                    result = not expr_value
                case _: 
                    # if not, error for wrong type
                    raise InterpTypeError(f"Invalid type. Must be a boolean.")

            return (result, expr_type, new_state)

        case If(condition=condition, true=true, false=false):
            """ edited by me """
            # might still be weird 
            condition_value, condition_type, new_state = evaluate(condition, state)

            match condition_type:
               # expression = boolean type?
                case Boolean(): 
                    # if so, check if value true or not and return
                    if condition_value:
                        result, condition_type, new_state = evaluate(true, new_state)
                    else:
                        result, condition_type, new_state = evaluate(false, new_state)
                case _:
                    # if not, error for wrong type
                    raise InterpTypeError(f"Condition type must be boolean. Actual type: {condition_type}")

            return (result, condition_type, new_state)

        case Lt(left=left, right=right):
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            result = None

            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types for Lt:
            Cannot compare {left_type} and {right_type}""")

            match left_type:
                case Integer() | Boolean() | String() | FloatingPoint():
                    result = left_value < right_value
                case Unit():
                    result = False
                case _:
                    raise InterpTypeError(
                        f"Cannot perform < on {left_type} type.")

            return (result, Boolean(), new_state)

        case Lte(left=left, right=right):
            """(less than or equal to)"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            # do the two types match?
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            match left_type:
                # are the types numeric?
                case Integer() | FloatingPoint() | Boolean() | String():
                    # if so, go ahead and compare
                    result = left_value <= right_value
                case Unit(): # weird case. If they're both units, then they should be equal, so technically count under LTE. But barely, and weirdly.
                    result = True
                case _:
                    # if not, error
                    raise InterpTypeError(f"""Cannot compare {left_type}s""")

            return (result, Boolean(), new_state)

        case Gt(left=left, right=right):
            """(greater than)"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            # Check if both left and right values are of comparable types
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            match left_type:
                case Integer() | FloatingPoint() | Boolean() | String():
                    result = left_value > right_value
                case Unit():
                    result = False # can't be just greater/less than. Just equal to. 
                case _:
                    raise InterpTypeError(f"""Cannot compare {left_type}s""")

            return (result, Boolean(), new_state)

        case Gte(left=left, right=right):
            """(greater than or equal to)"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            # Check if both left and right values are of comparable types
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            match left_type:
                case Integer() | FloatingPoint() | Boolean() | String():
                    result = left_value >= right_value
                case Unit():
                    result = True
                case _:
                    raise InterpTypeError(f"""Cannot compare {left_type}s""")
                
            return (result, Boolean(), new_state)

        case Eq(left=left, right=right):
            """edited by me. (equal to)"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            result = None

            # Check if both left and right values are of comparable types
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")
            
            match left_type:
                case Integer() | FloatingPoint() | Boolean() | String():
                    result = (left_value == right_value)
                case Unit():
                    result = True
                case _:
                    InterpTypeError(f"""Cannot compare {left_type}s""")

            return (result, Boolean(), new_state) 

        case Ne(left=left, right=right):
            """(not equal to)"""
            left_value, left_type, new_state = evaluate(left, state)
            right_value, right_type, new_state = evaluate(right, new_state)

            # Check if both left and right values are of comparable types
            if left_type != right_type:
                raise InterpTypeError(f"""Mismatched types ({left_type} and {right_type}).""")

            match left_type:
                case Integer() | FloatingPoint() | Boolean() | String():
                    result = left_value != right_value
                case Unit():
                    result = False
                case _:
                    raise InterpTypeError(f"""Cannot compare {left_type}s""")
            
            return (result, Boolean(), new_state)

        case While(condition=condition, body=body):
            """edited by me. slightly confusing one"""
            condition_value, condition_type, new_state = evaluate(condition, state)

            while condition_value: # only do the stuff if it's true
                match condition_type:
                    case Boolean():
                        # do the body of code, evaluate code, get new condition val if applicable, move on if applicable
                        body_value, body_type, new_state = evaluate(body, new_state)
                        condition_value, condition_type, new_state = evaluate(condition, new_state)                        

                    case _:
                        raise InterpTypeError(f"While loop condition must be boolean, instead got {condition_type}")

            return (False, Boolean(), new_state)

        case _:
            raise InterpSyntaxError("Unhandled!")
    pass


def run_stimpl(program, debug=False):
    state = EmptyState()
    program_value, program_type, program_state = evaluate(program, state)

    if debug:
        print(f"program: {program}")
        print(f"final_value: ({program_value}, {program_type})")
        print(f"final_state: {program_state}")

    return program_value, program_type, program_state
