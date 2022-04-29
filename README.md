# Data Cleaning Script
python script for cleaning and categorizing data scrapped from IMDB to be used in a model for movie recommendation system

## Description
Short script for cleaning scrapped data from IMDB to use it later

Sample Input
{'poster':'p1','title': 'Vikings', 'rating': '8.5','number': '491K', 'directors': [], 'writers': [],'cast': ['Katheryn Winnick', 'Gustaf Skarsgård', 'Alexander Ludwig'], 'languages': ['English', 'Old English', 'Norse, Old', 'Latin', 'French', 'Arabic', 'Greek, Ancient (to 1453)', 'Russian'], 'genres': ['Action', 'Adventure', 'Drama'], 'age_group': 'TV-MA', 'series': True, 'length': '44m', 'year': '2013'}

Sample Output
{'poster': 'p1', 'title': 'Vikings', 'rating': 'high', 'directors': '', 'writers': '', 'cast': 'katherynwinnick gustafskarsgård alexanderludwig ', 'languages': 'english oldenglish norse,old latin french arabic greek,ancient(to1453) russian ', 'genres': 'action adventure drama ', 'age_group': 'TV-MA', 'series': 'series', 'length': 'short', 'year': 'old', 'features': 'Vikings high  katherynwinnick gustafskarsgård alexanderludwig english oldenglish norse,old latin french arabic greek,ancient(to1453) russian action adventure drama TV-MA series short old '}
 Note: This format is used for model of movie reccomendation system
 
