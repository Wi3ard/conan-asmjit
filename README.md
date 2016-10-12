[![Build status](https://ci.appveyor.com/api/projects/status/15omjoi949n2vli9?svg=true)](https://ci.appveyor.com/project/Wi3ard/conan-asmjit)
[![Build Status](https://travis-ci.org/Wi3ard/conan-asmjit.svg?branch=feature%2Fversion-1.0.0)](https://travis-ci.org/Wi3ard/conan-asmjit)

# conan-asmjit

[Conan.io](https://conan.io) package for [asmjit](https://github.com/asmjit/asmjit) library

The packages generated with this **conanfile** can be found in [conan.io](https://www.conan.io/source/asmjit/1.0.0/Wi3ard/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload asmjit/1.0.0@Wi3ard/stable --all

## Reuse the packages

### Basic setup

    $ conan install asmjit/1.0.0@Wi3ard/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    asmjit/1.0.0@Wi3ard/stable

    [options]
    asmjit:shared=True # False
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
