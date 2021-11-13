#!/usr/bin/python
FileName = "v8/build/linux/sysroot_scripts/install-sysroot.py"
with open(FileName) as f:
    newText=f.read().replace("detected_host_arch == 'arm64'", "detected_host_arch == 'aarch64'")

with open(FileName, "w") as f:
    f.write(newText)
