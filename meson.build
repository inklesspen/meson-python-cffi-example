project(
  'meson-python-cffi-example',
  'c',
  version: '0.1',
  default_options: ['warning_level=3'],
)

py = import('python').find_installation(pure: false)

install_subdir('src/meson_python_cffi_example', install_dir: py.get_install_dir())

meson_cffi_buildtool = find_program('meson_cffi_buildtool.py')

meson_cffi_gen = generator(
    meson_cffi_buildtool,
    output: '@BASENAME@',
    arguments: ['@INPUT@', '@OUTPUT@'],
)

fontconfig_ext_src = custom_target(
    command: [
        meson_cffi_buildtool,
        '--modulename', 'meson_python_cffi_example._fontconfig',
        '--cdef', '@INPUT0@',
        '--csrc', '@INPUT1@',
        '--output', '@OUTPUT@',
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
