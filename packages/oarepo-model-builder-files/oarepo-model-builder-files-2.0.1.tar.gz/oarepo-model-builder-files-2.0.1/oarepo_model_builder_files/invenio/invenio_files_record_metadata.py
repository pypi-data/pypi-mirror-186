from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder

class InvenioFilesRecordMetadataBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_record_metadata"
    class_config = "record-metadata-class"
    template = "files-record-metadata"

    def finish(self, **extra_kwargs):
        super().finish(parent_settings=self.settings.parent_schema.settings, **extra_kwargs)