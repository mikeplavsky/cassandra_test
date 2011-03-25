import pycassa

pool = pycassa.connect('MyKeyspace' )
col_fam = pycassa.ColumnFamily(pool, 'User')

col_fam.batch_insert( dict( 
    
    mike = dict( fname = 'Mike', lname = 'Alejandro', sex = 'male'  ),
    serge = dict( fname = 'Sergey', job_title = 'Developer' ) 
    
    ))
    
print col_fam.get( 'mike' ) 
print col_fam.get( 'serge' )

