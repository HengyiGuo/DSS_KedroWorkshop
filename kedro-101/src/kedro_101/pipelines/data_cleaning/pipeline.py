"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import data_cleaning


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            data_cleaning,
            inputs="train_df",
            outputs="train_clean",
            name="data_cleaning"
        )
    ])
