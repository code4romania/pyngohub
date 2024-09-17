# How to contribute to the Python NGOHub library

## Contributing in Code4Romania projects

This project is built by amazing volunteers, and you can be one of them! Here's a list of ways in
[which you can contribute to this project][link-contributing]. If you want to make any change to this repository, please **make a fork first**.

Help us out by testing this project. If you see something that does not quite work the way you expect it to, open an Issue. Make sure to describe what you _expect to happen_ and _what is actually happening_ in detail.

If you would like to suggest new functionality, open an Issue and mark it as a __[Feature request]__.
Please be specific about why you think this functionality will be of use.
If you can, please include some visual description of what you would like the UI to look like if you are suggesting new UI elements.

### Updating requirements

Updating requirements is done using tox.
For this, run the following command in the root directory:

```shell
tox -e update-requirements
```

If you want an efficient one-liner to update and install the requirements, use the following:

```shell
tox -e update-requirements && pushd requirements/ && pip install -r dev.txt && popd
```

### Publishing

Once a new tag is created, the `publish` job is triggered.
If the `project.version` from the `pyproject.toml` doesn't correspond with a tag or if it already exists in `pypi.org`,
then the job is failed, and the tag needs to be deleted and the `pyproject.toml` needs to be updated.

#### Publishing checklist

- [ ] Update the `pyproject.toml` with the new version
- [ ] Update the `CHANGELOG.md` with the new version
- [ ] Create a new tag
- [ ] Push the tag to the repository
- [ ] Wait for the `publish` job to finish

[link-contributing]: https://github.com/code4romania/.github/blob/main/CONTRIBUTING.md
