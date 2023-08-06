from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder

class InvenioRecordServiceConfigBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_record_service_config"
    class_config = "record-service-config-class"
    template = "files-service-config"

    def finish(self, **extra_kwargs):
        super().finish(parent_settings=self.settings.parent_schema.settings, **extra_kwargs)