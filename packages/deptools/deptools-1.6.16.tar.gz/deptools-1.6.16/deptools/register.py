# -*- coding: utf-8 -*-
'''AlazarTech Package Registration Script

Usage:
  register [--dev] [--dry-run] [--email-notif] [-p <passfile>] <endpoint> <specfile> <base_url> <version>
  register -h | --help
  register --version

Options:
  -h --help      Show this screen
  -p <passfile>  If a password should be registered with the website, you can
                 give the file containing the password here.
  --dev          Register packages specified with the development website,
                 instead of the release version.
  --dry-run      Performs a practice run of the operation, without actually
                 sending an HTTP request to the website.
  --email-notif  Send an email notification to <marketing@alazartech.com> after 
                 succesfull package registration.

Arguments:
  <endpoint>      Enpoint where to send request payload.
  <specfile>      Path to the YAML deployment specification file to use for
                  this deployment. See deploy.py for more information about the
                  file's format.
  <base_url>      Azure blob storage container path where the files are hosted.
  <version>       The version of the application to release

'''

import os

import smtplib

import json
from collections import namedtuple

from azure.storage.blob import BlobClient

from docopt import docopt
import requests

from .spec import get_specs_from_file, get_things, getenv

# The nomenclature in this module can be confusing. Here is a breakdown of all
# important concepts:
#
# - Product: An item that can be sold or distributed for free by AlazarTech.
#   For example, ATS-SDK is a product. Each product has:
#
#   * a product key: a string of characters that is used in the filename of the
#    installation packages for products to identify them
#
#   * a product ID: a number used by the website to uniquely identify each
#     product.
#
# - Package: The installation software for a product on a specific OS. The .exe
#   package to install ATS-SDK on Windows is a package. In the code, we refer to
#   `PackageId` to mean the combination of a product key and an OS. This should
#   not be confused with product IDs.

PRODUCTS = {
    # Key: ID
    "ATS-GPU-BASE": '1034',
    "ATS-GPU-OCT": '1035',
    "ATS-GPU-NUFFT": '1040',
    "AlazarDSO": '1017',
    "ATS-SDK": '1018',
    "ATS310": '13',
    "ATS330": '12',
    "ATS460": '11',
    "ATS660": '1025',
    "ATS850": '15',
    "ATS860": '14',
    "ATS9120": '1028',
    "ATS9130": '1030',
    "ATS9146": '1039',
    "ATS9182": '3007',
    "ATS9350": '4',
    "ATS9351": '5',
    "ATS9352": '1036',
    "ATS9353": '1041',
    "ATS9360": '2',
    "ATS9364": '3004',
    "ATS9371": '1027',
    "ATS9373": '1',
    "ATS9376": '3006',
    "ATS9380": '3005',
    "ATS9416": '1016',
    "ATS9428": '3008',
    "ATS9437": '3002',
    "ATS9440": '9',
    "ATS9442": '1048',
    "ATS9453": '1037',
    "ATS9462": '8',
    "ATS9470": '1043',
    "ATS9473": '3003',
    "ATS9625": '6',
    "ATS9626": '7',
    "ATS9628": '1047',
    "ATS9870": '3',
    "ATS9872": '1042',
    #"ATST371": '1044',
    "ATST352": '1045',
    "ATST146": '1046',
    "ATST364": '3009',
    # Negative product IDs are for products that we want to send to the website 
    # but are to be associated with other products. For instance, some packages 
    # are to be sent to Linux drivers resources.
    "libats": '-1',
    "Alazar-Front-Panel": '-2',
    "fwupdater-cli": '-3',
    "fwupdater-gui": '-4',
}

# Identifies a package that can be registered to the website
PackageId = namedtuple(
    'PackageId',
    [
        'key',  # type: str
        'os',  # type: str
        'arch',  # type: str
    ])


def get_os(filename):
    filename = filename.lower()
    if filename.endswith('.exe'):
        return 'Windows'
    if filename.endswith('.deb'):
        return 'Linux (.deb)'
    if filename.endswith('.rpm'):
        return 'Linux (.rpm)'
    if 'windows' in filename:
        return 'Windows'
    if 'debian' in filename:
        return 'Linux (.deb)'
    if 'centos' in filename:
        return 'Linux (.rpm)'
    if 'rpm' in filename:
        return 'Linux (.rpm)'
    raise ValueError("Could not determine OS for file {}".format(filename))

def get_arch(filename):
    filename = filename.lower()
    if 'arm64' in filename:
        return 'arm64'
    if 'aarch64' in filename:
        return 'arm64'
    else:
        return 'x86_64'

def is_driver(key):
    driver_infix = tuple('0123456789T')
    for c in driver_infix:
        if key.startswith("ATS"+c):
            return True
    return False

def get_name(packageid):
    if is_driver(packageid.key):
        if packageid.os == 'Windows':
            return packageid.key + " " + packageid.arch + " driver for Windows"
        elif packageid.os == 'Linux (.deb)' or packageid.os == 'Linux (.rpm)':
            return packageid.key + " " + packageid.arch + " driver for Linux"
    if packageid.key == 'libats':
        return "Libats library"
    if packageid.key == 'fwupdater-cli':
        return "Firmware Update Utility (CLI)"
    if packageid.key == 'fwupdater-gui':
        return "Firmware Update Utility (GUI)"
    return packageid.key

def get_french_name(packageid):
    if is_driver(packageid.key):
        if packageid.os == 'Windows':
            return "Pilotes " + packageid.key + " " + packageid.arch + " pour Windows"
        elif packageid.os == 'Linux (.deb)' or packageid.os == 'Linux (.rpm)':
            return "Pilotes " + packageid.key + " " + packageid.arch + " pour Linux"
    if packageid.key == 'libats':
        return "Librairie libats"
    if packageid.key == 'fwupdater-cli':
        return "Utilitaire de mise à jour de micrologiciel (CLI)"
    if packageid.key == 'fwupdater-gui':
        return "Utilitaire de mise à jour de micrologiciel (GUI)"
    return packageid.key

def get_md5_content(installer):
    blob = BlobClient.from_blob_url(installer) 
    return str(blob.get_blob_properties().content_settings.content_md5)

def get_category(key):
    if is_driver(key):
        return 'driver'
    elif key == "fwupdater-cli" or \
         key == "fwupdater-gui":
        return 'utility'
    else:
        return 'software'

def get_product_key(filename):
    for key in PRODUCTS:
        if key.lower() in filename.lower():
            return key
    raise ValueError("Could not identify product for file {}".format(filename))

def get_thunderbolt_equivalent(drv_key):
    if is_driver(drv_key):
        tb_key = drv_key.replace(drv_key[0:4], "ATST", 1)
        for key in PRODUCTS:
            if key == tb_key:
                return tb_key
    return ''

    


# The file and optional release notes associated with a package
Package = namedtuple(
    'Package',
    [
        'os',  # type: str
        'product_id',  # type: str
        'installer',  # type: str
        'readme',  # type: str
        'name',  # type: str
        'arch',  # type: str
        'category',  # type: str
        'name_french',  # type: str
    ])


def packages_from_files(files):
    installers = {}  # type: Dict[PackageId, PackageContents]
    readmes = {}  # type: Dict[str, PackageContents]
    for filename in files:
        key = get_product_key(filename)
        if filename.endswith('.html'):
            # This is a release notes file
            if key in readmes:
                raise ValueError(
                    "Multiple release notes files for package {} found".format(
                        key))
            filename = os.path.normpath(filename)
            readmes[key] = filename.split(os.sep)[-1]
        else:
            # This is an installer
            packageid = PackageId(key, get_os(filename), get_arch(filename))
            if packageid in installers:
                raise ValueError(
                    "Multiple installers files for package ID {} found.".
                    format(packageid))
            filename = os.path.normpath(filename)
            installers[packageid] = filename.split(os.sep)[-1]
    packages = []  # type: List[Package]
    for packageid in installers:
        packages.append(
            Package(os=packageid.os,
                    product_id=PRODUCTS[packageid.key],
                    installer=installers[packageid],
                    readme=readmes[packageid.key],
                    name=get_name(packageid),
                    arch=packageid.arch,
                    category=get_category(packageid.key),
                    name_french=get_french_name(packageid)))

        tb_key = get_thunderbolt_equivalent(packageid.key)
        if tb_key != '':
            tb_packageid = PackageId(tb_key, packageid.os, packageid.arch)
            packages.append(
                Package(os=tb_packageid.os,
                        product_id=PRODUCTS[tb_packageid.key],
                        installer=installers[packageid],
                        readme=readmes[packageid.key],
                        name=get_name(tb_packageid),
                        arch=tb_packageid.arch,
                        category=get_category(tb_packageid.key),
                        name_french=get_french_name(tb_packageid)))

    return packages

# Packages to be sent to Linux drivers resources.
def is_linux_resource(package):
    if package.os != 'Linux (.deb)' and package.os != 'Linux (.rpm)':
        return False
    if package.name == 'Libats library' or \
       package.name == 'Alazar-Front-Panel' or \
       package.name == 'Firmware Update Utility (CLI)' or \
       package.name == 'Firmware Update Utility (GUI)':
        return True
    return False

def payload_from_packages(packages, base_url, version, password):
    if not base_url.endswith('/'):
        base_url = base_url + '/'
    if password is None:
        password = ""
    payload = []
    for package in packages:
        if is_linux_resource(package):
            for key in PRODUCTS:
                if is_driver(key):
                    payload.append({
                        "os": package.os,
                        "product_id": PRODUCTS[key],
                        "url": base_url + package.installer,
                        "release_notes_url": base_url + package.readme,
                        "version": version,
                        "password": password,
                        "name": package.name,
                        "arch": package.arch,
                        "category": package.category,
                        "name_french": package.name_french,
                        "id": get_md5_content(base_url + package.installer) + "_" + PRODUCTS[key],
                    })
        if not package.product_id.startswith('-'):
            payload.append({
                "os": package.os,
                "product_id": package.product_id,
                "url": base_url + package.installer,
                "release_notes_url": base_url + package.readme,
                "version": version,
                "password": password,
                "name": package.name,
                "arch": package.arch,
                "category": package.category,
                "name_french": package.name_french,
                "id": get_md5_content(base_url + package.installer) + "_" + package.product_id,
            })
    return json.dumps(payload)

def send_email_notif(url_endpoint):
    server = smtplib.SMTP('smtp.videotron.ca')
    
    message = """\
    Subject: New product release
    From: GitLab <gitlab@gitlab.alazartech.com>
    To: Marketing <marketing@alazartech.com>

    Hi there! 

    A new product sent to """ + url_endpoint + """ is now ready for release."""

    server.sendmail("gitlab@gitlab.alazartech.com", "marketing@alazartech.com", message)
    server.quit()


def register(endpoint, development, passfile, specsfile, baseurl, version, dry_run, email_notif):
    specs = get_specs_from_file(specsfile)
    files = [thing for spec in specs for thing in get_things(spec)]
    packages = packages_from_files(files)
    if development:
        url_endpoint = "https://dev.alazartech.com/go/to/the/dci/" + endpoint + "/"
    else:
        url_endpoint = "https://www.alazartech.com/go/to/the/dci/" + endpoint + "/"
    password = None
    if passfile:
        with open(passfile, 'r') as passf:
            password = passf.readline().strip()
    payload = payload_from_packages(packages, baseurl, version, password)
    print("The POST request parameters:")
    print("- endpoint: {}".format(url_endpoint))
    print("- data: {}".format(payload))
    if dry_run:
        print("Dry run, stopping here.")
        return
    res = requests.post(url_endpoint,
                        params={"key": getenv("WEBSITE_API_KEY")},
                        data=payload)
    if res.status_code != 200:
        raise ValueError("Registration request returned status code {}".format(
            res.status_code))
    if email_notif:
        send_email_notif(url_endpoint)


def main():
    '''Main function'''
    arguments = docopt(__doc__, version='Deloy Utility')
    register(endpoint=arguments['<endpoint>'],
             development=arguments['--dev'],
             passfile=arguments['-p'],
             specsfile=arguments['<specfile>'],
             baseurl=arguments['<base_url>'],
             version=arguments['<version>'],
             dry_run=arguments['--dry-run'],
             email_notif=arguments['--email-notif'])

if __name__ == "__main__":
    main()
