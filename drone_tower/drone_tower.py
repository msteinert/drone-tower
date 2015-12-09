from drone import plugin
import subprocess
import sys


class DroneTower(object):

    def __init__(self):
        args = plugin.get_input()
        try:
            self.cwd = args['workspace']['path']
        except KeyError:
            self.cwd = None
        self.vargs = args['vargs']

    def run(self):
        if 'config' in self.vargs:
            for key, value in self.vargs['config'].items():
                sys.stdout.write(
                    '$ tower-cli config {key} ***\n'.format(key=key))
                sys.stdout.flush()
                self._run_command(["config", key, str(value)])
        if 'commands' in self.vargs:
            for command in self.vargs['commands']:
                self._run_command(command, trace=True)

    def _run_command(self, subcommand, trace=False):
        command = ["tower-cli"] + subcommand
        process = subprocess.Popen(command, cwd=self.cwd)
        if trace:
            sys.stdout.write('$ ' + ' '.join(command) + '\n')
            sys.stdout.flush()
        process.communicate()
        if process.returncode != 0:
            raise TowerCliError(process.returncode, command)


class TowerCliError(subprocess.CalledProcessError):

    pass
