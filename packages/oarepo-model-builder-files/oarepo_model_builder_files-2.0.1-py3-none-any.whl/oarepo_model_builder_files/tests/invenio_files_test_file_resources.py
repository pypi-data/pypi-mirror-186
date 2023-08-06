from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder

class InvenioFilesTestFileResourcesBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_files_test_files_resources"
    template = "files-test-file-resources"
    MODULE = "tests.files.test_files_resources"

    def finish(self, **extra_kwargs):
        python_path = self.module_to_path(self.MODULE)
        self.process_template(
            python_path,
            self.template,
            parent_settings=self.settings.parent_schema.settings,
            **extra_kwargs,
        )