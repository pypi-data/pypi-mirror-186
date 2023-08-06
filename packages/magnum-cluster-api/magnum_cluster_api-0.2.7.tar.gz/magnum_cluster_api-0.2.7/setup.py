# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magnum_cluster_api', 'magnum_cluster_api.cmd', 'magnum_cluster_api.manifests']

package_data = \
{'': ['*'],
 'magnum_cluster_api.manifests': ['audit/*', 'calico/*', 'ccm/*', 'csi/*']}

install_requires = \
['certifi', 'click', 'pykube-ng', 'requests', 'shortuuid']

entry_points = \
{'console_scripts': ['magnum-cluster-api-image-builder = '
                     'magnum_cluster_api.cmd.image_builder:main',
                     'magnum-cluster-api-image-loader = '
                     'magnum_cluster_api.cmd.image_loader:main'],
 'magnum.drivers': ['k8s_cluster_api_ubuntu_focal = '
                    'magnum_cluster_api.driver:UbuntuFocalDriver']}

setup_kwargs = {
    'name': 'magnum-cluster-api',
    'version': '0.2.7',
    'description': 'Cluster API driver for Magnum',
    'long_description': '![Cluster API driver for Magnum](docs/static/logo.png?raw=true "Cluster API driver for Magnum")\n\n## Images\n\nThe images are built and published to an object storage bucket hosted at the\n[VEXXHOST](https://vexxhost.com) public cloud.  These images are built and\npublished for the latest stable release of Kubernetes.\n\n### Pre-built images\n\nYou can find the pre-built images for the latest stable release of Kubernetes\nat the following URL:\n\n* [v1.23.13](https://object-storage.public.mtl1.vexxhost.net/swift/v1/a91f106f55e64246babde7402c21b87a/magnum-capi/ubuntu-2004-v1.23.13.qcow2)\n* [v1.24.7](https://object-storage.public.mtl1.vexxhost.net/swift/v1/a91f106f55e64246babde7402c21b87a/magnum-capi/ubuntu-2004-v1.24.7.qcow2)\n* [v1.25.3](https://object-storage.public.mtl1.vexxhost.net/swift/v1/a91f106f55e64246babde7402c21b87a/magnum-capi/ubuntu-2004-v1.25.3.qcow2)\n\n### Building images\n\nThe Cluster API driver for Magnum provides a tool in order to build images, you\ncan use it by installing the `magnum-cluster-api` package and running the\nthe following command:\n\n```bash\nmagnum-cluster-api-image-builder\n```\n\n## Testing & Development\n\nIn order to be able to test and develop the `magnum-cluster-api` project, you\nwill need to have an existing Magnum deployment.  You can use the following\nsteps to be able to test and develop the project.\n\n1. Start up a DevStack environment with all Cluster API dependencies\n\n   ```bash\n   ./hack/stack.sh\n   ```\n\n1. Upload an image to use with Magnum and create cluster templates\n\n   ```bash\n   pushd /tmp\n   source /opt/stack/openrc\n   for version in v1.23.13 v1.24.7 v1.25.3; do \\\n      curl -LO https://object-storage.public.mtl1.vexxhost.net/swift/v1/a91f106f55e64246babde7402c21b87a/magnum-capi/ubuntu-2004-${version}.qcow2; \\\n      openstack image create ubuntu-2004-${version} --disk-format=qcow2 --container-format=bare --property os_distro=ubuntu-focal --file=ubuntu-2004-${version}.qcow2; \\\n      openstack coe cluster template create \\\n         --image $(openstack image show ubuntu-2004-${version} -c id -f value) \\\n         --external-network public \\\n         --dns-nameserver 8.8.8.8 \\\n         --master-lb-enabled \\\n         --master-flavor m1.medium \\\n         --flavor m1.medium \\\n         --network-driver calico \\\n         --docker-storage-driver overlay2 \\\n         --coe kubernetes \\\n         --label kube_tag=${version} \\\n         k8s-${version};\n   done;\n   popd /tmp\n   ```\n\n1. Spin up a new cluster using the Cluster API driver\n\n   ```bash\n   openstack coe cluster create \\\n     --cluster-template k8s-v1.25.3 \\\n     --master-count 3 \\\n     --node-count 2 \\\n     k8s-v1.25.3\n   ```\n\n1. Once the cluster reaches `CREATE_COMPLETE` state, you can interact with it:\n\n   ```bash\n   eval $(openstack coe cluster config k8s-cluster)\n   ```\n',
    'author': 'Mohammed Naser',
    'author_email': 'mnaser@vexxhost.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
