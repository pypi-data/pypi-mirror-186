import argparse

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors


def get_indexed_anime(path_to_csv):
    df = pd.read_csv(path_to_csv)
    indexed_df = df.set_index("Rank")
    return indexed_df


def get_anime_recommendations(column, indexed_df):
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


def run_session_including_indexed_anime(
    path_to_csv="../data/01_raw/anime.csv",
    column="Tags",
):
    # Given multiple artifacts, we need to save each right after
    # its calculation to protect from any irrelevant downstream
    # mutations (e.g., inside other artifact calculations)
    import copy

    artifacts = dict()
    indexed_df = get_indexed_anime(path_to_csv)
    artifacts["indexed_anime"] = copy.deepcopy(indexed_df)
    final_df = get_anime_recommendations(column, indexed_df)
    artifacts["anime_recommendations"] = copy.deepcopy(final_df)
    return artifacts


def run_all_sessions(
    path_to_csv="../data/01_raw/anime.csv",
    column="Tags",
):
    artifacts = dict()
    artifacts.update(run_session_including_indexed_anime(path_to_csv, column))
    return artifacts


if __name__ == "__main__":
    # Edit this section to customize the behavior of artifacts
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_csv", type=str, default="../data/01_raw/anime.csv")
    parser.add_argument("--column", type=str, default="Tags")
    args = parser.parse_args()
    artifacts = run_all_sessions(
        path_to_csv=args.path_to_csv,
        column=args.column,
    )
    print(artifacts)
