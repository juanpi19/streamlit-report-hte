# 📊 Streamlit Report: Heterogeneous Treatment Effects

A Streamlit application that demonstrates how causal inference can be used to optimize business decisions through personalized discount strategies. Instead of focusing on average treatment effects, this app explores **Conditional Average Treatment Effects (CATE)** to understand which customers should receive discounts.

## 🎯 Purpose

This application answers the question: **"Who should receive a discount?"** rather than **"What's the overall impact of a discount?"**

The app demonstrates:
- How to move from average effects to individual treatment effects
- Implementation of T-learners for causal inference
- Visualization of price elasticity distribution across customers
- Practical application of heterogeneous treatment effects in business

## 🔬 Methodology

The application uses **T-learners** to model potential outcomes:

- `Y(1)`: Units sold **with** a discount  
- `Y(0)`: Units sold **without** a discount

Two separate models are trained:
- `t₀ = f(Y | X, t = 0)`  
- `t₁ = f(Y | X, t = 1)`

The treatment effect for each customer is estimated as:
```
CATE(X) = t₁(X) - t₀(X)
```

To make results interpretable, relative lift is computed:
```
Relative Lift = CATE / Baseline Demand
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/juanpi19/streamlit-report-hte.git
cd streamlit-report-hte
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
streamlit-report-hte/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── rel-lift.png       # Distribution visualization
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 📊 Features

- **Interactive Report**: Clean, professional presentation of causal inference concepts
- **Visual Analysis**: Distribution chart showing relative lift across customers
- **Educational Content**: Clear explanations of T-learners and CATE methodology
- **Business Context**: Real-world application to discount optimization
- **Resource Links**: Additional learning materials and full analysis

## 🎨 Key Visualizations

The app includes a distribution chart showing the **Relative Lift Index** across customers:
- Customers to the **right** of zero are positively influenced by discounts
- Customers to the **left** may reduce demand or show no change when offered discounts
- This enables **personalized discount strategies**

## 📚 Learning Resources

The app provides links to:
- Full discount analysis
- Causal Inference Handbook by Matheus Facure

## 🛠️ Built With

- **Streamlit** - Web app framework
- **Matplotlib & Seaborn** - Data visualization
- **Pandas & NumPy** - Data manipulation
- **Pillow** - Image processing

## 📈 Use Cases

This application is useful for:
- Data scientists learning causal inference
- Business analysts optimizing marketing strategies
- Students studying heterogeneous treatment effects
- Anyone interested in personalized business decisions

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional features.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Streamlit and causal inference principles*
