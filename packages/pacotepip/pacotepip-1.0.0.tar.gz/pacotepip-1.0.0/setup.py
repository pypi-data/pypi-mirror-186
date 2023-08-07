from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.md", "r") as fh:
    readme = fh.read()
  
long_description = readme
  
cmds = ["cmd/*.txt"]
setup(
        name ='pacotepip',
        url='https://github.com/diogjunior100/pacotepip.git',
        version ='1.0.0',
        author ='Bruno, Igor e Diógenes',
        author_email ='bruno.martval@gmail.com',
        description ='Pacote de teste',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        package_dir={'': 'src'},
        packages = find_packages(where='src'),
        package_data = {'pacotepip' : cmds },
        entry_points ={
            'console_scripts': [
                'pacotepip= pacotepip.main:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords =['pacotepip'],
        install_requires = requirements,
        zip_safe = False
)