"""
Replicating the mushroom_model behavior
"""
import streamlit as st

import pandas as pd

from  mushroom_model import predict_mushroom


# # # Header # # #

st.header("Mushroom Classifier")


# what is noqa?
# https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html

st.markdown("""
Enter the properties of your mushroom below.
> Note: this model was trained on a generated database.
Do not use it to classify real mushrooms!
""")  # noqa w291

# # # Initial Observation State # # #
observation = {
    'cap-diameter': [50],
    'stem-height': [20],
    'stem-width': [30],
    'has-ring': ['t'],
    'cap-shape': ['c']
}


# # # User Input Widgets # # #

has_ring = st.checkbox("The mushroom has a ring")

cap_shape = st.selectbox(
    "Mushroom Cap Shape",
    options=[
        'conical', 'bell', 'convex', 'flat',
        'sunken', 'spherical', 'others']
)
cap_shape_map = {
    'conical': 'c',
    'bell': 'b',
    'convex': 'x',
    'flat': 'f',
    'sunken': 's',
    'spherical': 'p',
    'others': 'o'
}
cap_diameter = st.number_input(
    "Cap diameter (cm)",
    min_value=0.38,
    max_value=62.34,
    value=50.0,
    help="Cap diameter from 0.38 to 62.34 cm"
)

stem_height = st.number_input(
    "Stem height (cm)",
    min_value=0.00,
    max_value=33.92,
    value=20.0,
    help="Stem height from 0 to 33.92 cm"
)

stem_width = st.number_input(
    "Stem width (mm)",
    min_value=0.00,
    max_value=103.91,
    value=30.0,
    help="Stem width from 0 to 103.91 mm"
)

#Update Model Parameters
observation['has-ring'] = ['t'] if has_ring else ['f']
observation['cap-shape'] = [cap_shape_map[cap_shape]]
observation['cap-diameter'] = [cap_diameter]
observation['stem-height'] = [stem_height]
observation['stem-width'] = [stem_width]


# # # Prediction and Display # # #

single_obs_df = pd.DataFrame(observation)

# so far there's only one prediction so we'll index that prediction
current_prediction = predict_mushroom(single_obs_df)[0]


# note that these still print to the console
print(f"model results: {current_prediction}")
print(observation)

# Streamlit will happily take emojis
if current_prediction == 0:
    st.markdown("### 🍄🍄🍄 Mushroom is not poisonous")
else:
    st.markdown("### 🤢🤮💀 Mushroom is poisonous!")

st.markdown("""
> Note: this model was trained on a generated database.
Do not use it to classify real mushrooms!
""")  # noqa w291