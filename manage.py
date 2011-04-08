from pycassa.system_manager import *
sys = SystemManager( '10.30.36.245:9160' )

print sys.describe_cluster_name()

for k in sys.list_keyspaces():

    print k
    print sys.get_keyspace_properties(k)
    print sys.get_keyspace_column_families(k)
    
    if k != 'system':
        print sys.describe_ring( k )


print sys.describe_schema_versions()
print sys.describe_snitch()
print sys.describe_version()