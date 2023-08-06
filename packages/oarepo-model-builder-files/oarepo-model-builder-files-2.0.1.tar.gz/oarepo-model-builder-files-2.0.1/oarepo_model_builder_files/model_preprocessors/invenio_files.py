from oarepo_model_builder.model_preprocessors import ModelPreprocessor
from oarepo_model_builder.utils.camelcase import camel_case

class InvenioModelFilesPreprocessor(ModelPreprocessor):
    TYPE = "invenio_files"

    def transform(self, schema, settings):
        parent_record_prefix = camel_case(
                        settings.parent_schema.settings.package.rsplit(".", maxsplit=1)[-1]
                    )
        model_python = settings.parent_schema.settings.python
        python = settings.python
        python.setdefault("record-prefix", f"{parent_record_prefix}File")
        python.setdefault("record-permissions-class", model_python.record_permissions_class)
        python.setdefault("profile-package", "files")
        python.setdefault("record-search-options-class", "")
        settings["collection-url"] = f'{settings.parent_schema.settings["collection-url"]}<pid_value>'
        settings.parent_schema.settings.python.setdefault("record-service-config-components", []).append("invenio_records_resources.services.records.components.FilesOptionsComponent")


        """"""