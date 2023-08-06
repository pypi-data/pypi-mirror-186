"""
This is a boilerplate pipeline 'build_recommendations_based_similar'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from multi_recommender.pipelines.build_recommendations_based_similar.scripts.anime_pipeline_module import (
    get_anime_recommendations
)

build_recommendations_node = node(
    func=get_anime_recommendations,
    inputs=["params:target_column", "dataframe"],
    outputs="dataframe_with_recs"
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        build_recommendations_node
    ])
