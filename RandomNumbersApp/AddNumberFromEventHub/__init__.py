import pyodbc
import logging
import azure.functions as func

def main(event: func.EventHubEvent):
    logging.info(f'Event Hubs trigger function processed message: {event.get_body()}')
    logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'  SequenceNumber = {event.sequence_number}')
    logging.info(f'  Offset = {event.offset}')
    
    conn = pyodbc.connect('CONNETION STRING')
    cursor = conn.cursor()

    cursor.execute("insert into <TABLE> values(1, 1, 1, 1)")
    conn.commit()
