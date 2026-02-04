prices = [29.99, 45.50, 12.75, 38.20]


for percentages in range(len(prices)):
    if percentages == 0:
        factor = 0.9
    elif percentages == 1: 
        factor = 0.80 
    elif percentages == 2:
        factor = 0.85 
    elif percentages == 3:
        factor = 0.95

    prices[percentages] *= factor
    print(f"Updated price for item {percentages}: ${prices[percentages]:.2f}")
