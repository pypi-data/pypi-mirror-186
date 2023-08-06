# Click Reviewer Tools

Runnable click tests:

- bin/click-check-bin-path: snappy bin-path tests
- bin/click-check-content-hub: content-hub hook tests
- bin/click-check-desktop: desktop hook tests
- bin/click-check-framework: click framework tests
- bin/click-check-functional: a few functional tests
- bin/click-check-lint: lint tests
- bin/click-check-online-accounts: online accounts tests
- bin/click-check-push-helper: push-helper tests
- bin/click-check-scope: scope tests
- bin/click-check-security: security hook tests
- bin/click-check-systemd: snappy systemd tests
- bin/click-check-url-dispatcher: url-dispatcher hook tests
- bin/click-run-checks: all tests

This gives an alternate view on bin/click-run-checks:

- bin/click-review

Running tests locally:
$ PYTHONPATH=$PWD ./bin/click-review /path/to/click

Importable tests:

- clickreviews/cr_lint.py: lint tests
- clickreviews/cr_security.py: security hook tests
- clickreviews/cr_desktop.py: desktop hook tests
- ...

In general, add or modify tests and report by using:
`self._add_result(<type>, <name>, <message>)`

Where `<type>` is one of 'info', 'warn', 'error'. `<name>` is the name of the
test (prefixed by `<review_type>_`), which is set when creating a ClickReview
object. After all tests are run, if there are any errors, the exit status is
'2', if there are no errors but some warnings, the exit status is '1',
otherwise it is '0.

See click-check-skeleton and cr_skeleton.py for how to create new tests. In
short:

- create a `click-check-<something>` and a `cr_<something>.py` script based off of
   the skeleton. IMPORTANT: the new script must be `click-check-<something>` so
   other tools that use click-reviewers-tools (eg, ubuntu-sdk) can find them.
- modify `click-check-<something>` to use `cr_<something>.py`
- add tests to `cr_<something>.py`. If you name the tests `check_<sometest>`
   `ClickReview.do_checks()` will enumerate and run them automatically

To run tests, just execute:

```bash
./run-tests                       # all tests
./run-tests test_cr_security.py   # only security tests
```
