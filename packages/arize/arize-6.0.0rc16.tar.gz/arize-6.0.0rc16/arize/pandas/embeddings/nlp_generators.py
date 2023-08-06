from functools import partial
from typing import Optional, cast

import pandas as pd

from .base_generators import NLPEmbeddingGenerator
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


class EmbeddingGeneratorForNLPSequenceClassification(NLPEmbeddingGenerator):
    def __init__(self, model_name: str = "distilbert-base-uncased", **kwargs):
        super(EmbeddingGeneratorForNLPSequenceClassification, self).__init__(
            use_case=UseCases.NLP.SEQUENCE_CLASSIFICATION,
            model_name=model_name,
            **kwargs,
        )

    def generate_embeddings(
        self,
        text_col: pd.Series,
        class_label_col: Optional[pd.Series] = None,
    ) -> pd.Series:
        if not isinstance(text_col, pd.Series):
            raise TypeError("text_col must be a pandas Series")
        if class_label_col is not None:
            if not isinstance(class_label_col, pd.Series):
                raise TypeError("class_label_col must be a pandas Series")

        if class_label_col is not None:
            df = pd.concat({"text": text_col, "class_label": class_label_col}, axis=1)
            prepared_text_col = df.apply(
                lambda row: row["text"] + f" The "
                f"classification label is {row['class_label']}.",
                axis=1,
            )
            ds = Dataset.from_dict({"text": prepared_text_col})
        else:
            ds = Dataset.from_dict({"text": text_col})
        ds.set_transform(partial(self.tokenize, text_feat_name="text"))
        logger.info("Generating embedding vectors")
        ds = ds.map(
            lambda batch: self._get_embedding_vector(batch, "cls"),
            batched=True,
            batch_size=self.batch_size,
        )
        return cast(pd.DataFrame, ds.to_pandas())["embedding_vector"]
