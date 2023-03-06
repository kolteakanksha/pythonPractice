from os import listdir
from os.path import join
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


# open a file and return the contents
def load_file(filepath):
    # open the file
    with open(filepath, 'r') as handle:
        # return the contents
        return handle.read(), filepath


# load all files in a directory into memory
def main(path=r'C:\Users\pnema\OneDrive\Desktop\parts'):
    # prepare all of the paths
    paths = [join(path, filepath) for filepath in listdir(path)]
    # create the thread pool
    with ThreadPoolExecutor(10) as executor:
        # submit all tasks
        futures = [executor.submit(load_file, p) for p in paths]
        # process all results
        for future in as_completed(futures):
            # open the file and load the data
            data, filepath = future.result()
            # report progress
            print(f'.loaded {filepath}')
    print('Done')


# entry point
if __name__ == '__main__':
    main()