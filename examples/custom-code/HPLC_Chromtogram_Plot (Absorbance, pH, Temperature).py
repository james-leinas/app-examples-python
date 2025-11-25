from io import BytesIO
import pandas as pd
from typing import NamedTuple
import plotly.graph_objects as go

class IOData(NamedTuple):
    name: str
    data: BytesIO | pd.DataFrame | go.Figure

def custom_code(inputs: list[IOData], **kwargs) -> list[IOData]:
    df = inputs[0].data
    # Extract the relevant data series and convert them to floats
    absorbance_data = df['absorbance (mAU)'].astype(float) 
    retention_volume_data = df['retention volume (mL)'].astype(float)
    
    fig = go.Figure()

    # Add Absorbance Trace
    fig.add_trace(go.Scatter(
        x=df['retention volume (mL)'],
        y=df['absorbance (mAU)'],
        name="Absorbance (mAU)",
        line=dict(color='royalblue'),
        yaxis="y1"
    ))
    
    # Add other traces (pH, Conc. B)
    fig.add_trace(go.Scatter(
        x=df['retention volume (mL)'], y=df['pH (pH)'],
        name="pH", line=dict(color='crimson', dash='dash'), yaxis="y2"
    ))
    fig.add_trace(go.Scatter(
        x=df['retention volume (mL)'], y=df['temperature (degC)'],
        name="Temperature (degC)", line=dict(color='green', dash='dot'), yaxis="y3"
    ))

    # --- Layout Definition ---
    fig.update_layout(
        title_text="Chromatogram with Abs, pH, Temperature Traces",
        xaxis_title="Retention Volume (mL)",
        plot_bgcolor='white',
        legend_title="Traces",
        xaxis=dict(domain=[0.1, 0.88]),
        yaxis=dict(
            title="<b>Absorbance (mAU)</b>",
            tickfont=dict(color="royalblue"),
            color="royalblue"
        ),
        yaxis2=dict(
            title="<b>pH</b>",
            tickfont=dict(color="crimson"), color="crimson",
            anchor="x", overlaying="y", side="right"
        ),
        yaxis3=dict(
            title="<b>Temperature (degC)</b>",
            tickfont=dict(color="green"), color="green",
            anchor="free", overlaying="y", side="right", position=0.92
        ) 
    )
    
    
    return [IOData(name="Chromatogram_New", data=fig)]
