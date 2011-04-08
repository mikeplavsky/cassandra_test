import pycassa

pool = pycassa.connect('MyKeyspace' )
col_fam = pycassa.ColumnFamily(pool, 'User')

col_fam.remove( 'mike', [ 'fname', 'sex' ] )  
 
for k in col_fam.get_range():
    print k
    
for k in col_fam.get_range( columns = ['lname'] ):
    print k
 
print col_fam.get( 'mike' ) 
print col_fam.get( 'serge' ) 
