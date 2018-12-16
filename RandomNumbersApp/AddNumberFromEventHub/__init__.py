import logging
import azure.functions as func

def main(event: func.EventHubEvent):
    logging.info(f'Event Hubs trigger function processed message: {event.get_body()}')
    logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'  SequenceNumber = {event.sequence_number}')
    logging.info(f'  Offset = {event.offset}')
