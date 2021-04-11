import folium
from folium.plugins import MarkerCluster
import branca.colormap as cm


class MapVisualization:
    """
    This class takes a crawled daft dataset which consists of 
    price, longitute, latitude, number of bedrooms, number of bathrooms
    with price in asending order then generate a folium map object"""

    def __init__(self, dataset):
        self.df = dataset
        self.map = self.create_map()
        self.color_names = [
            "darkblue",
            "blue",
            "lightblue",
            "orange",
            "lightred",
            "red",
            "darkred",
        ]  # 7 types of color
        self.color_codes = [
            "#0065a1",
            "#36a6d8",
            "#86d9ff",
            "#f1932e",
            "#ff8a7a",
            "#ca3c2a",
            "#9f3236",
        ]
        self.index = self.generate_color_bins()

    def generate_color_bins(self):
        """Generate color bins based on the price at 1%, 4%, 14% ... percentiles"""
        prices = self.df.monthly_price
        percentiles = [0.01, 0.04, 0.14, 0.30, 0.56, 0.70, 0.84, 1.00]
        return [prices.quantile(p) for p in percentiles]

    def create_map(self):
        """Creat the initial folium map with the location of the first record"""
        lat_of_first_record = self.df.iloc[0]["latitude"]
        lon_of_first_record = self.df.iloc[0]["longitude"]
        return folium.Map(
            location=[lat_of_first_record, lon_of_first_record],
            zoom_start=12,
            control_scale=True,
        )

    def color_dispatcher(self, price):
        for i in range(len(self.index) - 1):
            if price <= self.index[i + 1]:
                return self.color_names[i]

    def marker_icon(self, price):
        return folium.Icon(color=self.color_dispatcher(price))

    def add_markers(self):
        markers_dict = {}
        for index, row in self.df.iterrows():
            lat, lon, price = row["latitude"], row["longitude"], row["monthly_price"]
            beds, baths = row["bedrooms"], row["bathrooms"]
            popup_name = (
                "<p>"
                + "Bedrooms: "
                + str(beds)
                + "</p>"
                + "<p>"
                + "Bathrooms: "
                + str(baths)
                + "</p>"
            )
            popup_name += '<a href=" {0} "target="_blank"> link </a>'.format(
                row["daft_link"]
            )
            icon = self.marker_icon(price)
            marker = folium.Marker(
                [lat, lon], popup=popup_name, tooltip=price, icon=icon
            )
            if (lat,lon) in markers_dict.keys():
                markers_dict[(lat,lon)].append(marker)
            else:
                markers_dict[(lat,lon)] = [marker]

        for key, item in markers_dict.items():
            if len(item) == 1:
                item[0].add_to(self.map)
            else:
                marker_cluster = MarkerCluster().add_to(self.map)
                for i in range(len(item)):
                    item[i].add_to(marker_cluster)

    def add_colorbar(self):
        """add a colorbar at the top right corner of the map"""
        vmin, vmax = self.df["monthly_price"].quantile(0.005), self.df["monthly_price"].max()
        # set vmin to price.min() will screw the colorbar scale
        colormap = cm.StepColormap(
            self.color_codes, index=self.index, vmin=vmin, vmax=vmax
        )
        colormap.caption = "Monthly rent (‎€)"
        self.map.add_child(colormap)

    def save(self, file):
        self.map.save(file)