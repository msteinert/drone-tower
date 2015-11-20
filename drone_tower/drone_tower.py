from drone.plugin import input
import subprocess


class DroneTower(object):

    def __init__(self):
        args = input.get_plugin_input()
        try:
            self.cwd = args['workspace']['path']
        except KeyError:
            self.cwd = None
        self.vargs = args['vargs']

    def run(self):
        if 'config' in self.vargs:
            for key, value in self.vargs['config'].items():
                print('$ tower-cli config {key} ***'.format(key=key))
                self._run_command(["config", key, str(value)])
        if 'commands' in self.vargs:
            for command in self.vargs['commands']:
                self._run_command(command, trace=True)

    def _run_command(self, command, trace=False):
        process = subprocess.Popen(
            ["tower-cli"] + command,
            cwd=self.cwd)
        if trace:
            print('$ tower-cli ' + ' '.join(command))
        process.communicate()
