from dataclasses import dataclass

from google.cloud import bigquery


@dataclass
class BQProjectDetails:

    name: str
    dataset: str

    # Table names:
    school_holiday: str
    national_holiday: str

    substation_hourly: str
    substation_weekly: str
    substation_metadata: str

    meteringpoint_hourly: str
    meteringpoint_weekly: str
    meteringpoint_metadata: str

    # Price data:
    prices_dataset: str
    prices_table: str


@dataclass
class BigQueryBundle:

    client: bigquery.Client
    project: BQProjectDetails
