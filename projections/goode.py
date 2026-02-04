import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import sys
import cartopy.feature as cfeature
import geopandas as gpd
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
###
# Load the Natural Earth shapefile for countries
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#https://www.naturalearthdata.com/downloads/50m-cultural-vectors/
world = gpd.read_file('ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')

# List of countries to color
countries_to_color = ['Switzerland', 'Germany', 'France', 'Italy', 'Austria', 'Indonesia', 'Hungary', 'Poland','Mexico','Portugal','Belgium','Czech Republic']
#'Australia',
# Filter the dataframe to include only the countries of interest
countries = world[world['NAME'].isin(countries_to_color)]
#
states_to_world = ['North Carolina', 'South Carolina', 'Massachusetts', 'Colorado', 'Georgia', 'Tennessee', 'Nevada','Delaware','New Jersey',\
'West Virginia', 'Virginia', 'New York', 'Kentucky', 'Oregon', 'California', 'Illinois', 'Minnesota', 'Washington','Ohio','DC','Arizona','Louisiana',\
'New South Wales','Victoria','South Australia','Northern Territory','Western Australia','Queensland','Tasmania']

states_to_color_ind=['Chandigarh','Delhi','Himachal Pradesh','Haryana','Jammu and Kashmir','Andhra Pradesh','Kerala','Karnataka',\
'Punjab','Rajasthan','Uttar Pradesh','Uttarakhand','West Bengal','Madhya Pradesh','Puducherry','Tamil Nadu','Gujarat','Maharashtra']
# states_india=[]
# us_states = gpd.read_file('data/usa-states-census-2014.shp')
us_states = gpd.read_file('ne_50m_admin_1_states_provinces/ne_50m_admin_1_states_provinces.shp')
list_ind_states=[]
for idx, row in us_states.iterrows():
    if row['sov_a3'] == 'IND':
        list_ind_states.append(row['name'])
#print(us_states.columns.tolist())
states_to_color=states_to_world+states_to_color_ind
states = us_states[us_states['name'].isin(states_to_color)]
states_ind = us_states[us_states['name'].isin(list_ind_states)]

###
# cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
cities = gpd.read_file('ne_10m_populated_places_simple/ne_10m_populated_places_simple.shp')

# for idx, row in cities.iterrows():
#     if row['sov0name'] == 'Australia':
        # print(row['name'])
        # list_ind_states.append(row['name'])

cities_oz=['Sydney','Perth','Hobart','Melbourne','Alice Springs','Adelaide','Canberra','Brisbane','Wollongong','Darwin','Cairns','Wagga Wagga','Tumut','Merimbula',
'Albury','Mildura','Narrabri','Orange','Eden','Mackay','Townsville','Rockhampton','Sunshine Coast','Bundaberg','Coffs Harbour','Horsham','Cooma','Nowra','Ulladulla','Batemans Bay',\
'Davenport','Katherine','Yulara','Warrnambool','Gold Coast','Bendigo','Launceston','Bowen','Moree','Tennant Creek','Hervey Bay','Sunshine Coast']
cities_india=['Indore','Bhopal','Srinagar','Pune','New Delhi','Bengaluru','Kolkata','Kochi','Kanpur','Agra','Lucknow','Jaipur','Bhusawal',\
'Jodhpur','Jaisalmer','Nagpur','Coimbatore','Puducherry','Munnar','Dehradun','Nagercoil','Ahmedabad','Mysuru','Mangaluru','Jammu','Gandhinagar']
cities_europe=['Vienna','Budapest','Bonn','Cologne','Interlaken','Bern','Basel','Milan','Geneva','Berlin','Warsaw','Chamonix',\
'Metzeral','Bolzano','Brussels','Krakow','Lisbon']
cities_us=['Boulder', 'New York','Bend','Atlanta','Los Angeles','Minneapolis','Chicago','Medford',\
'Myrtle Beach','Boston','Mt Shasta','Furnace Creek','Asheville','Huntington','Lexington','Great Barrington',\
'Mt Airy','Phoenix','Flagstaff','New Orleans']
cities_misc=['Singapore','Denpasar','Yogyakarta','Malang','Jember','Monterrey']
cities_to_plot = cities_oz+cities_india+cities_europe+cities_us+cities_misc
# cities_filtered = cities[cities['name'].isin(cities_us)]
cities_filtered = cities[cities.apply(lambda row: row['name'] in cities_to_plot and (
    (row['sov0name'] == 'Australia' and row['name'] in cities_oz) or
    (row['sov0name'] == 'India' and row['name'] in cities_india) or
    (row['sov0name'] in ['Austria', 'Hungary', 'Germany', 'Switzerland', 'Italy', 'Poland','Belgium','Portugal'] and row['name'] in cities_europe) or
    (row['sov0name'] == 'United States' and row['name'] in cities_us) or
    (row['sov0name'] in ['Singapore', 'Indonesia','Mexico'] and row['name'] in cities_misc)
), axis=1)]
########################################

plt.ion()
# Create a figure and axis with Goode Homolosine projection
fig, ax = plt.subplots(figsize=(15, 12),subplot_kw={'projection': ccrs.InterruptedGoodeHomolosine()})
ax.add_feature(cfeature.COASTLINE, linewidth=.64,edgecolor='xkcd:fern green')
# ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.85, edgecolor='xkcd:white',scale='50m')#
ax.add_feature(cfeature.NaturalEarthFeature(category='cultural', name='admin_0_boundary_lines_land',\
 scale='50m', facecolor='none'), linestyle='-', linewidth=0.85, edgecolor='xkcd:white')
ax.add_feature(cfeature.LAND, facecolor='xkcd:dark sea green', alpha=0.45)
ax.add_feature(cfeature.OCEAN, facecolor='xkcd:dull blue', alpha=0.75)

lakes = cfeature.NaturalEarthFeature('physical', 'lakes', '50m', facecolor='xkcd:ice', alpha=0.9)
ax.add_feature(lakes)
# countries
for country in countries.geometry:
    ax.add_feature(ShapelyFeature([country], ccrs.PlateCarree(), facecolor='xkcd:white', \
    edgecolor='xkcd:deep lilac', linewidth=0.5, alpha=0.85))

for state in states.geometry:
    ax.add_feature(ShapelyFeature([state], ccrs.PlateCarree(), facecolor='xkcd:white', edgecolor='xkcd:deep lilac',
     linewidth=0.25, alpha=0.85))

for state in states_ind.geometry:
    ax.add_feature(ShapelyFeature([state], ccrs.PlateCarree(), facecolor='none', edgecolor='xkcd:deep lilac',
     linewidth=0.25, alpha=0.85))

# for idx, row in cities_filtered.iterrows():
#     city_feature = ShapelyFeature([row.geometry], ccrs.PlateCarree(), facecolor='grey', edgecolor='xkcd:dark cream')
#     ax.add_feature(city_feature,linewidth=0.25, alpha=0.5)

# Plot the cities as small circles
for idx, row in cities_filtered.iterrows():
    ax.plot(row.geometry.x, row.geometry.y, 'o', markeredgecolor='xkcd:black',color='xkcd:light burgundy',markeredgewidth=.2, markersize=3, \
    transform=ccrs.PlateCarree(),alpha=.75)
# ##
ax.plot(0, 89, 'o', markeredgecolor='xkcd:black',color='xkcd:white',markeredgewidth=.1, markersize=1, \
transform=ccrs.PlateCarree(),alpha=.8)
ax.plot(175, -89, 'o', markeredgecolor='xkcd:black',color='xkcd:white',markeredgewidth=.1, markersize=1, \
transform=ccrs.PlateCarree(),alpha=.8)
ax.plot(175, 0, 'o', markeredgecolor='xkcd:black',color='xkcd:white',markeredgewidth=.1, markersize=1, \
transform=ccrs.PlateCarree(),alpha=.8)
ax.plot(-175, 0, 'o', markeredgecolor='xkcd:black',color='xkcd:white',markeredgewidth=.1, markersize=1, \
transform=ccrs.PlateCarree(),alpha=.8)
# dull blue, ocean blue,
# Draw map boundary
# plt.title('Places ')
plt.tight_layout()
plt.show()

sys.exit()
plt.savefig('Countries_w_city.png', dpi=800,bbox_inches='tight', pad_inches=0.1)
plt.savefig('Countries_new_.png', dpi=800,bbox_inches='tight', pad_inches=0.1)

# Create a new figure and axes
