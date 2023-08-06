import dataclasses


@dataclasses.dataclass()
class DbVendorConfig:
	query_to_list_tables: str
	query_to_drop_table: str
	excluded_tables: list

	def queries_to_drop_multiple_tables(self, table_list) -> list:
		_drop_table_queries = []
		if isinstance(table_list, list) and len(table_list) > 0:
			for table in table_list:
				if table[0] not in self.excluded_tables and self.query_to_drop_table.strip(" ") != "":
					_drop_table_queries.append(self.query_to_drop_table.format(table_name=table[0]))
		return _drop_table_queries