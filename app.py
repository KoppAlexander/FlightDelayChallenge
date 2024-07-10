import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from io import BytesIO

# Set page config
st.set_page_config(page_title="Flight Delay Presentation", page_icon="images/flight.ico", layout="wide")

# Load and encode the image
image = Image.open("images/flight.png")
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Create inline HTML for image and text
inline_title = f"""
<div style="display: flex; align-items: center; white-space: nowrap;">
    <span style="font-size: 2em; font-weight: bold;">Flight Delay</span>
    <img src="data:image/png;base64,{img_str}" style="height: 3em; margin-left: 10px;">
</div>
"""

# Display the inline title
st.write(inline_title, unsafe_allow_html=True)

# Sidebar for navigation
page = st.sidebar.radio("Overview", ["Case Study", "Data", "Analysis", "Model", "Precision"])

# Introduction page
if page == "Case Study":
    st.header("Case Study")
    st.write("Flight delays are a significant concern in the aviation industry, affecting passenger satisfaction, airline operations, and overall transportation efficiency. This dataset focuses on flight delays experienced by Tunisian airlines, providing valuable insights into the patterns and causes of delays in the North African aviation sector.")
    
    st.subheader("Features")
    st.write("- Departure & Destination")
    st.write("- Time data")
    st.write("- Flight ID & Plane ID")

    st.subheader("Target")
    st.write("- Delay")

# Data Analysis page
elif page == "Data":
    st.header("Data")

    # Load data
    @st.cache_data
    def load_data():
        return pd.read_csv("data/Train.csv")

    df = load_data()

    st.subheader("DataFrame")
    st.write(df.head())

    def load_data():
        return pd.read_csv("data/data.csv")

    df = load_data()

    st.subheader("Distribution of Airports")

    # Create the scatter plot
    fig = px.scatter_mapbox(df, lat="latitude_arr", lon="longitude_arr", 
                            color_discrete_sequence=["teal"], zoom=2)

    # Custom mapbox style with opacity
    mapbox_style = {
        "version": 8,
        "sources": {
            "osm": {
                "type": "raster",
                "tiles": ["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
                "tileSize": 256,
                "attribution": "&copy; OpenStreetMap Contributors",
                "maxzoom": 19
            }
        },
        "layers": [{
            "id": "osm",
            "type": "raster",
            "source": "osm",
            "paint": {"raster-opacity": 0.8}  # Set the opacity here
        }]
    }

    # Update layout with custom mapbox style
    fig.update_layout(mapbox_style=mapbox_style)

    # Update layout for size and title
    fig.update_layout(
        height=600,  # Adjust height as needed
        title={
            'text': "Distribution of Airports",
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Optional: Add a data table below the map
    if st.checkbox("Show raw data"):
        st.write(df)

# Other pages
elif page == "Analysis":
    st.header("Analysis")
    # Add your analysis content here

elif page == "Model":
    st.header("Model")
    # Add your model content here

elif page == "Precision":
    st.header("Precision")
    # Add your precision content here

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Done by [Alexander Kopp](https://github.com/KoppAlexander), [Simon Bernarding](https://www.linkedin.com/in/simon-bernarding/) & [Michel Penke](https://michelpenke.de/portfolio/)")