import datetime

from chalk.client import FeatureResult
from chalk.client.client_impl import OnlineQueryResponseWrapper
from chalk.features import features, has_one


@features
class User:
    id: str
    email: str


@features
class PlaidAccount:
    user_id: str
    user: User = has_one(lambda: PlaidAccount.user_id == User.id)
    bank_name: str


data = [
    FeatureResult(
        field="plaid_account.user.email",
        value="faker@gmail.com",
        error=None,
        ts=datetime.datetime(2022, 12, 29, 22, 31, 10, tzinfo=datetime.timezone.utc),
    ),
    FeatureResult(
        field="plaid_account.user.id",
        value="IuiTTRfsldkj0878650X6Kn9mjDE73",
        error=None,
        ts=datetime.datetime(2022, 12, 29, 22, 31, 10, tzinfo=datetime.timezone.utc),
    ),
    FeatureResult(
        field="plaid_account.bank_name",
        value="Wells Fargo",
        error=None,
        ts=datetime.datetime(2022, 12, 29, 22, 31, 10, tzinfo=datetime.timezone.utc),
    ),
]

data_response = OnlineQueryResponseWrapper(data=data, errors=[], warnings=[])

repr_result = """                      field  ...                        ts
0  plaid_account.user.email  ... 2022-12-29 22:31:10+00:00
1     plaid_account.user.id  ... 2022-12-29 22:31:10+00:00
2   plaid_account.bank_name  ... 2022-12-29 22:31:10+00:00

[3 rows x 4 columns]"""

html_result = """<div><stylescoped>.dataframetbodytrth:only-of-type{vertical-align:middle;}.dataframetbodytrth{vertical-align:top;}.dataframetheadth{text-align:right;}</style><tableborder="1"class="dataframe"><thead><trstyle="text-align:right;"><th></th><th>field</th><th>value</th><th>error</th><th>ts</th></tr></thead><tbody><tr><th>0</th><td>plaid_account.user.email</td><td>faker@gmail.com</td><td>None</td><td>2022-12-2922:31:10+00:00</td></tr><tr><th>1</th><td>plaid_account.user.id</td><td>IuiTTRfsldkj0878650X6Kn9mjDE73</td><td>None</td><td>2022-12-2922:31:10+00:00</td></tr><tr><th>2</th><td>plaid_account.bank_name</td><td>WellsFargo</td><td>None</td><td>2022-12-2922:31:10+00:00</td></tr></tbody></table></div>"""


class TestClientStringRepresentation:
    def test_OQRW_data_repr(self):
        assert "".join(repr_result.split()) == "".join(repr(data_response).split())

    def test_OQRW_data_repr_html(self):
        assert "".join(html_result.split()) == "".join(data_response._repr_html_().split())
