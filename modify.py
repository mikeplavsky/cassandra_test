import pycassa

pool = pycassa.connect('MyKeyspace' )
col_fam = pycassa.ColumnFamily(pool, 'User')


col_fam.batch_insert( dict( 
    
    mike = dict( fname = 'Mike', lname = 'Alejandro', sex = 'male'  ),
    serge = dict( fname = 'Sergey', job_title = 'Developer' ),
    cat = dict( fname = 'Cat', job_title = 'Pet' ) 
    
    ))
    

    
print col_fam.get( 'mike' ).keys()
print col_fam.get( 'cat' ) 
print col_fam.get( 'serge' )[ 'job_title' ]

print col_fam.get( 'mike', columns = ['lname'] )

col_fam.insert( 'mike' , dict( fname = 'Mike', lname = 'Vazovsky', sex = 'monstr'  ))

print col_fam.get( 'mike', columns = ['fname', 'lname'], include_timestamp = True )
print col_fam.get( 'cat', columns = ['job_title'], include_timestamp = True )


