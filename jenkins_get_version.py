import jenkins

server = jenkins.Jenkins('http://127.0.0.1:8080/',
                         username='admin',
                         password='pass')

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
