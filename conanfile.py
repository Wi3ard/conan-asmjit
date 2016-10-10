from conans import ConanFile, CMake
import os
import shutil

class asmjitConan(ConanFile):
    name = "asmjit"
    version = "1.0.0"
    url="https://github.com/Wi3ard/conan-asmjit"
    license="The MIT License (MIT) https://opensource.org/licenses/MIT"
    settings = "os", "compiler", "build_type", "arch"
    exports = "cmake/*"
    options = {"shared": [True, False],
               "asmjit_trace": [True, False],
               "asmjit_build_arm32": [True, False],
               "asmjit_build_arm64": [True, False],
               "asmjit_build_x86": [True, False],
               "asmjit_build_x64": [True, False],
               "asmjit_build_test": [True, False],
               }
    default_options = '''
shared=False
asmjit_trace=False
asmjit_build_arm32=False
asmjit_build_arm64=False
asmjit_build_x86=True
asmjit_build_x64=True
asmjit_build_test=False
'''

    def source(self):
        self.run("git clone https://github.com/asmjit/asmjit")

        self.output.info("Copying CMakeLists.txt")
        os.unlink("asmjit/CMakeLists.txt")
        #shutil.copy("%s/cmake/CMakeLists.txt" % (self.conanfile_directory), "asmjit")
        shutil.move("cmake/CMakeLists.txt", "asmjit")

    def build(self):
        cmake = CMake(self.settings)

        cmake_options = []
        for option_name in self.options.values.fields:
            activated = getattr(self.options, option_name)
            the_option = "%s=" % option_name.upper()
            if option_name == "shared":
               the_option = "ASMJIT_STATIC=OFF" if activated else "ASMJIT_STATIC=ON"
            else:
               the_option += "ON" if activated else "OFF"
            cmake_options.append(the_option)

        cmake_cmd_options = " -D".join(cmake_options)

        cmake_conf_command = 'cmake %s/asmjit %s -DCMAKE_INSTALL_PREFIX:PATH=install -D%s' % (self.conanfile_directory, cmake.command_line, cmake_cmd_options)
        self.output.warn(cmake_conf_command)
        self.run(cmake_conf_command)

        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.lib", dst="lib", src="install/lib")
        self.copy("*.a", dst="lib", src="install/lib")

    def package_info(self):
        self.cpp_info.libs = ["asmjit"]
