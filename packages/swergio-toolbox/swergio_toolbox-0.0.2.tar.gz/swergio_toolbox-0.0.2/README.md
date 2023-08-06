# Swergio-Toolbox

Toolbox of useful functions and methods to extend the swergio (https://github.com/swergio/swergio) capabilities.

Full documentation for the swergio project can be found at https://swergio.github.io.

## How to install

For single install, if base swergio package is already available us:
```
pip install swergio_toolbox 
```
To install the toolbox together with swergio we can directly use:
```
pip install swergio[toolbox] 
```
For the latest version from github:

```
pip install git+https://github.com/swergio/toolbox.git
```

## Current Content

- Functionality to start/stop and handle multiple swergio components (Swarm)
- Mutable number and boolean objects that can be used as counters etc. in swergio message handler functions.