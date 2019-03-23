from subprocess import run, PIPE
def retorna(r):
	if r.returncode != 0:
		print('Deu ruim!')
	else:
		print('Okay')