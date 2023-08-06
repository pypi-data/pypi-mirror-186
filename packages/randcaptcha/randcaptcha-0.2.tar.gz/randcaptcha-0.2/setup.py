from distutils.core import setup


setup( name = 'randcaptcha',
       packages = ['randcaptcha'], # this must be the same as the name above version = '0.1',
       #module = "randcaptcha",
       install_requires=["pillow",
       ],
       dependencies=["pillow"],
       readme = "README.rst",
    description = 'Genera una imagen de una captcha random | generate a random captcha image with Python.',
       author = 'Leonardo A. Reichert',
       author_email = 'leoreichert5000@gmail.com',
       url = 'https://github.com/LeonardoReichert/randcaptcha', # use the URL to the github repo download_url = 'https://github.com/{user_name}/{repo}/tarball/0.1',
       download_url = "https://github.com/LeonardoReichert/randcaptcha/archive/refs/tags/v0.2.zip",
       keywords = ["captcha", "image", "random", "security", "random image", "random captcha",
                   "generate image", "generate", "gen", "auto", "simple", "auth"],

       license='MIT',

       version='0.2',

    project_urls={
    'Source': 'https://github.com/LeonardoReichert/randcaptcha/'},
       
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        #'Topic :: Software Development :: Form Tools',
        #'Topic :: Software Development :: Password Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ],
       )

