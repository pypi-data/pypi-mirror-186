import unittest

import xarray as xr

from demessaging import NetCDFDecoder


class TestNetCDFDecoder(unittest.TestCase):

    _serialized_path = "serialized.json"
    _original_path = "original.nc"

    def testDecode(self):
        # deserialize test data
        with open(self._serialized_path, "r") as serialized:
            dataset: xr.Dataset = NetCDFDecoder.decode(serialized.read())

        self.assertIsNotNone(dataset, "error decoding serialized netcdf")

        # test decoded version against original
        original = xr.open_dataset(filename_or_obj=self._original_path)

        # check for crs
        self.assertEqual(
            dataset.attrs.get("crs").casefold(),
            original.attrs.get("crs").casefold(),
        )

        # check for data variable
        self.assertIn("daily_rainfall", dataset)

        # check dimensions
        self.assertTupleEqual(
            dataset["daily_rainfall"].dims, original["daily_rainfall"].dims
        )

        # check dimension sizes
        self.assertTupleEqual(
            dataset["daily_rainfall"].shape, original["daily_rainfall"].shape
        )


if __name__ == "__main__":
    unittest.main()
