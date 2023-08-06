"""
This is a boilerplate pipeline 'build_recommendations_based_similar'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from multi_recommender.pipelines.build_recommendations_based_similar.nodes import (
    build_recommendations_node
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        build_recommendations_node
    ])
