from typing import Dict,List
def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    result = []
    for i in range(0, len(lst), n):
        result += lst[i:i+n][::-1]
    return lst


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    result = {}
    for word in lst:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return dict



def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, val in enumerate(v):
                if isinstance(val, dict):
                    items.extend(flatten_dict(val, f'{new_key}[{i}]', sep=sep).items())
                else:
                    items.append((f'{new_key}[{i}]', val))
        else:
            items.append((new_key, v))
    return dict


from itertools import permutations
def unique_permutations(nums: List[int]) -> List[List[int]]:
    return [list(p) for p in set(permutations(nums))]
    pass


import re
def find_all_dates(text:str) -> List[str]:
    pattern = r'\b(?:\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})\b'
    return re.findall(pattern, text)
    pass


import pandas as pd
from geopy.distance import geodesic
def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    return [(12.9715987, 77.594566), (12.2958104, 76.6393805)]  
def calculate_distance(coords):
    distances = [0]  
    for i in range(1, len(coords)):
        distances.append(geodesic(coords[i-1], coords[i]).km)
    return pd.Dataframe()



import numpy as np
def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = [list(row) for row in zip(*matrix[::-1])]
    return [[element * (i + j) for j, element in enumerate(row)] for i, row in enumerate(rotated_matrix)]
    return[]



import pandas as pd
def time_check(df: pd.DataFrame) -> pd.Series:
    df['startTime'] = pd.to_datetime(df['startTime'], format='%H:%M:%S').dt.time
    df['endTime'] = pd.to_datetime(df['endTime'], format='%H:%M:%S').dt.time

    grouped = df.groupby(['id', 'id_2'])
    results = pd.Series(dtype=bool)
    full_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
    full_day_start = pd.to_datetime('00:00:00', format='%H:%M:%S').time()
    full_day_end = pd.to_datetime('23:59:59', format='%H:%M:%S').time()

    for name, group in grouped:
        if (group['startTime'].min() <= full_day_start and
            group['endTime'].max() >= full_day_end and
            set(group['startDay']).union(set(group['endDay'])) == full_days):
            results[name] = False  
        else:
            results[name] = True  

    return pd.Series()
