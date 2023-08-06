from functools import partial
from typing import Dict, List, Optional, Tuple, Union, cast

import pandas as pd

from .base_generators import NLPEmbeddingGenerator
from .models import NLP_PRETRAINED_MODELS
from .usecases import UseCases
from .utils import is_list_of, logger

try:
    import torch
    from datasets import Dataset
    from transformers import AutoTokenizer  # type: ignore
except ImportError:
    raise ImportError(
        "To enable embedding generation, "
        "the arize module must be installed with the EmbeddingGeneration option: "
        "pip install 'arize[EmbeddingGeneration]'."
    )


class EmbeddingGeneratorForTabularFeatures(NLPEmbeddingGenerator):
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n"
            f"  use_case={self.use_case},\n"
            f"  model_name={self.model_name},\n"
            f"  tokenizer_max_length={self.tokenizer_max_length},\n"
            f"  tokenizer={self.tokenizer.__class__},\n"
            f"  model={self.model.__class__},\n"
            f")"
        )

    def __init__(
        self,
        model_name: str = "xlm-roberta-large",
        **kwargs,
    ):
        if model_name not in NLP_PRETRAINED_MODELS:
            raise ValueError(
                f"model_name not supported. Check supported models with "
                f"`AutoEmbeddingGenerator.list_pretrained_models()`"
            )
        super(EmbeddingGeneratorForTabularFeatures, self).__init__(
            use_case=UseCases.STRUCTURED.TABULAR_FEATURES,
            model_name=model_name,
            **kwargs,
        )

    def generate_embeddings(
        self,
        df: pd.DataFrame,
        selected_columns: List[str],
        rename_cols_mapper: Optional[Dict[str, str]] = None,
        return_prompt_col: Optional[bool] = False,
        method: Optional[str] = "cls",
    ) -> Union[pd.Series, Tuple[pd.Series, pd.Series]]:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df must be a pandas DataFrame")
        if not is_list_of(selected_columns, str):
            raise TypeError("columns must be a list of column names (strings)")
        if not all(col in df.columns for col in selected_columns):
            missing_cols = [col for col in selected_columns if col not in df.columns]
            raise ValueError(
                "selected_columns list must only contain columns of the dataframe. "
                f"The following columns are not found {missing_cols}"
            )
        if rename_cols_mapper is not None:
            if not isinstance(rename_cols_mapper, dict):
                raise TypeError(
                    "rename_cols_mapper must be a dictionary mapping column names to new column "
                    "names"
                )
            for k, v in rename_cols_mapper.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    raise ValueError(
                        "rename_cols_mapper dictionary keys and values should be strings"
                    )
            if not all(col in df.columns for col in rename_cols_mapper.keys()):
                missing_cols = [
                    col for col in rename_cols_mapper.keys() if col not in df.columns
                ]
                raise ValueError(
                    "rename_cols_mapper must only contain keys which are columns of the dataframe. "
                    f"The following columns are not found {missing_cols}"
                )

        if rename_cols_mapper is not None:
            new_cols = [
                rename_cols_mapper[col] if col in rename_cols_mapper.keys() else col
                for col in selected_columns
            ]
            prompts = df.rename(columns=rename_cols_mapper).apply(
                lambda row: self.__prompt_fn(row, new_cols), axis=1
            )
        else:
            prompts = df.apply(
                lambda row: self.__prompt_fn(row, selected_columns), axis=1
            )
        ds = Dataset.from_dict({"prompt": prompts})
        ds.set_transform(partial(self.tokenize, text_feat_name="prompt"))
        logger.info("Generating embedding vectors")
        ds = ds.map(
            lambda batch: self._get_embedding_vector(batch, method),
            batched=True,
            batch_size=self.batch_size,
        )

        if return_prompt_col:
            return cast(pd.DataFrame, ds.to_pandas())["embedding_vector"], cast(
                pd.Series, prompts
            )

        return cast(pd.DataFrame, ds.to_pandas())["embedding_vector"]

    @staticmethod
    def __prompt_fn(row: pd.DataFrame, columns: List[str]) -> str:
        msg = ""
        for col in columns:
            repl_text = col.replace("_", " ")
            value = row[col]
            if isinstance(value, str):
                value = value.strip()
            msg += f"The {repl_text} is {value}. "
        return msg.strip(" ")
