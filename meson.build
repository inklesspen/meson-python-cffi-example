project(
    'meson-python-cffi-example',
    'c',
    version: '0.1',
    default_options: ['warning_level=3'],
)

py = import('python').find_installation(pure: false)

install_subdir(
    'src/meson_python_cffi_example',
    install_dir: py.get_install_dir(),
)

gen_cffi_src = find_program('gen-cffi-src')

fontconfig_ext_src = custom_target(
    command: [
        gen_cffi_src,
        'read-sources',
        'meson_python_cffi_example._fontconfig',
        '@INPUT0@',
        '@INPUT1@',
        '@OUTPUT@',
    ],
    output: '_fontconfig.c',
    input: [
        'cffi/meson_python_cffi_example/_fontconfig.cdef.txt',
        'cffi/meson_python_cffi_example/_fontconfig.csrc.c',
    ],
)

fontconfig = dependency('fontconfig')

py.extension_module(
    '_fontconfig',
    fontconfig_ext_src,
    subdir: 'meson_python_cffi_example',
    install: true,
    dependencies: [fontconfig, py.dependency()],
    limited_api: '3.8',
)
