import streamlit as st
from PIL import Image, ImageDraw
import pandas as pd

# Function to create a new dataframe with default values
def create_dataframe():
    df = pd.DataFrame(columns=['x', 'y', 'shot_type'])
    return df

# Initialize dataframe and image variables
df = create_dataframe()
image = None
duplicate_image = None
clicked = False
click_coordinates = ()
shot_type = ''
filtered_df = df  # Initialize filtered dataframe with all data by default

# Function to draw circles on the duplicate image based on shot type and coordinates
def draw_circles(draw, x, y, shot_type):
    colors = {'raak': 'green', 'mis': 'red', 'redding': 'orange', 'block': 'yellow', 'eigen doelpunt': 'blue'}
    color = colors.get(shot_type, 'black')  # Default to black if shot type is not found in the dictionary
    