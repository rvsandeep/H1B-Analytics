from pytest import fixture

@fixture
def dataframe():
    from src.H1BDataFrame import DataFrame
    return DataFrame


#[TO-DO]
def test_read_csv(dataframe):
    assert True == True

#[TO-DO]
def test_get_header(dataframe):
    assert True == True

#[TO-DO]
def test_fiter(dataframe):
    assert True == True
