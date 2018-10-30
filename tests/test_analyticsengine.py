from pytest import fixture
from .context import DataFrame

@fixture
def analyticsengine():
    from .context import AnalyticsEngine
    return AnalyticsEngine

def test_top_values(analyticsengine):
    data = [
        ["CERTIFIED","SOFTWARE"],
        ["CERTIFIED","DOCTOR"],
        ["CERTIFIED","DOCTOR"],
        ["CERTIFIED","DERMATOLOGIST"],
        ["CERTIFIED","DERMATOLOGIST"],
    ]
    columns = ["CASE_STATUS","SOC_NAME"]
    df = DataFrame(data, columns)
    feature, counts = analyticsengine.top_values(df, 'SOC_NAME')
    assert feature == ["DERMATOLOGIST","DOCTOR","SOFTWARE"]
    assert counts == [2,2,1]

def test_topk_stats(analyticsengine):
    data = [
        ["CERTIFIED","SOFTWARE"],
        ["CERTIFIED","DOCTOR"],
        ["CERTIFIED","DOCTOR"],
        ["CERTIFIED","DERMATOLOGIST"],
        ["CERTIFIED","DERMATOLOGIST"],
    ]
    columns = ["CASE_STATUS","SOC_NAME"]
    df = DataFrame(data, columns)
    res = analyticsengine.topk_stats(df, 'SOC_NAME')
    assert res == [["DERMATOLOGIST",2,'40.0%'],
                   ["DOCTOR",2,'40.0%'],
                   ["SOFTWARE",1,'20.0%']]
