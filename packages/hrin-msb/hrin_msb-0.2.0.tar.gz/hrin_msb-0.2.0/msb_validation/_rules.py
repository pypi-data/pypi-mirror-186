from ._schema import InputField
from ._decorators import ValidationSchema


class DefaultRules:
	date = InputField.Date(regex="^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$")
	pk = InputField.String(required=True)
	gender = InputField.String(allowed=['M', 'F', 'O'])

	@staticmethod
	def pk_validation_rule(pk_name: str):
		return ValidationSchema(**{pk_name: InputField.String(required=True)})
