import inspect


def _test_direct_module(self, mod):
    return eval("mod.var_defined_globally")


# Most of these methods below don't work because of how jupyter runs code.
def _test_access_global_var(self):
    # https://stackoverflow.com/questions/1095543/get-name-of-calling-functions-module-in-python
    mod = inspect.getmodule(inspect.stack()[1][0])

    return eval("mod.var_defined_globally")


def _test_set_global_var(self):
    mod = inspect.getmodule(inspect.stack()[1][0])

    exec("mod.var_defined_globally = 'bar'")

    pass
