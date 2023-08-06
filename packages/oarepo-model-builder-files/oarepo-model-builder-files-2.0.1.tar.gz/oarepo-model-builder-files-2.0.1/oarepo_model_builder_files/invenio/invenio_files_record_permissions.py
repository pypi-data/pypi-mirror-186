from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder

class InvenioFilesRecordPermissionsBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_permissions"
    class_config = "record-permissions-class"
    template = "files-permissions"