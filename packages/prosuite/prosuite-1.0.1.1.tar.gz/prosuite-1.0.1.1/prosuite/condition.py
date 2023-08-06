__all__ = ['Condition']
from prosuite.issue_filter import IssueFilter
from prosuite.parameter import Parameter
from typing import List


class Condition:
    """
    Defines a test condition. Conditions are created with the class :py:mod:`prosuite.generated.quality_conditions` 
    """

    def __init__(self, test_descriptor: str, name: str = ""):

        #:
        self.name = name

        #:
        self.test_descriptor = test_descriptor

        #:
        self.allow_errors: bool = False

        #:
        self.category: str = "Geometry"

        #:
        self.stop_on_error: bool = False

        #:
        self.description: str = ""

        #:
        self.url: str = ""

        #:
        self.parameters: List[Parameter] = []

        #:
        self.issue_filters: List[IssueFilter] = []

        #:
        self.issue_filter_expression: str

    def generate_name(self):
        """
        generates a technical name using the dataset name(s) and the test descriptor 
        """
        first_dataset_parameter = next(
            (p for p in self.parameters if p.is_dataset_parameter), None)
        if first_dataset_parameter:
            ds_param: Parameter = first_dataset_parameter
            if ds_param.contains_list_of_datasets:
                dataset_list: List[str] = [ds.name for ds in ds_param.dataset]
                dataset_names = "_".join(dataset_list)
                self.name = f"{self.test_descriptor} {dataset_names}"
            else:
                self.name = f"{self.test_descriptor} {ds_param.dataset.name}"
