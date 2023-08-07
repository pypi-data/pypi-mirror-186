import json

from mlflow.utils.proto_json_utils import (
    NumpyEncoder,
    _get_jsonable_obj,
    parse_tf_serving_input,
)


def patch_feature_serving_predictions_to_json(raw_predictions, output):
    predictions = _get_jsonable_obj(raw_predictions, pandas_orient="records")
    json.dump({"features": predictions}, output, cls=NumpyEncoder)
