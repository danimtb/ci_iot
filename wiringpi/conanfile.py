from conans import ConanFile, CMake
# from conans import tools
from conans.errors import ConanInvalidConfiguration


class WiringpiConan(ConanFile):
    name = "wiringpi"
    version = "2.46"
    license = "GPLv3"
    description = "GPIO Interface library for the Raspberry Pi"
    homepage = "http://wiringpi.com/"
    url = "https://github.com/conan-community/conan-wiringpi"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "CMakeLists.txt", "wiringPi/*"
    generators = "cmake"

    # def source(self):
    #     self.run("git clone C:/Users/danimtb/juc_israel/wiringpi/wiringPi")
    #     with tools.chdir("wiringPi"):
    #         self.run("git checkout %s" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("COPYING*", src="wiringPi", dst="licenses", keep_path=False)
        self.copy("*.h", src="wiringPi/wiringPi", dst="include", keep_path=True)
        self.copy("*.a*", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["wiringPi", "pthread", "crypt", "m", "rt"]

    def configure(self):
        del self.settings.compiler.libcxx

        if self.settings.os in ("Windows", "Macos"):
            raise ConanInvalidConfiguration("This library is not suitable for Windows/Macos")

        if "arm" not in self.settings.arch:
            raise ConanInvalidConfiguration("This library is only suitable for Raspberry Pi (ARM architectures)")
