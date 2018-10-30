from pytest import fixture
from .context import DataFrame

@fixture
def transformer():
    from .context import DataTransformer
    return DataTransformer


def test_standardize_col_names(transformer):
    data = [[1,2,3]]
    columns = ['Approval_Status','bed','cdf']

    df = DataFrame(data, columns)
    new_df = transformer.standardize_col_names(df)
    assert new_df.get_header() == ['CASE_STATUS','bed','cdf']
