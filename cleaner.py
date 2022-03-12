import pandas as pd

class Cleaner:
    '''
    The class is defined to make the data clearning process more clearer to the reader
    '''
    def __init__(self, file):
        '''
        initializing the instance by reading the data file
        Args:
            file: a csv data file.
        Return:
            None.
        '''
        self.df = pd.read_csv(file)

    def keepColumns(self, columns):
        '''
        keep the given columns
        Args:
            columns: an array of strings.
        Return:
            None.
        '''
        self.df = self.df[columns]

    def changeName(self, oldName, newName):
        '''
        change the name of given columns
        Args:
            oldName: an array of strings.
            newName: an array of strings.
        Return:
            None.
        '''
        for i in range(len(oldName)):
            self.df = self.df.rename(columns={oldName[i]: newName[i]})
        
    def dropNA(self):
        '''
        drop NA values
        '''
        self.df = self.df.dropna()
        
    def cleanPlayerName(self):
        '''
        clean the players' names by getting rid of useless characters
        '''
        self.df["Player"] = self.df["Player"].str.split("\\").str.get(0)
    
    def cleanSalary(self):
        '''
        clean the salary column by getting rid of the dollar sign and change the variable type
        '''
        if any(self.df["Salary"].isna()):
            raise TypeError("There is null value in the dataset")
        else:
            self.df["Salary"] = self.df["Salary"].str.split("\$").str.get(1)
            self.df['Salary'] = self.df["Salary"].replace(',','', regex=True)
            self.df['Salary'] = self.df["Salary"].astype("float64")
    
    def getSeason(self, season):
        '''
        drop useless seasons
        Args:
            season: a string.
        Return:
            None
        '''
        self.df = self.df[self.df["season"] == season]

    def unique(self, column):
        '''
        drop the duplicates in a given column
        Args:
            column: a string.
        Return:
            None.
        '''
        self.df = self.df.drop_duplicates(subset = [column])

    def merge(self, other):
        '''
        merge two Cleaner instances and return a dataframe
        Args:
            other: a Cleaner instance
        Return:
            A dataframe merged by the dataframes of self and other
        '''
        if not (self.df["Player"].is_unique and other.df["Player"].is_unique):
            raise ValueError("The Player column is not unique")
        else:
            return pd.merge(self.df, other.df, on = "Player")