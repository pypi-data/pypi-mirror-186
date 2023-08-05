- this repository has similar actions, https://github.com/depp/uniset
- used in similar solution of mk_wcwidth in cwidth, https://github.com/sebastinas/cwcwidth/blob/d4b32276c017eab0f8fdc5fbc5d976a90e67bdfe/cwcwidth/wcwidth.c#L125
- needs a UNICODE_FOLDER definition, so it might support any version of unicode
  for exporting ranges of "sets" in numeric & C format, anyway, at v. least,
  can be used for manual or automatic test results of combining character sets,
  but this library only parses UnicodeData.txt and EastAsianWidth.txt,
  no zero-width emoji etc.


- drop python2.7, 3.3, 3.4, 3.5, if necessary, new package can publish as
  only supported by necessary versions, this might help a lot with the
  package definition, we'd like to say:
  - use wcwidth from pre-compiled linux, mac, windows binary wheel for x64
    architectures, can we maybe support such a build infrastructure today with
    github actions?
  - otherwise try to compile it yourself, maybe you are arm64 raspi, etc.
  - and if you can't do that, that's ok too! just fallback to the slow
    pure-python implementation

fetch_table_zero_data
        # TODO: test whether all of category, 'Cf' should be 'zero
        #       width', or, just the subset 2060..2064, see open issue
        #       https://github.com/jquast/wcwidth/issues/26

