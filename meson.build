project('TP3', 'cpp')

s = run_command('.getsrc.sh', ['src'])
# t = run_command('.getsrc.sh', ['tests'])
l = run_command('.getsrc.sh', ['lib'])

srclist = s.stdout().strip().split('\n')
# testlist = t.stdout().strip().split('\n')
liblist = l.stdout().strip().split('\n')


incdir = include_directories(['include', 'lib'])
cli = executable('client', sources: ['client.cpp'] + srclist + liblist, include_directories : incdir)
## t = executable('test_all', sources: srclist + testlist + liblist, include_directories: [incdir, 'tests'])
# test('Full Tests', t)
