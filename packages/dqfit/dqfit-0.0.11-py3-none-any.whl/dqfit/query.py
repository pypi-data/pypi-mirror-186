from typing import Union
import json
from zipfile import ZipFile
from pathlib import Path
import pandas as pd
import os
from glob import glob


def valueset_query(oid: str) -> pd.DataFrame:
    def _get_vs(oid: str) -> dict:
        vs_path = f"data/valuesets/{oid}.json"
        with open(vs_path, "r") as f:
            vs = json.load(f)
        return vs

    return pd.DataFrame([_get_vs(oid)])


def weights_query(context: list = None, version: str = "v0") -> pd.DataFrame:
    package_dir = Path(__file__).parent
    weights_path = f"https://storage.googleapis.com/cdn.dqfit.org/weights/v0.csv"
    # weights_path = f"{package_dir}/data/weights/{version}.csv"
    df = pd.read_csv(
        weights_path, dtype={"dim_key": "str", "dim_weight": "float"}
    )
    if context:
        df = df[df['context'].isin(context)].reset_index(drop=True)
    return df

def bundles_query(path: str) -> pd.DataFrame:
    """
        Takes in a path pointing to zip, feather, or directory of FHIR bundles
        Returns Bundles in a DataFrame
    """
    filetype = path.split(".")[-1]
    if filetype == "feather":
        bundles = pd.read_feather(path)
    elif filetype == "zip":
        zf = ZipFile(path)
        bundles = [json.load(zf.open(f)) for f in zf.namelist()[1::]]
        bundles = pd.DataFrame(bundles)
    elif os.path.isdir(path):
        def _open(bundle_path):
            with open(bundle_path, 'r') as f:
                return json.loads(f.read())
        bundles = pd.DataFrame([_open(p) for p in glob(f"{path}/*.json")])
        
    bundles = bundles.reset_index().rename(columns={'index':'bundle_index'})
    assert("bundle_index" in bundles.columns)
    return bundles

def sample_synthea_bundles_query(n=100) -> pd.DataFrame:
    bundles = bundles_query("https://storage.googleapis.com/cdn.dqfit.org/cohort_synthea_100_bundles.feather")
    return bundles[0:n]


class BundleQuery:

    """Returns n x m DataFrame where n is count of FHIR Bundles in Cohort"""

    @staticmethod
    def zipfile_query(cohort_zip_path: str) -> pd.DataFrame:
        zf = ZipFile(cohort_zip_path)
        bundles = [json.load(zf.open(f)) for f in zf.namelist()[1::]]
        return pd.DataFrame(bundles)

    @staticmethod
    def directory_query(cohort_dir: str) -> pd.DataFrame:
        ...

    @staticmethod
    def big_query() -> pd.DataFrame:
        ...


class CohortQuery:

    """Returns n x m DataFrame where n is count of FHIR Bundles in Cohort"""

    # def __init__(self, cohort_zip_path: str) -> None:
    #     .

    def _load_zipfile(cohort_zip_path: str) -> pd.DataFrame:
        zf = ZipFile(cohort_zip_path)
        bundles = [json.load(zf.open(f)) for f in zf.namelist()[1::]]
        return pd.DataFrame(bundles)

    # @staticmethod
    # def directory_query(cohort_dir: str) -> pd.DataFrame:
    #     ...

    # @staticmethod
    # def big_query() -> pd.DataFrame:
    #     ...
