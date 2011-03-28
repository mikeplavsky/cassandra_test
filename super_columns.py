from pycassa.system_manager import *
sys = SystemManager( 'localhost:9160' )
#sys.create_column_family( 'MyKeyspace', 'SuperUser', super = True )

sys.close() 

import pycassa
pool = pycassa.connect('MyKeyspace' )

col_fam = pycassa.ColumnFamily(pool, 'SuperUser')
col_fam.insert( "velaskec", dict( hobby = dict( chess = "master", soccer = "amateur" ),  names = dict( fname = "Konstantin", lname = "Solomon" ) ) )

print col_fam.get( "velaskec" )
print col_fam.get( "velaskec" )[ 'hobby' ]
print col_fam.get( "velaskec" )[ 'names' ][ 'fname' ]