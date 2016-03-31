# push-to-try-android
Forget try syntax! Push to try, running all of the android tests, with
a single command.

## Install

The [push-to-try][] extension must be installed. If you use  `./mach
bootstrap`, it's available in:

    ~/.mozbuild/version-control-tools/hgext/push-to-try

Also, it's recommended to add the script to your path or aliases.

## Run
Make some changes and run the following from your mozilla-central directory:

    push-to-try-android

To print the try syntax without pushing:

    push-to-try-android --dry-run

For example, you can use this to manually select a subset of the tests
or copy the syntax to put it into mozreview. On OS X, you can easily
copy to the clipboard with:

    push-to-try-android --dry-run | pbcopy

## Missing a job?
The command pulls the [latest online version][conf] of the `config.json`
file. Is it missing a job? Pull requests welcome!

[conf]: https://github.com/mcomella/push-to-try-android/blob/master/config.json
[push-to-try]: https://hg.mozilla.org/hgcustom/version-control-tools/file/tip/hgext/push-to-try
