import sys

# This is built specifically to handle loading test variables for papermill.
# EXTREMELY brittle.
def load_test_parameters(self, params_dict):
    mod = _get_notebook_module()

    for var_name, var_val in params_dict.items():
        try:
            # If this is defined by papermill or anyone else, we don't want to set it.
            eval(f"mod.{var_name}")
        except (NameError, AttributeError):
            # Papermill nor anyone else defined this variable, let's set it ourselves!
            setattr(mod, var_name, var_val)


def get_parameter(self, var_name, default=None):
    mod = _get_notebook_module()

    if default:
        try:
            return eval(f"mod.{var_name}")
        except (NameError, AttributeError):
            return default
    else:
        return eval(f"mod.{var_name}")


def _get_notebook_module():
    mod = sys.modules["__main__"]

    if mod:
        return mod
    else:
        raise ModuleNotFoundError("__main__ not found, is this called from a Notebook?")

def _run_data(self):
    logical_step_name = self.get_parameter("logical_step_name")
    state_machine_run_id = self.get_parameter("state_machine_run_id")

    return logical_step_name, state_machine_run_id