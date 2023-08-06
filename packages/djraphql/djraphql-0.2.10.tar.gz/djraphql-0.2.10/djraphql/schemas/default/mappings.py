from django.db.models import Avg, Count, Max, Min, Sum
from graphene import String, ID, Int, Float, Boolean, DateTime, Date


DJANGO_TYPE_NAMES_TO_GRAPHENE_TYPES = {
    "AutoField": ID,
    "IntegerField": Int,
    "PositiveIntegerField": Int,
    "BigIntegerField": Int,
    "ForeignKey": ID,
    "OneToOneField": ID,
    "ManyToManyField": ID,
    "DecimalField": Float,
    "FloatField": Float,
    "DateField": Date,
    "DateTimeField": DateTime,
    "CharField": String,
    "TextField": String,
    "BooleanField": Boolean,
    "NullBooleanField": Boolean,
    "SmallIntegerField": Int,
}

AGGREGATE_FIELD_NAMES_TO_DJANGO_FUNCTIONS = {
    "_sum": Sum,
    "_min": Min,
    "_max": Max,
    "_avg": Avg,
    "_count": Count,
}


class Types:
    AGGREGATE_RESULT_TYPE = "aggregate_result_type"
    AGGREGATE_BASIC_TYPE = "aggregate_basic_type"
    AGGREGATE_GROUP_BY_TYPE = "aggregate_group_by_type"
    AGGREGATE_QUERY_TYPE = "aggregate_query_type"
    BASIC_TYPE = "basic_type"
    BY_PK_QUERY_TYPE = "by_pk_query_type"
    DELETE_MUTATION_RESOLVER = "delete_mutation_resolver"
    DELETE_MUTATION_TYPE = "delete_mutation_type"
    ENUM_TYPE = "enum_type"
    INSERT_INPUT_TYPE = "insert_input_type"
    INSERT_MUTATION_RESOLVER = "insert_mutation_resolver"
    INSERT_MUTATION_TYPE = "insert_mutation_type"
    LIST_UPDATE_INPUT_TYPE = "list_update_input_type"
    MANY_QUERY_TYPE = "many_query_type"
    NESTED_ITEM_INSERT_TYPE = "nested_item_insert_type"
    NESTED_ITEM_UPDATE_TYPE = "nested_item_update_type"
    ORDER_CLAUSE_TYPE = "order_clause_type"
    PK_INPUT_TYPE = "pk_input_type"
    UPDATE_INPUT_TYPE = "update_input_type"
    UPDATE_MUTATION_RESOLVER = "update_mutation_resolver"
    UPDATE_MUTATION_TYPE = "update_mutation_type"
    WHERE_CLAUSE_TYPE = "where_clause_type"
    WHERE_PREDICATE_INPUT_TYPE = "where_predicate_input_type"
    TAG_TO_PK_TYPE = "tag_to_pk_type"
