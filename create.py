from pycassa.system_manager import *
sys = SystemManager( '10.30.38.208:9160' )

sys.alter_keyspace( 'NewMyKeyspace', 2 )
#sys.create_column_family( 'SiteAdmin', 'User' )

sys.close() 
