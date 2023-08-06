"""
This is a boilerplate pipeline 'build_recommendations_based_similar'
generated using Kedro 0.18.4
"""

from typing import List

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
from kedro.pipeline import node


def get_recommendations(column: str, indexed_df: pd.DataFrame) -> pd.DataFrame:
    def build_recommendations(
        rs_df: pd.DataFrame, column: str, rec_column_name: str = "recommendations"
    ) -> pd.DataFrame:
        """Строит рекомендации для каждой строки в Dataframe относительно выбранного столбца путём векторизации его
        текста и нахождения наиболее похожих строк по этому же векторизованному столбцу.
        Args:
            rs_df (pd.Dataframe):
            column (str): название столбца для построения на нём рекомендаций.
            rec_column_name (str, optional): название столбца, куда будут записаны рекомендации. Defaults to "recommendations".
        Returns:
            pd.Dataframe: Dataframe с сгенерированными рекомендациями в новом столбце.
        """
        target_column = rs_df.copy()[column].dropna()
        vectorizer = CountVectorizer(token_pattern=r"(?u)(\w[\w ]+)")
        vectors = vectorizer.fit_transform(target_column.tolist())
        nbrs = NearestNeighbors(n_neighbors=11).fit(vectors)
        _, indices = nbrs.kneighbors(vectors)
        recommendations = pd.Series(indices.tolist())
        recommendations.name = rec_column_name

        def fix_indices(indices: List[int]) -> List[int]:
            """Исправляет рекомендации, удаляя индекс того, кому эти рекомендации принадлежат
            (каждая рекомендация в строке ссылается на себя же).
            Args:
                indices (List[int]): список индексов-рекомендаций.
            Returns:
                List[int]: исправленный список индексов-рекомендаций.
            """
            return list(map(lambda idx: target_column.index[idx], indices))[1:]

        recommendations = recommendations.apply(fix_indices)
        recommendations.index = target_column.index
        final_df = rs_df.join(recommendations)
        return final_df

    final_df = build_recommendations(indexed_df, column=column)
    return final_df


build_recommendations_node = node(
    func=get_recommendations,
    inputs=["params:target_column", "dataframe"],
    outputs="dataframe_with_recs"
)
