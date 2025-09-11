#!/usr/bin/env python3
"""
AI Lab - Getting Started Example
Course: 2025-2 Artificial Intelligence

This is a basic example to verify your Python AI environment is set up correctly.
"""

import sys
print("Python version:", sys.version)

try:
    import numpy as np
    print("✓ NumPy:", np.__version__)
except ImportError:
    print("✗ NumPy not installed")

try:
    import pandas as pd
    print("✓ Pandas:", pd.__version__)
except ImportError:
    print("✗ Pandas not installed")

try:
    import matplotlib
    print("✓ Matplotlib:", matplotlib.__version__)
except ImportError:
    print("✗ Matplotlib not installed")

try:
    import sklearn
    print("✓ Scikit-learn:", sklearn.__version__)
except ImportError:
    print("✗ Scikit-learn not installed")

print("\nEnvironment check complete!")

# Simple AI example - Linear regression with synthetic data
try:
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2 * X.ravel() + 3 + np.random.randn(100) * 2
    
    # Create and train model
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    # Calculate metrics
    mse = mean_squared_error(y, y_pred)
    print(f"\nSimple Linear Regression Example:")
    print(f"Coefficient: {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")
    
    print("\n🎉 AI environment setup successful!")
    
except ImportError as e:
    print(f"\n⚠️  Some libraries missing: {e}")
    print("Please install requirements: pip install -r requirements.txt")

if __name__ == "__main__":
    pass