from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.utils.jinja import package_name

class InvenioFilesParentSchemaBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_parent_schema"
    template = "files-parent-schema"

    def finish(self, **extra_kwargs):
        python_path = self.class_to_path(self.settings.parent_schema.model["oarepo:marshmallow"]["schema-class"])
        self.process_template(
            python_path,
            self.template,
            current_package_name=package_name(self.settings.parent_schema.model["oarepo:marshmallow"]["schema-class"]),
            **extra_kwargs,
        )