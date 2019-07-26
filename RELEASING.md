# Release Checklist

* [ ] Get master to the appropriate code release state. [Travis CI](https://travis-ci.org/hugovk/tinytext) should be running cleanly for all merges to master.

* [ ] Tag with the version number:
```bash
git tag -a 2.1.0 -m "Release 2.1.0"
```

* [ ] Push tag:
 ```bash
git push --tags
```

* [ ] Create new GitHub release: https://github.com/hugovk/tinytext/releases/new
  * Tag: Pick existing tag "2.1.0"
  * Title: "Release 2.1.0"

* [ ] Check the tagged [Travis CI build](https://travis-ci.org/hugovk/tinytext) has deployed to [PyPI](https://pypi.org/project/tinytext/#history)

* [ ] Check installation:
```bash
pip3 uninstall -y tinytext && pip3 install -U tinytext
```
