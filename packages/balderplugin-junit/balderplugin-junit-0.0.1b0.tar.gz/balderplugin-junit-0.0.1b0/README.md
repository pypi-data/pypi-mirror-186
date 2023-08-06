# BalderPlugin `balderplugin-junit`

This is a simple BalderPlugin, that allows to generate JUnit test reports from a balder test session run.

Balder is a python test system that allows you to reuse a once written testcode for different but similar 
platforms/devices/applications. Check it out [here](https://github.com/balder-dev/balder).

## Installation

You can install the latest release with pip:

```
python -m pip install balderplugin-junit
```

# Run Balder

After you've installed it, you can run Balder inside a Balder environment and provide the ``--junit-file`` argument to 
specify the filepath for your new junit report:

```
balder --junit-file result.xml
```

# License

This plugin is free and Open-Source

Copyright (c) 2022 Max Stahlschmidt and others

Distributed under the terms of the MIT license