#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class spdlogConan(ConanFile):
    name = "function2"
    version = "3.0.0"
    description = "Fast C++ logging library"
    url = "https://github.com/junbon/conan-function2"
    homepage = "https://github.com/Naios/function2"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    source_subfolder = "source_subfolder"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type", "cppstd"

    def source(self):
        source_url = "https://github.com/Naios/function2"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        self.copy(pattern="LICENSE", dst='licenses', src=self.source_subfolder)

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

    def package_id(self):
        self.info.header_only()
