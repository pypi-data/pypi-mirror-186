# Changelog

Run the following command to see the package's changelog:

```bash
git tag --list 'v*' -n99 --sort=-version:refname \
  --format='# %(refname:strip=2) (%(creatordate))%0a%0a%(contents)'
```
