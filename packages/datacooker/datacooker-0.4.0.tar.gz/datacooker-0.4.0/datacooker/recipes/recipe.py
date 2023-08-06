"""Recipe module"""

from typing import Callable, Dict
from numpy import ndarray
from numpy.random import choice
from pandas import DataFrame, get_dummies
from datacooker.variables.nominal_variable import NominalVariable

from datacooker.variables.variable import Variable


class Recipe:
    """
    A Recipe is a class holding steps to build data
    based on selected model and variables descriptions
    """

    def __init__(self, model_function: Callable, result_label: str = 'result') -> None:
        self._model: Callable = model_function
        self._result_label: str = result_label
        self._variables: Dict[str, Variable] = {}
        self._corr_variables: list[tuple[str, Callable]] = []
        self._error: Callable = None
        self._data: Dict[str, ndarray] = {}

    def add_variable(self, variable: Variable) -> None:
        """Adds an independent variable to the recipe

        Args:
            variable (Variable): variable
        """
        self._variables.update({variable.label: variable})

    def add_variables(self, variables: list[Variable]) -> None:
        """Adds a list of independent variables to the recipe

        Args:
            variables (list[Variable]): list of variables
        """
        for variable in variables:
            self.add_variable(variable)

    def add_corr_variable(self, label: str, lambda_fn: Callable) -> None:
        """Adds a correlated variable to the recipe.
        The correlation function defines how its values depend on indepedent variables
        added to the model.

        Args:
            label (str): variable name
            lambda_fn (Callable): function that defines correlated variable values taking
            dictionary of variables as argument
            other variables in the recipe.
        """
        self._corr_variables.append((label, lambda_fn))

    def add_corr_variables(self, labels: list[str], variable_fn: list[Callable]) -> None:
        """Adds a list of correlated variables to the recipe.
        The correlation function defines how its values depend on indepedent variables
        added to the model.

        Args:
            labels (list[str]): list of names for each added correlated variable
            lambda_fns (list[Callable]): list of function that defines correlated variable values
            taking dictionary of variables as argument
            other variables in the recipe.
        """
        if len(labels) != len(variable_fn):
            error_msg = invalid_labels_and_functions_length_msg(
                len(labels), len(variable_fn))
            raise ValueError(error_msg)

        for index, label in enumerate(labels):
            self.add_corr_variable(label, variable_fn[index])

    def add_error(self, lambda_fn: Callable) -> None:
        """Adds an error component that directly influences the resulting variable

        Args:
            label (str): noise variable name
            lambda_fn (Callable): _description_
        """
        self._error = lambda_fn

    def cook(self, size: int = 100) -> DataFrame:
        """Cooks the recipe!
        Generates values for independent, correlated, noise and result variables.
        Stores data in a dataframe

        Args:
            size (int, optional): How many entries should be generated. Defaults to 100.

        Returns:
            pd.DataFrame: dataframe containing all variables
        """
        self._generate_variables(size)
        self._generate_result_values(size)
        self._apply_missing_data_fraction(size)
        return DataFrame.from_dict(self._data)

    def _generate_variables(self, size):
        self.__generate_indepedent_var_values(size)
        self.__generate_corr_var_values()

    def _apply_missing_data_fraction(self, size: int) -> None:
        for label, variable in self._variables.items():
            fraction = variable.missing_values_fraction
            if fraction:
                choices_count = int(fraction * size)
                chosen_indexes = choice(size, choices_count, replace=False)
                if isinstance(variable, NominalVariable):
                    self.__update_nominal_missing_data(label, chosen_indexes)
                else:
                    values = self._data[label]
                    values[chosen_indexes] = None
                    self._data.update({label: values})

    def __update_nominal_missing_data(self, label: str, chosen_indexes: ndarray) -> None:
        for category, values in self._data.items():
            if category.startswith(f"{label}."):
                values = values.astype(float)
                values[chosen_indexes] = None
                self._data.update({category: values})

    def _generate_error_values(self, size: int) -> int | ndarray:
        if not self._error:
            return 0

        return self._error(self._data, size)

    def _generate_result_values(self, size: int) -> None:
        error_values = self._generate_error_values(size)
        results = self._apply_model(error_values)
        self._data.update({self._result_label: results})

    def __generate_corr_var_values(self) -> None:
        if bool(self._corr_variables):
            for (label, corr_fn) in self._corr_variables:
                self._data.update({label: corr_fn(self._data)})

    def __generate_indepedent_var_values(self, size: int) -> None:
        if not self._variables:
            raise ValueError(NO_VARIABLES_ERROR_MSG)

        for label, variable in self._variables.items():
            if isinstance(variable, NominalVariable):
                dummies_dataframe = get_dummies(variable.simulate_values(size))
                for column in dummies_dataframe:
                    self._data.update(
                        {f"{label}.{column}": dummies_dataframe[column].values})
            else:
                self._data.update({label: variable.simulate_values(size)})

    def _apply_model(self, error_values):
        return self._model(self._data, error_values)


def invalid_labels_and_functions_length_msg(length_labels: int, length_functions: int) -> str:
    """Builds error message for labels and functions lenghts mismatch

    Args:
        length_labels (int): length of labels list
        length_functions (int): length of functions list

    Returns:
        str: error message
    """

    return f"""
        Labels and Functions lists must have the same length: Labels legth: {length_labels}, \
            functions length: {length_functions}.
    """


NO_VARIABLES_ERROR_MSG = "No variables have been included in the recipe"
