"""
Extractor for Base extractor hemnet
"""
import logging

logger = logging.getLogger(__name__)

def get_unseen(latest_fetched_ids, links):
    """
    Get Unseen links
    """
    logger.debug(f"Latest Ids: {latest_fetched_ids}")
    new_links = [l for l in links if l["id"] not in latest_fetched_ids]
    logger.debug(f"New Links: {[n['id'] for n in new_links]}")
    # returns new links and if any links had been seen before
    return new_links, len(new_links) == len(links)
