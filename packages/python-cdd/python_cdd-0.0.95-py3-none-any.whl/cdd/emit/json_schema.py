"""
JSON schema emitter
"""

from collections import OrderedDict
from functools import partial
from json import dump
from operator import add

from cdd.emit.docstring import docstring
from cdd.emit.utils.json_schema_utils import param2json_schema_property
from cdd.pure_utils import SetEncoder, deindent


def json_schema(
    intermediate_repr,
    identifier=None,
    emit_original_whitespace=False,
):
    """
    Construct a JSON schema dict

    :param intermediate_repr: a dictionary of form
        {  "name": Optional[str],
           "type": Optional[str],
           "doc": Optional[str],
           "params": OrderedDict[str, {'typ': str, 'doc': Optional[str], 'default': Any}]
           "returns": Optional[OrderedDict[Literal['return_type'],
                                           {'typ': str, 'doc': Optional[str], 'default': Any}),)]] }
    :type intermediate_repr: ```dict```

    :param identifier: The `$id` of the schema
    :type identifier: ```str```

    :param emit_original_whitespace: Whether to emit original whitespace (in top-level `description`) or strip it out
    :type emit_original_whitespace: ```bool```

    :return: JSON Schema dict
    :rtype: ```dict```
    """
    assert isinstance(
        intermediate_repr, dict
    ), "Expected `dict` got `{type_name}`".format(
        type_name=type(intermediate_repr).__name__
    )
    if identifier is None:
        identifier = "https://offscale.io/{}.schema.json".format(
            intermediate_repr["name"]
        )
    required = []
    _param2json_schema_property = partial(param2json_schema_property, required=required)
    properties = dict(
        map(_param2json_schema_property, intermediate_repr["params"].items())
    )

    return {
        "$id": identifier,
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": deindent(
            add(
                *map(
                    partial(
                        docstring,
                        emit_default_doc=True,
                        emit_original_whitespace=emit_original_whitespace,
                        emit_types=True,
                    ),
                    (
                        {
                            "doc": intermediate_repr["doc"],
                            "params": OrderedDict(),
                            "returns": None,
                        },
                        {
                            "doc": "",
                            "params": OrderedDict(),
                            "returns": intermediate_repr["returns"],
                        },
                    ),
                )
            )
        ).lstrip("\n")
        or None,
        "type": "object",
        "properties": properties,
        "required": required,
    }


def json_schema_file(input_mapping, output_filename):
    """
    Emit `input_mapping`—as JSON schema—into `output_filename`

    :param input_mapping: Import location of mapping/2-tuple collection.
    :type input_mapping: ```Dict[str, AST]```

    :param output_filename: Output file to write to
    :type output_filename: ```str```
    """
    schemas_it = (json_schema(v) for k, v in input_mapping.items())
    schemas = (
        {"schemas": list(schemas_it)} if len(input_mapping) > 1 else next(schemas_it)
    )
    with open(output_filename, "a") as f:
        dump(schemas, f, cls=SetEncoder)


__all__ = ["json_schema", "json_schema_file"]
