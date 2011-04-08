import pycassa

pool = pycassa.connect('SiteAdmin', ['10.30.38.208:9160', '10.30.36.245:9160'] )
col_fam = pycassa.ColumnFamily(pool, 'User')


'''
col_fam.batch_insert(dict( 
    
    Nikolay = dict( fname = 'Nikolay', lname = 'Alejandro', sex = 'male', job_title = 'Manager'  ),
    Yury = dict( fname = 'Yury', job_title = 'Developer' ),
    Next = dict( fname = 'Next', job_title = 'Pet' ),
    Smile = dict( fname = 'Yep', job_title = 'Pet' ),
    Cry = dict( fname = 'No', job_title = 'Pet' ),
    someone = dict( fname = 'Sure', job_title = 'Pet' ) 
    
 ))
'''
    
print col_fam.get( 'Yury' ).keys()
print col_fam.get( 'Yury' ) 

print col_fam.get( 'Smile' ) 
print col_fam.get( 'Cry' ) 
print col_fam.get( 'someone' ) 

print col_fam.get( 'serge' )[ 'job_title' ]

print col_fam.get( 'mike', columns = ['lname'] )

col_fam.insert( 'mike' , dict( fname = 'Mike', lname = 'Vazovsky', sex = 'monstr'  ))

print col_fam.get( 'mike', columns = ['fname', 'lname'], include_timestamp = True )
print col_fam.get( 'cat', columns = ['job_title'], include_timestamp = True )


