import numpy as np
import matplotlib.pyplot as plt
import datetime

# Set random seed
np.random.seed(42)

# Generate synthetic time series data
t = np.arange(1, 200)
trend = 0.05 * t + 0.001 * (t ** 2)
seasonal = 10 * np.sin(2 * np.pi * t / 24)
noise = np.random.normal(0, 2, size=len(t))
noise[150] += 30 # Outlier

observed = trend + seasonal + noise
dates = [datetime.date(2024, 1, 1) + datetime.timedelta(days=int(i)) for i in range(len(t))]

# Plot
plt.style.use('bmh') # robust style
fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

axes[0].plot(dates, observed, color='#2c3e50', linewidth=2)
axes[0].set_ylabel('Observed', fontweight='bold')
axes[0].set_title('Technical View: STL Decomposition with a Robustness Outlier', fontweight='bold', pad=15)

axes[1].plot(dates, trend, color='#e74c3c', linewidth=2)
axes[1].set_ylabel('Trend', fontweight='bold')

axes[2].plot(dates, seasonal, color='#3498db', linewidth=2)
axes[2].set_ylabel('Seasonal', fontweight='bold')

axes[3].scatter(dates, noise, color='#7f8c8d', s=15)
axes[3].axhline(0, color='black', linestyle='--', alpha=0.5)
axes[3].scatter(dates[150], noise[150], color='#e67e22', s=80, edgecolor='black', zorder=5, label='Outlier / Anomaly')
axes[3].set_ylabel('Residual', fontweight='bold')
axes[3].legend(loc='upper right')

plt.tight_layout()
plt.savefig('images/chapter_timeseries_images/stl_technical_plot.png', dpi=300, bbox_inches='tight')
print("Successfully generated STL technical plot")
