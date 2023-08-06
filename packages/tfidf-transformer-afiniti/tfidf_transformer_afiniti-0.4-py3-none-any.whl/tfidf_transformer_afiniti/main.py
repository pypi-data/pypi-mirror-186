from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfFramework:
    """
    A class for performing tf-idf transformation using sklearn's TfidfVectorizer.
    """

    def __init__(self):
        """
        Initializes an empty list to hold the input strings, 
        an instance of TfidfVectorizer and an empty variable to hold tf-idf matrix
        """
        self.data = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def fit_transform(self):
        """
        Computes the tf-idf matrix
        """
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data)
    

    def append_list_data(self, new_data_list):
        """
        Append new list of data to the data list and update the tf-idf matrix
        
        Parameters:
        new_data_list (list): The new list of data to be appended.
        
        Raises:
        ValueError: If the provided data is not a list of non-empty strings.
        """
        
        if isinstance(new_data_list, list):
            for data in new_data_list:
                if not (isinstance(data, str) and len(data) > 0):
                    raise ValueError("Invalid data. All elements must be non-empty strings.")
            self.data.extend(new_data_list)
            self.fit_transform()
        else:
            raise ValueError("Invalid data. Must be a list of non-empty strings.")


    def append_data(self, new_data):
        """
        Append new data to the data list and update the tf-idf matrix
        
        Parameters:
        new_data (str): The new data to be appended. Must be a non-empty string.
        
        Raises:
        ValueError: If the provided data is not a non-empty string.
        """
        if not new_data:
            print("No new data provided.")
            raise ValueError("No new data provided.")
            
        
        # check if new_data is a list
        if not isinstance(new_data, str):
            print("New data must be provided in the form of a string.")
            raise ValueError("New data must be provided in the form of a string.")
            

        if isinstance(new_data, str) and len(new_data) > 0:
            self.data.append(new_data)
            self.fit_transform()
        else:
            raise ValueError("Invalid data. Must be a non-empty string.")

if __name__ == '__main__':
    
    framework = TfidfFramework()

    # Append some data to the data list
    data = ["This is the first document.", "This document is the second document.", "And this is the third one."]
    for d in data:
        framework.append_data(d)

    # Print the tf-idf matrix
    print(framework.tfidf_matrix.toarray())

    # Add new one
    new_data = "this is a new test document"
    framework.append_data(new_data)
    # Print the tf-idf matrix
    print(framework.tfidf_matrix.toarray())

    # Add new list
    new_list_data = ["And this is the realy fifth one.","And this is the finaly sixth one."]  
    framework.append_list_data(new_list_data)
    # Print the tf-idf matrix
    print(framework.tfidf_matrix.toarray())