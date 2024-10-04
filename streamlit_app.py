import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Required title for the menu
        options=["Home", "Projects", "Contact"],  # Options to display in the menu
    )
  

