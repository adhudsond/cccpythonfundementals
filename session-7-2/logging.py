import logging
# Configure logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s'
)
# Use logging instead of print
def process_file(filename):
    logging.info(f'Processing {filename}')
    try:
        with open(filename, 'r') as f:
            data = f.read()
        logging.info(f'Loaded {len(data)} characters')
        return data
    except Exception as e:
        logging.error(f'Failed to process {filename}: {e}')
        return None
# Professional logging!