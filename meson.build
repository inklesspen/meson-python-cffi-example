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

fontconfig = dependency('fontconfig')

py.extension_module(
  '_fontconfig',
  meson_cffi_gen.process('cffi/meson_python_cffi_example/_fontconfig.c.py'),
  subdir: 'meson_python_cffi_example',
  install: true,
  dependencies: [fontconfig, py.dependency()],
  limited_api: '3.8',
)
