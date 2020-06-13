import ldap3

server = ldap3.Server("challenge01.root-me.org", get_info=ldap3.ALL,port=54013)
connection = ldap3.Connection(server)
connection.bind()
# print(server.info)

print("-------------------------------------------------------------------")

# connection.search('dc=challenge01,dc=root-me,dc=org', '(objectclass=*)')
connection.search(search_base='ou=anonymous,dc=challenge01,dc=root-me,dc=org', search_filter='(&(objectClass=*))',
                  search_scope='SUBTREE', attributes='*')
print(connection.entries)
print(connection.result)


print(connection.extend.standard.who_am_i())
