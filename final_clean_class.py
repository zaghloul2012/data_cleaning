import pandas as pd

class clean():
    """
    Clean dataset to fix or remove incorrect, corrupted, incorrectly formatted,
    duplicate, or incomplete data within a dataset.
    Also it aims to categorize some features to produce clean dataset used in movie reccommendation system model. 
    """
    
    def __init__(self, data_path):
        """
        Clean class constructor 

        Parameters
        ----------
        data_path : list
            path of dataset scrapped from imdb to be cleaned.

        Returns
        -------
        None.

        """
        self.data_path = data_path
        self.df = pd.DataFrame(data_path)

    def categorize_rating(self, rating):
        """
        Categorize rating into three groups where:
        low: rating <= 5
        medium: rating <= 7
        high: else

        Parameters
        ----------
        rating : int
            rating of movie or series.

        Returns
        -------
        str
            rating group(low - medium - high).

        """

        if rating <= 5:
            return "low"
        elif rating <= 7:
            return "medium"
        else:
            return "high"

    def convert_raters_to_numbers(self, raters):
        """
        Convert number of raters from compact short format
        into numeric format(10k -> 10000)

        Parameters
        ----------
        raters : str
            number of raters in compact short format(10k).

        Returns
        -------
        int
            number of raters in numeric format(10000).

        """
        if (raters.lower()[-1] == "k"):
            return int(float(raters[:-1])*1e3)

        elif(raters.lower()[-1] == "m"):
            return int(float(raters[:-1])*1e6)
        
        else:   # number of raters already in numeric format
            return int(raters)

    def convert_list_to_string(self,lst):
        """
        Convert list of strings into compact lowered format of strings
        The purpose of that function is to use these string in the model 
        to compute cosine similarity.
        One use of this function is to convert list of directors of movies 
        into string 

        Parameters
        ----------
        lst : list
            list of strings.

        Returns
        -------
        str
            compact format of string.

        """
        names = ""

        for person in lst:
            names += "".join(person.lower().split())
            names += " "    #separate differnet persons

        return names

    def categorize_length(self, length):
        """
        Convert length(movie-series) from short compact format into numeric format(1h -> 60)
        Categorize length(movie-series episode) into three groups

        Parameters
        ----------
        length : str
            compact format of (movie-series episode) length.

        Returns
        -------
        str
            length group(short-medium-long).

        """

        # Error handling 
        if length == "" or length == None or "-" in length:
            return ""

        length = length.split(" ")
        length_in_minutes = 0
        for time in length:
            if (time[-1] == "m"):
                length_in_minutes += int(time[:-1])
            elif (time[-1] == "h"):
                length_in_minutes += int(time[:-1]) * 60

        # Categorizing
        if length_in_minutes <= 90:
            return "short"

        elif length_in_minutes <= 150:
            return "medium"

        else:
            return "long"

    def categorize_year(self, year):
        """
        Categorize publish time of movie into two groups.
        old: year < 2014
        new: else

        Parameters
        ----------
        year : int
            Publish time of movie-series.

        Returns
        -------
        str
            Publish group(old-new).

        """
        year = int(year)        
        if(year < 2014):
            return "old"
        else:
            return "new"

    def is_series(self, title):
        """
        Define if title is series or movie

        Parameters
        ----------
        title : str
            Title of movie or series.

        Returns
        -------
        str
            Type of title(movie-series).

        """
        if title:
            return "series"
        else:
            return "movie"
    
    def clean_and_categorize(self):
        """
        Apply all functions to the dataset to provide features used in model
        by adding new key called "features"

        Returns
        -------
        None.

        """
        
        # Categorize rating
        self.df['rating'] = self.df['rating'].apply(self.categorize_rating)
        
        # Truncate movies with number of raters less than 10k
        self.df['new_raters'] = self.df['number'].apply(self.convert_raters_to_numbers)
        self.df = self.df[self.df['new_raters'] > 1e5]
        self.df = self.df.drop(columns=['new_raters', "number"], axis=1)

        # Categorize movie/series
        self.df['series'] = self.df['series'].apply(self.is_series)

        # Convert genres to string
        self.df['genres'] = self.df['genres'].apply(self.convert_list_to_string)

        # Convert writers to string
        self.df['writers'] = self.df['writers'].apply(self.convert_list_to_string)

        # Convert directors to string
        self.df['directors'] = self.df['directors'].apply(self.convert_list_to_string)

        # Convert cast to string
        self.df['cast'] = self.df['cast'].apply(self.convert_list_to_string)

        # Convert languages to string
        self.df['languages'] = self.df['languages'].apply(self.convert_list_to_string)

        # Categorize length
        self.df['length'] = self.df['length'].apply(self.categorize_length)

        # Categorize year
        self.df['year'] = self.df['year'].apply(self.categorize_year)

        # drop the axis column
        columns = self.df.columns[1:]

        # Construcing features 
        for column in columns:
            if column == "poster":
                continue
            self.df["features"] += self.df[column] + " "
        
        
    def save_to_dict(self):
        """
        Save data into dictinary so that it can be handled in database

        Parameters
        ----------
        out : dict
            Dictionary of data .

        Returns
        -------
        None.

        """
        self.out = self.df.to_dict("records")
        return self.out






