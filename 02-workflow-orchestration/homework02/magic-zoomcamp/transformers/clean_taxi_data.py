if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    indices = data['passenger_count']>0
    num_rows_zero_passengers = data['passenger_count'].eq(0).sum()
    print("Num rows with zero passengers:", num_rows_zero_passengers)
    return data[indices]

    return data


@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].eq(0).sum() == 0, 'There are rows with zero passengers'