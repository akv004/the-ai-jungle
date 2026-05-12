import numpy as np
import matplotlib.pyplot as plt
import datetime

# Set random seed
np.random.seed(42)

# Generate synthetic history
t_hist = np.arange(1, 100)
history = 50 + 0.2 * t_hist + 5 * np.sin(2 * np.pi * t_hist / 20) + np.random.normal(0, 2, size=len(t_hist))

# Generate forecast
t_future = np.arange(100, 140)
forecast_mean = 50 + 0.2 * t_future + 5 * np.sin(2 * np.pi * t_future / 20)
# Expanding confidence intervals
std_dev = np.linspace(2, 12, len(t_future))
lower_80 = forecast_mean - 1.28 * std_dev
upper_80 = forecast_mean + 1.28 * std_dev
lower_95 = forecast_mean - 1.96 * std_dev
upper_95 = forecast_mean + 1.96 * std_dev

# Dates
dates_hist = [datetime.date(2024, 1, 1) + datetime.timedelta(days=int(i)) for i in range(len(t_hist))]
dates_future = [datetime.date(2024, 1, 1) + datetime.timedelta(days=int(i)) for i in range(len(t_hist), len(t_hist) + len(t_future))]

plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(10, 5))

# Plot history
ax.plot(dates_hist, history, color='#2c3e50', linewidth=2, label='Observed History')

# Plot forecast
ax.plot(dates_future, forecast_mean, color='#e74c3c', linewidth=2, linestyle='--', label='ARIMA Forecast Mean')

# Plot confidence intervals
ax.fill_between(dates_future, lower_95, upper_95, color='#e74c3c', alpha=0.15, label='95% Confidence Interval')
ax.fill_between(dates_future, lower_80, upper_80, color='#e74c3c', alpha=0.3, label='80% Confidence Interval')

ax.set_title("Technical View: ARIMA Forecast with Confidence Intervals", fontweight='bold', pad=15)
ax.set_ylabel("Value", fontweight='bold')
ax.legend(loc='upper left')

# Highlight the point of forecast
ax.axvline(dates_hist[-1], color='black', linestyle=':', alpha=0.5)
ax.text(dates_hist[-1], 45, ' Forecast Origin', verticalalignment='bottom')

plt.tight_layout()
plt.savefig('images/chapter_timeseries_images/arima_technical_plot.png', dpi=300, bbox_inches='tight')
print("Successfully generated ARIMA technical plot")
