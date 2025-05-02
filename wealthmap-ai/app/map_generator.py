import folium
import pandas as pd
import os

# Load data
csv_path = os.path.join(os.path.dirname(__file__), '../data/city_wealth_migration.csv')
df = pd.read_csv(csv_path)

# Create map centered at global view
wealth_map = folium.Map(location=[20, 0], zoom_start=2)

# Add circles for each city
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=max(abs(row['net_migration']) / 300, 5),
        popup=f"{row['city']}: Net Migration {row['net_migration']}",
        color='green' if row['net_migration'] > 0 else 'red',
        fill=True,
        fill_opacity=0.7,
        fill_color='green' if row['net_migration'] > 0 else 'red'
    ).add_to(wealth_map)

# Save to output
output_path = os.path.join(os.path.dirname(__file__), '../output/wealth_migration_map.html')
wealth_map.save(output_path)
print(f"Map saved to {output_path}")
