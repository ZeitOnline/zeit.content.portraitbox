from setuptools import setup, find_packages

setup(
    name='zeit.content.portraitbox',
    version = '1.22.6dev',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://svn.gocept.com/repos/gocept-int/zeit.cms',
    description="ZEIT portraitbox",
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages = ['zeit', 'zeit.content'],
    install_requires=[
        'gocept.form',
        'setuptools',
        'zeit.cms>1.40.3',
        'zeit.wysiwyg',
        'zope.app.appsetup',
        'zope.app.testing',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.publisher',
        'zope.security',
        'zope.testing',
    ],
)
