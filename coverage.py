import matplotlib.pyplot as plt

# Years
years = ["Q4 2024", "Q4 2025", "Q4 2026", "Q4 2027", "Q4 2028", "Q4 2029", "Q4 2030"]

# CDMA 2G and EV-DO (3G) percentages from your dataset
cdma_2g_pct = [5.35, 2.00, 1.18, 1.01, 1.07, 0.94, 2.00]
cdma_evdo_pct = [45.19, 33.00, 25.74, 20.19, 15.53, 11.64, 8.00]

plt.figure(figsize=(10,6))
plt.plot(years, cdma_2g_pct, marker='o', label="CDMA 2G (%)")
plt.plot(years, cdma_evdo_pct, marker='o', label="CDMA EV-DO (3G) (%)")

# Optional annotation for LTE coverage (no exact data available)
plt.text(5.5, 10, "LTE coverage present but exact % unknown", color='green', fontsize=10)

plt.title("Yemen Mobile CDMA 2G and 3G Coverage Trends")
plt.xlabel("Year / Quarter")
plt.ylabel("Percentage of Connections (%)")
plt.ylim(0, 50)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
