from enum import Enum


class ApplicationType(Enum):

    UNKNOWN = "unknown"
    REGRESSION = "regression"
    MULTIOUTPUT_REGRESSION = "multioutput_regression"
    CLASSIFICATION = "classification"
    BINARY_CLASSIFICATION = "binary_classification"
    MULTICLASS_CLASSIFICATION = "multiclass_classification"
    MULTIOUTPUT_CLASSIFICATION = "multioutput_classification"
    MULTICLASS_MULTIOUTPUT_CLASSIFICATION = "multiclass_multioutput_classification"


class MLFramework(Enum):

    SKLEARN = "sklearn"
    XGBOOST = "xgboost"
    LIGHTGBM = "lightgbm"
    TENSORFLOW = "tensorflow"
