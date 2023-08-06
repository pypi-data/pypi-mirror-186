import importlib
import os
import sys
from pathlib import Path

import autumn8  # systemwide import (to match user's annotations import) - not the local lib/code one
from click import ClickException

sys.path.append(os.getcwd())

PYTHON_FILE_EXTENSION = ".py"


def analyze_python_source(model_file_path, model_script_args=[]):
    # spec = importlib.util.spec_from_file_location("__main__", model_file_path)
    # module = importlib.util.module_from_spec(spec)
    # spec.loader.exec_module(module)
    args = sys.argv
    sys.argv = [args[0]]
    importlib.import_module(
        model_file_path[: -len(PYTHON_FILE_EXTENSION)]
    )  # TODO relative imports not working (fix: https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
    sys.argv = [args, model_script_args]
    # exec(open(model_file_path).read(), {})
    models = autumn8.attached_models

    if len(models) < 1:
        # TODO try to manually find the model without autodl attachments
        raise ClickException(
            "The provided model file does not contain any models attached with `autumn8.attach_model`.\n"
            + "Please refer to our documentation to read on how to attached your models."
        )
    if len(models) > 1:
        print(
            "WARNING: Our current CLI implementation does not support multiple models in one file yet. Please contact us and file an inquiry to add this feature if you need it."
        )

    model, dummy_input, interns, externs, max_search_depth = models[-1]
    # idk, maybe there is better way to diffrentiate between tensorflow and pytorch source
    if "tensorflow" in sys.modules:
        import tensorflow as tf

        if isinstance(model, tf.keras.Model):
            model_file_bytes = autumn8.export_tensorflow_model_repr(
                model, dummy_input
            )
            return model_file_bytes, dummy_input, "TENSORFLOW"

    model_file_bytes = autumn8.export_pytorch_model_repr(
        model, dummy_input, interns, externs, max_search_depth
    )

    return model_file_bytes, dummy_input, "PYTORCH"


def load_tensorflow_protobuf(model_file_path):
    import tensorflow.compat.v1 as tf
    from google.protobuf.message import DecodeError
    from tensorflow.core.protobuf import saved_model_pb2
    from tensorflow.python.platform import gfile
    from tensorflow.python.util import compat

    graph_def = tf.GraphDef()

    with tf.Session() as sess:
        try:
            # this load method cannot load models from https://tfhub.dev/
            # crashes with `google.protobuf.message.DecodeError: Error parsing message with type 'tensorflow.GraphDef'`

            with tf.gfile.GFile(model_file_path, "rb") as file:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(file.read())

                return [n for n in graph_def.node]

        except DecodeError:
            # this load method cannot load models from @marcink
            # nasnet is missing input dimensions
            # posenet is missing meta_graphs - crashes with `IndexError: list index (0) out of range` on tf.import_graph_def(sm.meta_graphs[0].graph_def)
            with gfile.GFile(model_file_path, "rb") as file:
                data = compat.as_bytes(file.read())
                sm = saved_model_pb2.SavedModel()
                sm.ParseFromString(data)
                tf.import_graph_def(sm.meta_graphs[0].graph_def)
                return [n for n in sm.meta_graphs[0].graph_def.node]


def infer_tensorflow_protobuf_input_shape(model_file_path):
    graph_nodes = load_tensorflow_protobuf(model_file_path)
    inferred_batch_size, inferred_input_dims = (
        None,
        [],
    )

    for node in graph_nodes:
        if node.op == "Placeholder":
            shape_proto = node.attr["shape"]
            dim_sizes = [dim.size for dim in shape_proto.shape.dim]
            print("Detected input layer with shape", dim_sizes)
            dim_sizes += [None, None, None, None]
            dim_sizes = dim_sizes[0:4]
            dim_sizes = [None if size == -1 else size for size in dim_sizes]

            if len(shape_proto.shape.dim) > 0:
                [
                    inferred_batch_size,
                    *inputs,
                ] = dim_sizes
                if len(inputs) > 2:
                    inputs = [
                        inputs[-1],
                        *inputs[:-1],
                    ]
                inferred_input_dims.append(inputs)

    return (inferred_batch_size, inferred_input_dims)


def analyze_model_file(model_file_path, model_script_args=[]):
    extension = Path(model_file_path).suffixes[-1]

    (
        model_file,
        inferred_model_name,
        framework,
        inferred_quantization,
    ) = (None, None, None, None)
    _inferred_batch_size = None
    inferred_input_dims = []

    model_file = model_file_path
    inferred_model_name = Path(model_file_path).stem
    inferred_quantization = "FP32"

    if extension in [".py"]:
        model_file_bytes, dummy_input, framework = analyze_python_source(
            model_file_path, model_script_args
        )
        model_file_name = f"./{inferred_model_name}.adlpt"
        model_file = open(model_file_name, mode="wb")
        model_file.write(model_file_bytes.getbuffer())
        model_file.close()
        model_file = model_file_name

        [
            _inferred_batch_size,
            *inferred_input_dims,
        ] = dummy_input.shape

        inferred_input_dims = [inferred_input_dims]

    elif extension in [".mar"]:
        framework = "PYTORCH"
        # TODO analyze .mar file for input shape

    elif extension in [".pb", ".h5"]:
        framework = "TENSORFLOW"

    elif extension in [
        ".tflite"
    ]:  # TODO - add this extension also to the UI autofiller
        framework = "TFLITE"
        raise ClickException(f"Files with '{extension}' are not supported yet")

    elif extension in [".pt", ".pth"]:
        raise ClickException(
            f"Files with '{extension}' are not supported - please contact us at support@autumn8.ai to add the support."
        )

    else:
        raise ClickException(
            f"Files with '{extension}' are not supported - please contact us at support@autumn8.ai to add the support."
        )

    return (
        model_file,
        inferred_model_name,
        framework,
        inferred_quantization,
        inferred_input_dims,
    )
