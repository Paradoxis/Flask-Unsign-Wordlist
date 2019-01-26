import os
import sys
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from unittest import TestCase

import flask_unsign_wordlist


class FlaskUnsignWordlistTestCase(TestCase):
    files = ('all', 'github', 'stackoverflow')

    def test_get(self):
        for file in self.files:
            path = flask_unsign_wordlist.get(file)
            self.assertTrue(os.path.isfile(path))

        with self.assertRaises(flask_unsign_wordlist.NoSuchWordlist):
            flask_unsign_wordlist.get('a non existent wordlist')

    def test_main(self):
        for file in self.files:
            stdout = StringIO()

            with redirect_stdout(stdout):
                sys.argv = ['flask-unsign-wordlist'] + [file]
                flask_unsign_wordlist.main()
                stdout.seek(0)

            data = stdout.read()

            self.assertIn(file, data)
            self.assertTrue(os.path.exists(data))

        stdout = StringIO()
        stderr = StringIO()

        with redirect_stdout(stdout):
            with redirect_stderr(stderr):
                sys.argv = ['flask-unsign-wordlist'] + ['foobar']
                flask_unsign_wordlist.main()

        stdout.seek(0)
        stderr.seek(0)

        self.assertEqual(flask_unsign_wordlist.main(), 1)
        self.assertEqual(stdout.read(), '')
        self.assertNotEqual(stderr.read(), '')
