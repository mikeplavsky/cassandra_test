import pycassa

pool = pycassa.connect('system', ['localhost:9160'] )
col_fam = pycassa.ColumnFamily(pool, 'LocationInfo')

from pycassa.system_manager import *
sys = SystemManager( 'localhost:9160' )

sys.create_keyspace( 'MyKeyspace', 1 )
sys.create_column_family( 'MyKeyspace', 'User' )

sys.close() 
