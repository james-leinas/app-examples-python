"""
Supported packages:

allotropy
numpy
openpyxl
pandas
plotly
pyarrow
pydantic
scikit-learn
scipy
statsmodels
"""
from io import BytesIO
import pandas as pd
from typing import NamedTuple
import plotly.graph_objects as go
import plotly.express as px

class IOData(NamedTuple):
    name: str
    data: BytesIO | pd.DataFrame | go.Figure

def custom_code(inputs: list[IOData], **kwargs) -> list[IOData]:
    pass