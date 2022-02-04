# Standard library
import logging

# Third party
import azure.functions as func

# Local
from .processor import Processor
from .utils import InputBlobTriggerException


def main(inputBlob: func.InputStream):
    logging.info(f"Processing Azure blob: {inputBlob.name} ({inputBlob.length} bytes)")
    processor = Processor(100000)
    try:
        processor.load(inputBlob)
        processor.update_geometries()
        processor.update_forecasts()
        processor.update_latest_forecast()
    except InputBlobTriggerException as exc:
        logging.error(f"Failed with message:\n{exc}")
    logging.info(f"Finished processing Azure blob: {inputBlob.name}")
