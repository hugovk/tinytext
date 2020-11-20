# Release Checklist

- [ ] Get master to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/tinytext/actions) should be running
      cleanly for all merges to master.
      [![GitHub Actions status](https://github.com/hugovk/tinytext/workflows/Test/badge.svg)](https://github.com/hugovk/tinytext/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/hugovk/tinytext/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/tinytext/actions?query=workflow%3ADeploy)
      has deployed to [PyPI](https://pypi.org/project/tinytext/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y tinytext && pip3 install -U tinytext && tinytext --version
```
