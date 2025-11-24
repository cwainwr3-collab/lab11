"""Replaces PII entities with initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.services.validators import validate_type

class Initial(Operator):
    """Reduces PII entity to its initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: first initial of each PII."""
        #creating variable to hold output we will return
        output = ""

        # Splitting text so that we can print each initial
        textArray = text.split()

        # Loop for printing out each inital in our textArray
        last_index = len(textArray) -1
        for index, each in enumerate(textArray):
            temp = each
            output += temp[0]
            if index == last_index:
                output += "."
            else:
                output += ". "        
        print(output)
        return output



    def validate(self, params: Dict = None) -> None:
        """initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize