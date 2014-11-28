CoreOS
=========

Seamlessly provision CoreOS clusters locally (Vagrant) or in the Cloud (EC2).

Requirements
------------

* Vagrant+VirtualBox (if applicable)
* AWS account (if applicable)
* Ansible

Role Variables
--------------

* num_instances: the number of instances in the cluster
* provisioner: vagrant/ec2

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

This will create a CoreOS cluster of 5 nodes running on VirtualBox (via Vagrant)

    ---
    - hosts: localhost
      connection: local
      gather_facts: false
      roles:
        - { role: coreos, provisioner: vagrant, num_instances: 5, state: present }

This will create a CoreOS cluster of 3 nodes running on EC2

    ---
    - hosts: localhost
      connection: local
      gather_facts: false
      roles:
        - { role: coreos, provisioner: vagrant, stack_name: test-stack, num_instances: 3, state: present }

License
-------

BSD
