__author__ = "The ProSuite Authors"
__copyright__ = "Copyright 2021-2023, The ProSuite Authors"
__license__ = "MIT"
__version__ = "1.0.1.0"
__maintainer__ = "Dira GeoSystems"
__email__ = "programmers@dirageosystems.ch"
__date__  = "14.01.2023"
__status__ = "Production"


from datetime import datetime
from typing import List
from prosuite.issue_filter import IssueFilter
from prosuite.parameter import Parameter
from prosuite.dataset import BaseDataset
from prosuite.factories.enums import *

class IssueFilters:

    @classmethod
    def if_intersecting_0(cls, feature_class: BaseDataset) -> IssueFilter:
        """
        Filters errors that intersect any feature in a 'featureClass'
        """
        
        result = IssueFilter("IfIntersecting(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.generate_name()
        return result

    @classmethod
    def if_involved_rows_0(cls, constraint: str, tables: List[BaseDataset] = None) -> IssueFilter:
        """
        Filters errors where any involved row fulfills 'constraint'
        """
        
        result = IssueFilter("IfInvolvedRows(0)")
        result.parameters.append(Parameter("constraint", constraint))
        if type(tables) == list:
            for element in tables:
                result.parameters.append(Parameter("Tables", element))
        else:
            result.parameters.append(Parameter("Tables", tables))
        result.generate_name()
        return result

    @classmethod
    def if_within_0(cls, feature_class: BaseDataset) -> IssueFilter:
        """
        Filters errors that are completely within any feature in a 'featureClass'
        """
        
        result = IssueFilter("IfWithin(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.generate_name()
        return result
