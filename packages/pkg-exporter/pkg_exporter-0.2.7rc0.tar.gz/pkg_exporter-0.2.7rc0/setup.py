# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pkg_exporter', 'pkg_exporter.pkgmanager']

package_data = \
{'': ['*']}

install_requires = \
['prometheus-client>=0.15.0,<0.16.0']

entry_points = \
{'console_scripts': ['pkg-exporter = pkg_exporter.textfile:main']}

setup_kwargs = {
    'name': 'pkg-exporter',
    'version': '0.2.7rc0',
    'description': 'This project provides an textfile-based exporter for apt-repositories',
    'long_description': '# Prometheus PKG Exporter\n\nThis project provides an textfile-based exporter for apt-repositories. \n\n**The Project is in its early development phases. Interfaces may change without notice. Compatibility and Stability do vary.**\n\nFor the changelog, use the [Releases-Section on GitHub](https://github.com/margau/pkg-exporter/releases/)\n\n## Exported Metrics\n\nAt the moment, the packages installed, upgradable, broken and autoremovable are exported per repository as gauge. The label set depends on the packet manager type.\n\nAdditionally, `pkg_reboot_required` is exported to indicate that an reboot is needed.\n\n```\n# HELP pkg_reboot_required Node Requires an Reboot\n# TYPE pkg_reboot_required gauge\npkg_reboot_required 1.0\n# HELP pkg_update_start_time timestamp of last apt update start\n# TYPE pkg_update_start_time gauge\npkg_update_start_time 1.641382890503045e+09\n# HELP pkg_update_end_time Timestamp of last apt update finish\n# TYPE pkg_update_end_time gauge\npkg_update_end_time 1.641382892755024e+09\n# HELP pkg_update_time_available Availability of the apt update timestamp\n# TYPE pkg_update_time_available gauge\npkg_update_time_available 1.0\n# HELP pkg_installed Installed packages per origin\n# TYPE pkg_installed gauge\npkg_installed{archive="focal-updates",component="main",label="Ubuntu",origin="Ubuntu",site="ftp.fau.de",trusted="True"} 672.0\n# HELP pkg_upgradable Upgradable packages per origin\n# TYPE pkg_upgradable gauge\npkg_upgradable{archive="focal-updates",component="main",label="Ubuntu",origin="Ubuntu",site="ftp.fau.de",trusted="True"} 7.0\n# HELP pkg_auto_removable Auto-removable packages per origin\n# TYPE pkg_auto_removable gauge\npkg_auto_removable{archive="focal-updates",component="main",label="Ubuntu",origin="Ubuntu",site="ftp.fau.de",trusted="True"} 6.0\n# HELP pkg_broken Broken packages per origin\n# TYPE pkg_broken gauge\npkg_broken{archive="focal-updates",component="main",label="Ubuntu",origin="Ubuntu",site="ftp.fau.de",trusted="True"} 0.0\n\n```\n\n## Contributing\n\nFeel free to contribute improvements, as well as support for non-apt based systems.\n\n## Installation\n\nRun `pip3 install pkg-exporter`.\n\nClone the repository and run `poetry install` from the main directory.\nYou can also use other standard installation methods for python packages, like directly installing from this git repository.\n\nThe pyinstaller-based binary is not provided any more.\n\n### apt-based systems\n\nCurrently, only apt-based systems are supported. `python3-apt` needs to be installed on the system.\n\n## Configuration and Usage\n\nThe node exporter needs to be configured for textfiles using the `--collector.textfile.directory` option. This exporter needs to write the exported metrics into this directory. \n\nThe default path is `/var/prometheus/pkg-exporter.prom`, and may be changed via the `PKG_EXPORTER_FILE`-Environment Variable.\nIf the directory is not already present, it will be created by the exporter.\n\nThe command `pkg_exporter` provided by the package or the binary shall be executed in a appropriate interval, e.g. using cron or systemd timers.\nThe exporter needs to be executed with appropriate privileges, which are not necessarily root privileges.\n\nAn example configuration will be provided in this repository in the future.\n\n### apt hook\nTo enable monitoring for apt update calls, place the file under `docs/00-pve-exporter` in `/etc/apt/apt.conf.d` on your system.\nIt will place files under `/tmp`. To customize the filepath of the timestamp files, the the environment variables `PKG_EXPORTER_APT_PRE_FILE` & `PKG_EXPORTER_APT_POST_FILE` may be used.\nYou can see the success of monitoring the apt update timestamps if the following metric is 1: `pkg_update_time_available 1.0`\n\nPlease not that the presence of an timestamp does not mean that all repositories were updated without issues.\n\n## Alerting\n\nExample alerting rules will be provided in the future.\n\n## Roadmap\n\n- Support for other pkg managers\n- Deployment as dpkg-Packet',
    'author': 'Marvin Gaube',
    'author_email': 'dev@marvingaube.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
