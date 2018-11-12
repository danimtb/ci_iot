# CI for IoT

This is the repository that gathers the material for the small talk and demo called:
**Continuous integration for C/C++ embedded devices with Jenkins, Docker and Conan**

This example is used to show how cross-building and CI can be achieved using [Conan](https://conan.io) to manage C/C++ dependencies in your
projects.

It contains the Wiring Pi library dependency packaged with a *conanfile.py* ready to be cross-compiled. The profile used for that purpose is
the file *win_to_rpi*.

The local toolchain to cross-build from Windows to ``armv7hf`` can be found in the GNU toolchains page:
[raspberry-gcc6.3.0.exe](http://gnutoolchains.com/raspberry/)

## Jenkins & Docker

The *blink* repository provides a *Jenkinsfile* that can be used to configure a Jenkins Multibranch job that will build the application
inside the **conanio/gcc6-amrv7hf** Docker container configured with the cross-building toolchain for Raspberry Pi.

## Demo steps

1.- Build WiringPi cross-building for ``armv7hf``: ``$ conan create wiringpi conan/stable -pr win_to_rpi``
2.- Upload WiringPi package to Artifactory: ``$ conan upload wiringpi/2.46@conan/stable -all -r artifactory_local``
3.- Make changes in the Blink app and commit them: ``cd blink && git add . && git commit -m "faster!"``
4.- Jenkins Multibranch job will start, get the latest change from *blink*, cross-build the application and upload it to Artifactory.

## LICENSE

Materials for this talk/demo are licensed under [MIT](LICENSE) except for the WiringPi library that contains its own one inside its folder.
