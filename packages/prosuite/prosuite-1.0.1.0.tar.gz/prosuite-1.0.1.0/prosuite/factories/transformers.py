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
from prosuite.transformer import Transformer
from prosuite.parameter import Parameter
from prosuite.dataset import BaseDataset
from prosuite.factories.enums import *

class Transformers:

    @classmethod
    def tr_combined_filter_0(cls, feature_class_to_filter: BaseDataset, input_filters: List[BaseDataset], expression: str) -> Transformer:
        """
        Creates a filtered feature class based on several other filters that use the same 'featureClassToFilter'.
        """
        
        result = Transformer("TrCombinedFilter(0)")
        result.parameters.append(Parameter("featureClassToFilter", feature_class_to_filter))
        if type(input_filters) == list:
            for element in input_filters:
                result.parameters.append(Parameter("inputFilters", element))
        else:
            result.parameters.append(Parameter("inputFilters", input_filters))
        result.parameters.append(Parameter("expression", expression))
        result.generate_name()
        return result

    @classmethod
    def tr_dissolve_0(cls, feature_class: BaseDataset, search: float = 0, neighbor_search_option: SearchOption = 0, attributes: List[str] = None, group_by: List[str] = None, constraint: str = None, create_multipart_features: bool = False) -> Transformer:
        """
        Transforms line feature class 'featureClass' by dissolving connected features
        """
        
        result = Transformer("TrDissolve(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.parameters.append(Parameter("Search", search))
        result.parameters.append(Parameter("NeighborSearchOption", neighbor_search_option))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        if type(group_by) == list:
            for element in group_by:
                result.parameters.append(Parameter("GroupBy", element))
        else:
            result.parameters.append(Parameter("GroupBy", group_by))
        result.parameters.append(Parameter("Constraint", constraint))
        result.parameters.append(Parameter("CreateMultipartFeatures", create_multipart_features))
        result.generate_name()
        return result

    @classmethod
    def tr_footprint_0(cls, multipatch_class: BaseDataset, attributes: List[str] = None) -> Transformer:
        """
        Transforms multipatches to polygons by taking their footprints
        """
        
        result = Transformer("TrFootprint(0)")
        result.parameters.append(Parameter("multipatchClass", multipatch_class))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_geometry_to_points_0(cls, feature_class: BaseDataset, component: GeometryComponent, attributes: List[str] = None) -> Transformer:
        """
        Transforms geometries to points. The transformed feature class has the attribute PartIndex and VertexIndex. These fields index from which polygon part the transformed polygon part was generated
        """
        
        result = Transformer("TrGeometryToPoints(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.parameters.append(Parameter("component", component))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_intersect_0(cls, intersected: BaseDataset, intersecting: BaseDataset) -> Transformer:
        """
        Transforms features of 'intersected' by intersecting them with features from 'intersecting'.
        If intersected is a line class and intersecting is a polygon class, then the resulting feature class has an attribute 'PartIntersected' which contains the (resultingFeature.Shape.Length \/ intersectedFeature.Shape.Length)
        """
        
        result = Transformer("TrIntersect(0)")
        result.parameters.append(Parameter("intersected", intersected))
        result.parameters.append(Parameter("intersecting", intersecting))
        result.generate_name()
        return result

    @classmethod
    def tr_line_to_polygon_0(cls, closed_line_class: BaseDataset, polyline_usage: PolylineConversion = 1, attributes: List[str] = None) -> Transformer:
        """
        Transforms closed lines of 'closedLineClass' to polygons
        """
        
        result = Transformer("TrLineToPolygon(0)")
        result.parameters.append(Parameter("closedLineClass", closed_line_class))
        result.parameters.append(Parameter("PolylineUsage", polyline_usage))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_make_table_0(cls, base_table: BaseDataset, view_or_table_name: str) -> Transformer:
        """
        Creates a table from an existing table or view in the database. This allows using tables that would otherwise not be usable because they have not been harvested as datasets in the data dictionary. Typical examples are:
        - Association tables in many-to-many relationship classes
        - Tables or views that are not part of the geodatabase.
        If the table is part of the geodatabase and registered as versioned it will be opened from the same version as the base table.
        """
        
        result = Transformer("TrMakeTable(0)")
        result.parameters.append(Parameter("baseTable", base_table))
        result.parameters.append(Parameter("viewOrTableName", view_or_table_name))
        result.generate_name()
        return result

    @classmethod
    def tr_make_table_1(cls, base_table: BaseDataset, sql: str, object_id_field: str) -> Transformer:
        """
        Creates a table from an SQL statement directly evaluated in the RDBMS. The same restrictions apply as for ArcGIS 'query layers'. For example, versioned data cannot be accessed, only the raw tables in the database including tables that are not registered as part of the geodatabase.
        """
        
        result = Transformer("TrMakeTable(1)")
        result.parameters.append(Parameter("baseTable", base_table))
        result.parameters.append(Parameter("sql", sql))
        result.parameters.append(Parameter("objectIdField", object_id_field))
        result.generate_name()
        return result

    @classmethod
    def tr_multiline_to_line_0(cls, feature_class: BaseDataset, attributes: List[str] = None) -> Transformer:
        """
        Transforms multipart lines to single lines. The transformed feature class has the attribute PartIndex. This field index from which line part the transformed line was generated
        """
        
        result = Transformer("TrMultilineToLine(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_multipolygon_to_polygon_0(cls, feature_class: BaseDataset, transformed_parts: PolygonPart = 0, attributes: List[str] = None) -> Transformer:
        """
        Transforms multipart polygons to single polygons. The transformed feature class has the attributes OuterRingIndex and InnerRingIndex. These fields index from which polygon part the transformed polygon was generated.
        The transformed feature class has also the attributes of 'featureClass', which can be accessed by 't0.<fieldName>'.
        """
        
        result = Transformer("TrMultipolygonToPolygon(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.parameters.append(Parameter("TransformedParts", transformed_parts))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_only_contained_features_0(cls, feature_class_to_filter: BaseDataset, containing: BaseDataset) -> Transformer:
        """
        Creates a filtered feature class containing only the features that are contained within features from 'containing'. The resulting feature class has the same properties and attributes as 'featureClassToFilter'.
        """
        
        result = Transformer("TrOnlyContainedFeatures(0)")
        result.parameters.append(Parameter("featureClassToFilter", feature_class_to_filter))
        result.parameters.append(Parameter("containing", containing))
        result.generate_name()
        return result

    @classmethod
    def tr_only_disjoint_features_0(cls, feature_class_to_filter: BaseDataset, disjoint: BaseDataset) -> Transformer:
        """
        Creates a filtered feature class containing only the features that are disjoint from features from 'disjoint'. Features that intersect any feature from 'disjoint' are filtered out. The resulting feature class has the same properties and attributes as 'featureClassToFilter'.
        """
        
        result = Transformer("TrOnlyDisjointFeatures(0)")
        result.parameters.append(Parameter("featureClassToFilter", feature_class_to_filter))
        result.parameters.append(Parameter("disjoint", disjoint))
        result.generate_name()
        return result

    @classmethod
    def tr_only_intersecting_features_0(cls, feature_class_to_filter: BaseDataset, intersecting: BaseDataset) -> Transformer:
        """
        Creates a filtered feature class containing only the features that intersect features from 'intersecting'.  The resulting feature class has the same properties and attributes as 'featureClassToFilter'.
        """
        
        result = Transformer("TrOnlyIntersectingFeatures(0)")
        result.parameters.append(Parameter("featureClassToFilter", feature_class_to_filter))
        result.parameters.append(Parameter("intersecting", intersecting))
        result.generate_name()
        return result

    @classmethod
    def tr_polygon_to_line_0(cls, feature_class: BaseDataset, attributes: List[str] = None) -> Transformer:
        """
        Transform polygon to line by taking the boundary of the polygons in 'featureClass'.
        The transformed feature class has also the attributes of 'featureClass', which can be accessed by 't0.<fieldName>'.
        """
        
        result = Transformer("TrPolygonToLine(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_project_0(cls, feature_class: BaseDataset, target_spatial_reference_id: int, attributes: List[str] = None) -> Transformer:
        """
        
        """
        
        result = Transformer("TrProject(0)")
        result.parameters.append(Parameter("featureClass", feature_class))
        result.parameters.append(Parameter("targetSpatialReferenceId", target_spatial_reference_id))
        if type(attributes) == list:
            for element in attributes:
                result.parameters.append(Parameter("Attributes", element))
        else:
            result.parameters.append(Parameter("Attributes", attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_spatial_join_0(cls, t0: BaseDataset, t1: BaseDataset, constraint: str = None, outer_join: bool = False, neighbor_search_option: SearchOption = 0, grouped: bool = False, t0_attributes: List[str] = None, t1_attributes: List[str] = None, t1_calc_attributes: List[str] = None) -> Transformer:
        """
        Transforms features of 't0' and features of 't1' to features, with shape of 't0' if they intersect.
        """
        
        result = Transformer("TrSpatialJoin(0)")
        result.parameters.append(Parameter("t0", t0))
        result.parameters.append(Parameter("t1", t1))
        result.parameters.append(Parameter("Constraint", constraint))
        result.parameters.append(Parameter("OuterJoin", outer_join))
        result.parameters.append(Parameter("NeighborSearchOption", neighbor_search_option))
        result.parameters.append(Parameter("Grouped", grouped))
        if type(t0_attributes) == list:
            for element in t0_attributes:
                result.parameters.append(Parameter("T0Attributes", element))
        else:
            result.parameters.append(Parameter("T0Attributes", t0_attributes))
        if type(t1_attributes) == list:
            for element in t1_attributes:
                result.parameters.append(Parameter("T1Attributes", element))
        else:
            result.parameters.append(Parameter("T1Attributes", t1_attributes))
        if type(t1_calc_attributes) == list:
            for element in t1_calc_attributes:
                result.parameters.append(Parameter("T1CalcAttributes", element))
        else:
            result.parameters.append(Parameter("T1CalcAttributes", t1_calc_attributes))
        result.generate_name()
        return result

    @classmethod
    def tr_table_append_0(cls, tables: List[BaseDataset]) -> Transformer:
        """
        
        """
        
        result = Transformer("TrTableAppend(0)")
        if type(tables) == list:
            for element in tables:
                result.parameters.append(Parameter("tables", element))
        else:
            result.parameters.append(Parameter("tables", tables))
        result.generate_name()
        return result

    @classmethod
    def tr_table_join_0(cls, t0: BaseDataset, t1: BaseDataset, relation_name: str, join_type: JoinType) -> Transformer:
        """
        Transforms table 't0' and table 't1', which must be related by 'relationName', to a joined table
        """
        
        result = Transformer("TrTableJoin(0)")
        result.parameters.append(Parameter("t0", t0))
        result.parameters.append(Parameter("t1", t1))
        result.parameters.append(Parameter("relationName", relation_name))
        result.parameters.append(Parameter("joinType", join_type))
        result.generate_name()
        return result

    @classmethod
    def tr_table_join_in_memory_0(cls, left_table: BaseDataset, right_table: BaseDataset, left_table_key: str, right_table_key: str, join_type: JoinType, many_to_many_table: BaseDataset = None, many_to_many_table_left_key: str = None, many_to_many_table_right_key: str = None) -> Transformer:
        """
        Creates a joined table with the fields from 'leftTable' and 'rightTable'.
        """
        
        result = Transformer("TrTableJoinInMemory(0)")
        result.parameters.append(Parameter("leftTable", left_table))
        result.parameters.append(Parameter("rightTable", right_table))
        result.parameters.append(Parameter("leftTableKey", left_table_key))
        result.parameters.append(Parameter("rightTableKey", right_table_key))
        result.parameters.append(Parameter("joinType", join_type))
        result.parameters.append(Parameter("ManyToManyTable", many_to_many_table))
        result.parameters.append(Parameter("ManyToManyTableLeftKey", many_to_many_table_left_key))
        result.parameters.append(Parameter("ManyToManyTableRightKey", many_to_many_table_right_key))
        result.generate_name()
        return result
