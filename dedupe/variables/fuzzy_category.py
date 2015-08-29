from __future__ import print_function

from dedupe.variables.base import DerivedType, FieldType
from dedupe import predicates
from fuzzycategory import FuzzyCategory

class FuzzyCategoricalType(FieldType) :
    type = "FuzzyCategorical"
    _predicate_functions = [predicates.wholeFieldPredicate]

    def __init__(self, definition) :

        super(FuzzyCategoricalType, self ).__init__(definition)
        
        self.comparator = FuzzyCategory(definition['field'],
                                        definition['corpus'],
                                        definition['other fields'])
