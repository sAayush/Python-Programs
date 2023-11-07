import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[(views['author_id'] == views['viewer_id'])]
    result = views[['article_id']]
    return result


data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
        [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
    {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})