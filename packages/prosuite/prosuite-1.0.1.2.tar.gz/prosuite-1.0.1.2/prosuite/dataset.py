from prosuite.model import Model


class BaseDataset():
    def __init__(self, name: str, filter_expression: str = ""):
        self.name: str = name
        self.filter_expression: str = filter_expression
        pass


class Dataset(BaseDataset):
    """
    A dataset represents a table in an esri workspace. Usually the table is a featureclass.
    """

    def __init__(self, name: str, model: Model, filter_expression: str = ""):
        """
        :param name: table (featureclass) name
        :param model: prosuite.model
        :param filter_expression: a where clause that filters the table. syntax of the whereclause is defined in
        <prosuite installation folder>/doc/tests/SQLSyntax_en.pdf
        """
        super().__init__(name, filter_expression)
        self.model: Model = model
