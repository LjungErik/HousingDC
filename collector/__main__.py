"""
Main script for executing
spawner and extractor of specified type
in arguments
"""
import os
import logging
import argparse

formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s]: %(message)s")
loglevel = logging.INFO
if os.getenv("COLLECTOR_VERBOSE", "FALSE").upper() == "TRUE":
    loglevel = logging.DEBUG

logger = logging.getLogger()
logger.setLevel(loglevel)

ch = logging.StreamHandler()

ch.setFormatter(formatter)
ch.setLevel(loglevel)

logger.addHandler(ch)

from collector.setup.config import config
config.load_configuration()

from collector.services.extractor.hemnet.for_sale import LatestForSaleExtractor
from collector.services.extractor.hemnet.sold import LatestSoldExtractor

from zetra.services.spawner import AsyncSpawner

def main():
    """
    Main function for executing the spawner and extractor
    """
    extractors = {
        "hemnet-latest-for-sale-properties": LatestForSaleExtractor,
        "hemnet-latest-sold-properties": LatestSoldExtractor
    }

    parser = argparse.ArgumentParser(prog="collector")
    parser.add_argument('extractor_type', metavar='extractor-type', type=str)
    args = parser.parse_args()

    # Run only on environment variables until further
    config.load_configuration()
    logger.info(config.action_tracker)
    logger.info("Extractor Type: %s", args.extractor_type)
    extractor = extractors.get(args.extractor_type)(config)
    spawner = AsyncSpawner(extractor)
    spawner.run()

    logger.info("Finished execution.")
    logger.info("Shutting down...")

if __name__ == "__main__":
    main()
