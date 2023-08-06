from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder

class InvenioFilesRecordBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_record"
    class_config = "record-class"
    template = "files-record"

    def finish(self, **extra_kwargs):
        super().finish(parent_settings=self.settings.parent_schema.settings, **extra_kwargs)

