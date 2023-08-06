from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioFilesSchemaBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_schema"
    class_config = "record-schema-class"
    template = "files-schema"