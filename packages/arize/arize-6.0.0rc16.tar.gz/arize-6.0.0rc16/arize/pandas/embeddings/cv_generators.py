from functools import partial
from typing import cast

import pandas as pd

from .base_generators import CVEmbeddingGenerator
from .usecases import UseCases
from .utils import logger

try:
    import torch
    from datasets import Dataset
except ImportError:
    raise ImportError(
        "To enable embedding generation, "
        "the arize module must be installed with the EmbeddingGeneration option: "
        "pip install 'arize[EmbeddingGeneration]'."
    )


class EmbeddingGeneratorForCVImageClassification(CVEmbeddingGenerator):
    def __init__(self, model_name: str = "google/vit-base-patch32-224-in21k", **kwargs):
        super(EmbeddingGeneratorForCVImageClassification, self).__init__(
            use_case=UseCases.CV.IMAGE_CLASSIFICATION, model_name=model_name, **kwargs
        )

    def generate_embeddings(self, local_image_path_col: pd.Series) -> pd.Series:
        if not isinstance(local_image_path_col, pd.Series):
            raise TypeError("local_image_path_col_name must be pandas Series object")

        # Validate that there are no null image paths
        if local_image_path_col.isnull().any():
            raise ValueError(
                f"There can't be any null values in the local_image_path_col series"
            )

        ds = Dataset.from_dict({"local_path": local_image_path_col})
        ds.set_transform(
            partial(
                self.extract_image_features,
                local_image_feat_name="local_path",
            )
        )
        logger.info("Generating embedding vectors")
        ds = ds.map(
            lambda batch: self._get_embedding_vector(batch, "avg"),
            batched=True,
            batch_size=self.batch_size,
        )
        return cast(pd.DataFrame, ds.to_pandas())["embedding_vector"]
