

# PyPi Imports
from starlette.requests import Request

###############################################################################

def get_db(request: Request):
	'''Return the database session from the request state'''
	return request.state.db
