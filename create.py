from pycassa.system_manager import *
sys = SystemManager( 'localhost:9160' )

sys.create_keyspace( 'MyKeyspace', 1 )
sys.create_column_family( 'MyKeyspace', 'User' )

sys.close() 
