import os

# define the root directory where the search will start
root = '/'

# define the search term that the user wants to find
search_term = input('Enter the search term: ')

# create a list to store the results of the search
results = []

# traverse the directory tree starting at the root directory
for dirpath, dirnames, filenames in os.walk(root):
    # iterate over the filenames in the current directory
    for filename in filenames:
        # check if the search term is in the filename
        if search_term in filename:
            # if the search term is found, add the file to the results list
            results.append(os.path.join(dirpath, filename))

# print the results of the search
print('Search results:')
for result in results:
    print(result)
