# Release Checklist

- [ ] Get master to the appropriate code release state.
      [Travis CI](https://travis-ci.org/hugovk/tinytext) and
      [GitHub Actions](https://github.com/hugovk/tinytext/actions) should be running
      cleanly for all merges to master.
      [![Build Status](https://travis-ci.org/hugovk/tinytext.svg?branch=master)](https://travis-ci.org/hugovk/tinytext)
      [![GitHub Actions status](https://github.com/hugovk/tinytext/workflows/Test/badge.svg)](https://github.com/hugovk/tinytext/actions)

- [ ] Tag with the version number:

```bash
git tag -a 2.1.0 -m "Release 2.1.0"
```

- [ ] Push tag:

```bash
git push --tags
```

- [ ] Edit new GitHub release: https://github.com/hugovk/tinytext/releases

- [ ] Check the tagged [Travis CI build](https://travis-ci.org/hugovk/tinytext) has
      deployed to [PyPI](https://pypi.org/project/tinytext/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y tinytext && pip3 install -U tinytext
```
