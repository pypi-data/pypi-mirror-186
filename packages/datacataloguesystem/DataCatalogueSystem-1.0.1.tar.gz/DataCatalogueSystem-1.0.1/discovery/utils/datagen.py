import math
import random
import time
import uuid
import faker
import numpy as np
import pandas as pd
from typing import Callable, Any
from uuid import UUID


class FakeDataGen:
    def __init__(self):
        self.fake = faker.Faker()
        self.index_types = {
            'datetime': self._generate_datetime_index,
            'counter': self._generate_counter_index,
            'categoric': self._generate_unique_categoric_index
        }

    def build_df_to_file(self, rows, path, index_type='datetime', continuous_data=1, categoric_data=1, file_spread=1,
                         file_extension='csv'):
        """
            Create the dataframe as a file or set of files
        """
        generated_df = self.build_df(rows=rows, index_type=index_type, continuous_data=continuous_data,
                                     categoric_data=categoric_data)
        step = rows // file_spread
        generated_files = []
        for file_number in range(file_spread):
            filename = f"{path}_{file_number}.csv"
            generated_df[step * file_number:step * (file_number + 1)].to_csv(filename)
            generated_files.append(filename)

        return generated_files

    def build_df(self, rows, index_type='datetime', continuous_data=1, categoric_data=1):
        """
            Build a random dataframe based on the input parameters
        """
        if index_type not in self.index_types:
            raise ValueError(f"Unsupported index type {index_type}")

        continuous_cols = []
        for _ in range(continuous_data):
            continuous_func = self._generate_sin_function()
            continuous_cols.append(np.vectorize(continuous_func)(pd.Series(np.arange(rows))))

        categoric_cols = []
        for _ in range(categoric_data):
            fake_word = lambda x: self.fake.word()
            categoric_cols.append(np.vectorize(fake_word)(pd.Series(np.arange(rows))))

        df_cols = {self.fake.word(): array for array in categoric_cols + continuous_cols}
        return pd.DataFrame(df_cols, index=self.index_types[index_type](rows))

    @staticmethod
    def _generate_sin_function():
        """
            Return a random sin function
        """
        multiplier = random.randint(1, 100)
        modifier = random.randint(1, 100)

        return lambda x: multiplier * math.sin(x) + modifier

    @staticmethod
    def _generate_datetime_index(rows):
        """
            Return a series of datetimes which can be used as an index
        """
        return pd.period_range("2016-01-01", freq='H', periods=rows)

    @staticmethod
    def _generate_counter_index(rows):
        """
            Return a series of numbers as an index
        """
        return np.arange(rows)

    @staticmethod
    def _generate_unique_categoric_index(rows):
        """
            Return a UUID that can be used as a row index
        """
        generate_id: Callable[[Any], UUID] = lambda x: uuid.uuid4()
        return np.vectorize(generate_id)(np.arange(rows))


if __name__ == "__main__":
    datagen = FakeDataGen()
    gen_rows = 10000
    start_time = time.time()
    datagen.build_df_to_file(gen_rows, path='mock_filesystem/new_test',
                             continuous_data=10, categoric_data=10, file_spread=2)
    print(f"Completed data generation in {time.time() - start_time} seconds")
