import io
import json
import os
import pickle
import sys
import zipfile

import torch

from autumn8.lib.package_resolver import package
from autumn8.common._version import __version__

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


def write_model(model, dummy_input, bytes):
    traced = torch.jit.trace(model, dummy_input)
    traced.save(bytes)


def export_tensorflow_model_repr(
    model, dummy_input, interns=[], externs=[], max_search_depth=5
):
    return export_model_repr(
        model, dummy_input, "TENSORFLOW", interns, externs, max_search_depth
    )


def export_pytorch_model_repr(
    model, dummy_input, interns=[], externs=[], max_search_depth=5
):
    return export_model_repr(
        model, dummy_input, "PYTORCH", interns, externs, max_search_depth
    )


def export_model_repr(
    model, dummy_input, framework, interns=[], externs=[], max_search_depth=5
):
    bytes = io.BytesIO()

    if not isinstance(dummy_input, tuple):
        dummy_input = (dummy_input,)

    if framework == "PYTORCH":
        externs.append("torch")
        externs.append("torchvision")

    if framework == "TENSORFLOW":
        externs.append("tensorflow")

    file, requirements, package_name = package(
        model, interns, externs, max_search_depth
    )

    with zipfile.ZipFile(bytes, "w") as zip:
        zip.writestr(
            "MANIFEST",
            json.dumps(
                {
                    "version": __version__,
                    "package_name": package_name,
                }
            ),
        )
        zip.write(file.name, arcname="model.package")
        requirement_list = []
        for package_name, package_version in requirements.items():
            requirement_list.append(f"{package_name}=={package_version}")

        zip.writestr("requirements.txt", "\n".join(requirement_list))

    bytes.seek(0)
    return bytes


def load_model(filename):
    with zipfile.ZipFile(filename) as z:
        with z.open("MANIFEST", "r") as manifest:
            package_name = json.loads(manifest.read())["package_name"]
        with z.open("model.package", "r") as model_file:
            resource_name = "model.pkl"
            imp = torch.package.PackageImporter(model_file)
            loaded_model = imp.load_pickle(package_name, resource_name)
            return loaded_model


attached_models = []


# TODO: create 'annotate' module?
def attach_model(
    model, example_input, interns=[], externs=[], max_search_depth=5
):
    attached_models.append(
        (model, example_input, interns, externs, max_search_depth)
    )
