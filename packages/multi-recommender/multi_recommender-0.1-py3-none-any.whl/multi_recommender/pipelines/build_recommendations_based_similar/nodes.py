"""
This is a boilerplate pipeline 'build_recommendations_based_similar'
generated using Kedro 0.18.4
"""

from typing import List

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
