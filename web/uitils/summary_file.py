from os import chdir, system

from termcolor import colored


class Summary(object):
    def __init__(self):
        self.report_file_name = 'summary.html'
        self.markers = 'base'
        self.file_name = 'summary_results'

    def run_tests(self):
        run_command_line = 'export PYTHONPATH=`pwd`;' \
                            'cd /Users/doringber/PycharmProjects/homework/amazon;'\
                           'py.test tests/test_amazon.py -m "%s" --disable-warnings --log-level=CRITICAL --html="logs/%s"' \
                           % (self.markers, self.report_file_name)
        print(colored('Run CMD: %s' % run_command_line, 'green'))
        system(run_command_line)

    def cleanup(self):
        chdir('..')
        system('cp /Users/doringber/PycharmProjects/homework/amazon/logs/%s .' % self.report_file_name)
        system('cp -rf /Users/doringber/PycharmProjects/homework/amazon/logs/assets .')
        zip_file_name = '%s.zip' % self.file_name
        system('zip -r %s assets %s' % (zip_file_name, self.report_file_name))
        system('rm -rf assets %s' % self.report_file_name)
        print(colored('Report zipped into %s' % zip_file_name, 'green'))
        system('open .')


if __name__ == '__main__':
    runner = Summary()

    print(colored('Step 5: Run tests', 'green'))
    runner.run_tests()

    print(colored('Step 6: Generate report', 'green'))
    runner.cleanup()
