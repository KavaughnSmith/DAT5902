import numpy as np

def correlation_coefficient(df, col1, col2):
    x = df[col1]
    y = df[col2]

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator_x = np.sum((x - mean_x)**2)
    denominator_y = np.sum((y - mean_y)**2)

    correlation_coefficient = numerator / np.sqrt(denominator_x * denominator_y)

    return correlation_coefficient
