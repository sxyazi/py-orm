from Types import Field

class ModelMeta(type):
    def __new__(cls, name, bases, namespace, **kwds):
        if not name == 'BaseModel':
            # 表名
            meta, table = namespace.get('Meta', None), name.lower()
            if meta is not None:
                table = getattr(meta, 'table', '') or table
            namespace['table'] = table

            # 字段
            fields = {}
            for k, v in namespace.items():
                if isinstance(v, Field): fields[k] = v
            namespace['fields'] = fields

        return type.__new__(cls, name, bases, namespace, **kwds)

class BaseModel(metaclass=ModelMeta):
    def insert(self):
        keys = self.fields.keys()

        return 'insert into {table}({keys}) values({values})'.format(
            table=self.table,
            keys=', '.join(keys),
            values=', '.join(map(lambda k: str(getattr(self, k)), keys))
        )
