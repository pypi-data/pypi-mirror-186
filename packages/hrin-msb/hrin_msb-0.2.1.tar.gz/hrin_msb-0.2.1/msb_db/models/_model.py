from django.core.serializers import serialize
from django.db import models as Models

from msb_cipher import Cipher
from ._model_manager import MsbModelManager
from .._constants import (COLUMN_NAME_DELETED, COLUMN_NAME_DELETED_BY)


class MsbModel(Models.Model):
	_private_fields = []
	_identifier_field = ""

	class Meta:
		abstract = True

	@property
	def related_fields(self):
		fields = []
		for field in self._meta.fields:
			if field.get_internal_type() in ['ForeignKey']:
				fields.append(field.name)
		return fields

	@property
	def pk_name(self):
		return self._meta.pk.attname

	@property
	def pk_value(self):
		return getattr(self, self.pk_name) if self.pk_name is not None else ""

	@property
	def identifier(self):
		return f"{getattr(self, self._identifier_field)}" if hasattr(self, self._identifier_field) else ""

	def dict(self, encrypted=True):
		try:
			return {
				k: v if (k not in [
					self._meta.pk.attname, *self._private_fields
				] or not encrypted) else Cipher.encrypt(v)
				for k, v in super().__dict__.items()
				if not k.startswith('__') and not k.startswith('_') and not callable(k)
			}

		except Exception:
			return dict()

	@property
	def serialized(self):
		return serialize('python', [self])

	def delete(self, deleted_by=None, using=None, keep_parents=False):
		if hasattr(self, COLUMN_NAME_DELETED):
			setattr(self,COLUMN_NAME_DELETED, True)

		if hasattr(self, COLUMN_NAME_DELETED_BY):
			setattr(self,COLUMN_NAME_DELETED_BY, deleted_by)
		self.save()
		return True

	def __str__(self):
		return f"<{self.__class__.__name__} [{self.pk_value}]: {self.identifier}>"

	def __unicode__(self):
		return self.__str__()

	def __repr__(self):
		return self.__str__()

	@property
	def db_query(self):
		return self.objects

	objects = MsbModelManager()
