from pycassa.system_manager import *

sys = SystemManager( 'localhost:9160' )

#sys.drop_index( 'MyKeyspace', 'User', 'job_title' )
sys.create_index('MyKeyspace', 'User', 'job_title', ASCII_TYPE)

sys.close()