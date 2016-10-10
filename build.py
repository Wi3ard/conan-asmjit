from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="asmjit:shared", pure_c=False)

    filtered_builds = []
    for settings, options in builder.builds:
        if settings["compiler.version"] == "14":
            filtered_builds.append([settings, options])
    builder.builds = filtered_builds

#    builder.add({"arch": "x86", "compiler": "Visual Studio", "compiler.runtime": "MT", "compiler.version": "14", "build_type": "Release"}, {"asmjit:shared": True})
#    builder.add({"arch": "x86", "compiler": "Visual Studio", "compiler.runtime": "MTd", "compiler.version": "14", "build_type": "Debug"})
#    builder.add({"arch": "x86", "compiler": "Visual Studio", "compiler.runtime": "MD", "compiler.version": "14", "build_type": "Release"})
#    builder.add({"arch": "x86", "compiler": "Visual Studio", "compiler.runtime": "MDd", "compiler.version": "14", "build_type": "Debug"})
#    builder.add({"arch": "x86_64", "compiler": "Visual Studio", "compiler.runtime": "MT", "compiler.version": "14", "build_type": "Release"})
#    builder.add({"arch": "x86_64", "compiler": "Visual Studio", "compiler.runtime": "MTd", "compiler.version": "14", "build_type": "Debug"})
#    builder.add({"arch": "x86_64", "compiler": "Visual Studio", "compiler.runtime": "MD", "compiler.version": "14", "build_type": "Release"})
#    builder.add({"arch": "x86_64", "compiler": "Visual Studio", "compiler.runtime": "MDd", "compiler.version": "14", "build_type": "Debug"})

    builder.run()
