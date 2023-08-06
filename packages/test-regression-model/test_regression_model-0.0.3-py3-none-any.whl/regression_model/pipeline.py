from feature_engine.encoding import OrdinalEncoder, RareLabelEncoder  # type: ignore
from feature_engine.imputation import AddMissingIndicator  # type: ignore
from feature_engine.imputation import CategoricalImputer  # type: ignore
from feature_engine.imputation import MeanMedianImputer  # type: ignore
from feature_engine.selection import DropFeatures  # type: ignore
from feature_engine.transformation import LogTransformer  # type: ignore
from feature_engine.wrappers import SklearnTransformerWrapper  # type: ignore
from sklearn.linear_model import Lasso  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore
from sklearn.preprocessing import Binarizer, MinMaxScaler  # type: ignore

from regression_model.config.core import config  # type: ignore
from regression_model.processing import features as pp  # type: ignore

price_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string missing
        (
            "missing_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_config.categorical_vars_with_na_missing,
            ),
        ),
        (
            "frequent_imputation",
            CategoricalImputer(
                imputation_method="frequent",
                variables=config.model_config.categorical_vars_with_na_frequent,
            ),
        ),
        # add missing indicator
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_vars_with_na),
        ),
        # impute numerical variables with the mean
        (
            "mean_imputation",
            MeanMedianImputer(
                imputation_method="mean",
                variables=config.model_config.numerical_vars_with_na,
            ),
        ),
        # == TEMPORAL VARIABLES ====
        (
            "elapsed_time",
            pp.TemporalVariableTransformer(
                variables=config.model_config.temporal_vars,
                reference_variable=config.model_config.ref_var,
            ),
        ),
        ("drop_features", DropFeatures(features_to_drop=[config.model_config.ref_var])),
        # ==== VARIABLE TRANSFORMATION =====
        ("log", LogTransformer(variables=config.model_config.numericals_log_vars)),
        (
            "binarizer",
            SklearnTransformerWrapper(
                transformer=Binarizer(threshold=0),
                variables=config.model_config.binarize_vars,
            ),
        ),
        # === mappers ===
        (
            "mapper_qual",
            pp.Mapper(
                variables=config.model_config.qual_vars,
                mappings=config.model_config.qual_mappings,
            ),
        ),
        (
            "mapper_exposure",
            pp.Mapper(
                variables=config.model_config.exposure_vars,
                mappings=config.model_config.exposure_mappings,
            ),
        ),
        (
            "mapper_finish",
            pp.Mapper(
                variables=config.model_config.finish_vars,
                mappings=config.model_config.finish_mappings,
            ),
        ),
        (
            "mapper_garage",
            pp.Mapper(
                variables=config.model_config.garage_vars,
                mappings=config.model_config.garage_mappings,
            ),
        ),
        # == CATEGORICAL ENCODING
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.01, n_categories=1, variables=config.model_config.categorical_vars
            ),
        ),
        # encode categorical variables using the target mean
        (
            "categorical_encoder",
            OrdinalEncoder(
                encoding_method="ordered",
                variables=config.model_config.categorical_vars,
            ),
        ),
        ("scaler", MinMaxScaler()),
        (
            "Lasso",
            Lasso(
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
