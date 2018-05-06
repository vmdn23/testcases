#!/usr/bin/python3
"""Testing Utility

    This modules can be imported to aide in testing functions.
"""
def no_imports(module, accepted):
    """Checks to ensure module namespace only contains accepted objects

        Args:
            module (module): the module to check
            accepted (list): list containing accepted objects

        Returns:
            returns True if module complies, False otherwise
    """

    correct = ['__builtins__', '__cached__', '__doc__',
                '__file__', '__loader__', '__name__', 
                '__package__', '__spec__'] + list(accepted)
    for obj in dir(module):
        if obj not in correct:
	        return False
    return True
