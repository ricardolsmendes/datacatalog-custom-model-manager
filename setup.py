import setuptools

setuptools.setup(
    name='datacatalog-custom-model-manager',
    version='0.1.0',
    url='https://github.com/ricardolsmendes/datacatalog-custom-model-manager',
    author='Ricardo Mendes',
    author_email='ricardolsmendes@gmail.com',
    license='MIT',
    description='A package to load user-specified metadata models into Google Cloud Data Catalog',
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'datacatalog-custom-model = datacatalog_custom_model_manager:main',
        ],
    },
    include_package_data=True,
    install_requires=(
        'datacatalog-custom-entries-manager ~= 0.1.1',
        'datacatalog-tag-manager ~= 2.1.1',
        'datacatalog-tag-template-processor ~= 0.2.0',
        'numpy ~= 1.19.4',
        'pandas ~= 1.1.4',
    ),
    setup_requires=('pytest-runner', ),
    tests_require=('pytest-cov', ),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
