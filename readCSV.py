import os
import pandas as pd

class FileSettings(object):
    def __init__(self, file_name, row_size=100):
        self.file_name = file_name
        self.row_size = row_size


class FileSplitter(object):

    def __init__(self, file_settings):
        self.file_settings = file_settings

        if type(self.file_settings).__name__ != "FileSettings":
            raise Exception("Please pass correct instance ")

        self.df = pd.read_csv(self.file_settings.file_name,
                              chunksize=self.file_settings.row_size)

    def run(self, directory=r'C:\Users\pnema\OneDrive\Desktop\parts'):

        try:
            os.makedirs(directory)
        except Exception as e:
            pass

        counter = 0

        while True:
            try:
                file_name = "{}/{}_{}.csv".format(
                    directory, "chunks", counter
                )
                df = next(self.df).to_csv(file_name)
                counter = counter + 1
            except StopIteration:
                break
            except Exception as e:
                print("Error:", e)
                break

        return True


def main():
    helper = FileSplitter(FileSettings(
        file_name=r'C:\Users\pnema\OneDrive\Desktop\data.csv',
        row_size=10
    ))
    helper.run()


main()
