import copy
from pathlib import Path
from typing import Union

from oarepo_model_builder.builder import ModelBuilder
from oarepo_model_builder.conflict_resolvers import AutomaticResolver
from oarepo_model_builder.entrypoints import create_builder_from_entrypoints
from oarepo_model_builder.schema import ModelSchema
from oarepo_model_builder.profiles import Profile

from oarepo_model_builder.utils.hyphen_munch import HyphenMunch
import munch


class FileProfile(Profile):
    # schema - ideas - build new schema from specifications of the submodel??
    # but I still probably need some of the old settings in the new schema and this would overwrite them?
    #
    # required_profiles = ('model',)
    def build(
            self,
            model: ModelSchema,
            output_directory: Union[str, Path],
            builder: ModelBuilder,
    ):
        # todo how the settings for the file model should look like exactly?
        # todo how the schema for defining the file model (or submodels in general) should look like? Should there be a
        # specific schema for types of models to prevent recursion for specific types for example?
        # new_model = copy.deepcopy(model)
        parent_model_builder = create_builder_from_entrypoints(
            profile='model', conflict_resolver=AutomaticResolver(resolution_type="replace"), overwrite=True
        )
        parent_model_builder.set_schema(model)
        parent_model_builder._run_model_preprocessors(model)

        new_schema = model.schema["files"]
        new_model = ModelSchema(file_path=model.file_path, content=new_schema, included_models=model.included_schemas,
                                loaders=model.loaders)


        new_model.schema.settings["package"] = model.schema.settings.package


        new_model.schema.settings.python = HyphenMunch()
        python = new_model.schema.settings.python
        new_model.schema.settings["parent-schema"] = model.schema

        python.use_isort = model.schema.settings.python.use_isort
        python.use_black = model.schema.settings.python.use_black

        builder.build(new_model, output_directory)