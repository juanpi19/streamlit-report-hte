import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="Causal Inference Report", layout="wide")

st.title("📊 From Average to Individual Treatment Effects")

st.markdown("""
This report explores how causal inference can be used to optimize business decisions, specifically around discount strategies. Instead of estimating average effects, we dive into **Conditional Average Treatment Effects (CATE)** to understand **who** should receive a discount.
            
Instead of asking **"What’s the overall impact of a discount?"**, we ask **"Who should receive a discount?"**

We use **T-learners** to model both potential outcomes:
- `Y(1)`: Units sold **with** a discount  
- `Y(0)`: Units sold **without** a discount

Since only one of these outcomes is observed per customer, we train two models:

- `t₀ = f(Y | X, t = 0)`  
- `t₁ = f(Y | X, t = 1)`

We then estimate the treatment effect for each customer:


`CATE(X) = t₀(X) - t(X)`

To make this interpretable, we compute the **relative lift**:

`Relative Lift = CATE / Baseline Demand`

This tells us the percentage increase in units sold if a discount is offered.
""")

st.header("📈 Distribution of Price Elasticity (Relative-Lift Index)")

# Load and display the image
image_path = "rel-lift.png"
image = Image.open(image_path)
st.image(image, caption="Distribution of Relative Lift across Customers")

st.markdown("""
Customers to the **right** of the red line (0) are positively influenced by a discount — they're more likely to purchase more.

Customers to the **left** of the line might actually reduce demand or show no change when offered a discount.

Understanding this distribution helps in **personalizing discount strategies** — targeting customers who are most likely to respond positively.
""")

st.header("Learn More")
st.markdown("""
- Full discount analysis: [tinyurl.com/bdfua2ww](https://tinyurl.com/bdfua2ww)  
- Causal Inference Handbook (free): [Matheus Facure](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)
""")