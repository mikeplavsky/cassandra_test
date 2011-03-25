import pycassa

pool = pycassa.connect('MyKeyspace' )
col_fam = pycassa.ColumnFamily(pool, 'User')

col_fam.remove( 'mike', [ 'fname', 'sex' ] )    
print col_fam.get( 'mike' ) 
