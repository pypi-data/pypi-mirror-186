from collections import namedtuple

HDF5PluginBuildConfig = namedtuple('HDF5PluginBuildConfig', ('openmp', 'native', 'bmi2', 'sse2', 'avx2', 'avx512', 'cpp11', 'cpp14', 'ipp', 'filter_file_extension', 'embedded_filters'))
build_config = HDF5PluginBuildConfig(**{'openmp': False, 'native': False, 'bmi2': False, 'sse2': True, 'avx2': False, 'avx512': False, 'cpp11': False, 'cpp14': False, 'ipp': False, 'filter_file_extension': '.so', 'embedded_filters': ('blosc', 'blosc2', 'bshuf', 'bzip2', 'lz4', 'sz', 'zfp', 'zstd')})
