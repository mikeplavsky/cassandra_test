import pycassa
from pycassa.index import *

pool = pycassa.connect('MyKeyspace' )
users = pycassa.ColumnFamily(pool, 'User')

job_expr = create_index_expression('job_title', 'Developer')
clause = create_index_clause([job_expr])

for key, user in users.get_indexed_slices( clause ):
    print key
