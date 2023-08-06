import subprocess

class ExecHelper():    
    @staticmethod
    def func_exec_stdout(app, *args):
        cmd = app
        if args:
            cmd += ' ' + ' '.join(args)
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        return p.stdout, p.stderr
    
    @staticmethod
    def func_exec_run(app, *args):
        out, err = ExecHelper.func_exec_stdout(app, *args)
        return out.decode('utf-8'), err.decode('utf-8')
