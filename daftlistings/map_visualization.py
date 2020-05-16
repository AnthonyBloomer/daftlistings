import pandas as pd
import folium
import branca.colormap as cm


class MapVisualization:
    """
    This class takes a crawled daft dataset which consists of 
    price, longitute, latitude, number of bedrooms, number of bathrooms
    with price in asending order then generate a folium map object"""

    def __init__(self, dataset):
        self.df = dataset
        self.clean_up()
        self.map = self.create_map()
        self.color_names = ['darkblue','blue','lightblue','orange','lightred','red','darkred'] # 7 types of color
        self.color_codes = ['#0065a1', '#36a6d8','#86d9ff','#f1932e', '#ff8a7a','#ca3c2a','#9f3236']
        self.index = self.generate_color_bins()
        
    def clean_up(self):
        """Some rent are collected weekly. Convert them to monthly values"""
        df = self.df
        row_num = df.price.count()
        # check the first row
        if df.iloc[0].price * 4 < df.iloc[1].price:
            df.iloc[0, df.columns.get_loc('price')] *= 4.333
        # check the rest of the records
        for i in range(1, row_num):
            if df.iloc[i].price < df.iloc[i-1].price - 100:
                df.iloc[i, df.columns.get_loc('price')] *= 4.333
        self.df = df.astype({"price": int})

    def generate_color_bins(self):
        """Generate color bins based on the price at 1%, 4%, 14% ... percentiles"""
        prices = self.df.price
        percentiles = [0.01, 0.04, 0.14, 0.30, 0.56, 0.70, 0.84, 1.00]
        return [prices.quantile(p) for p in percentiles]

    def create_map(self):
        """Creat the initial folium map with the location of the first record"""
        lat_of_first_record = self.df.iloc[0]["latitude"]
        lon_of_first_record = self.df.iloc[0]["longitude"]
        return folium.Map(location=[lat_of_first_record, lon_of_first_record], 
                            zoom_start=12, control_scale=True)

    def color_dispatcher(self, price):
        for i in range(len(self.index)-1):
            if price <= self.index[i+1]:
                return self.color_names[i]

    def marker_icon(self, price):
        return folium.Icon(color=self.color_dispatcher(price))

    def add_markers(self):
        for index, row in self.df.iterrows():
            lat, lon, price = row['latitude'], row['longitude'], row['price']
            beds, baths = row['num_bedrooms'], row['num_bathrooms']
            popup_name = '<p>' + 'Bedrooms: ' + str(beds) + '</p>' + '<p>' + 'Bathrooms: ' + str(baths) + '</p>'
            popup_name += '<a href=" {0} "target="_blank"> link </a>'.format(row['daft_link'])
            icon = self.marker_icon(price)
            marker = folium.Marker([lat, lon], popup=popup_name, tooltip=price, icon=icon)
            marker.add_to(self.map)

    def add_colorbar(self):
        """add a colorbar at the top right corner of the map"""
        vmin, vmax = self.df['price'].quantile(0.005), self.df['price'].max()
        # set vmin to price.min() will screw the colorbar scale
        colormap = cm.StepColormap(self.color_codes, index=self.index, vmin=vmin, vmax=vmax)
        colormap.caption = 'Monthly rent (‎€)'
        self.map.add_child(colormap)

    def save(self, file):
        self.map.save(file)


