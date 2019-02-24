# environment

Ansible role to set system environments

## Installation

```yaml
   ansible-galaxy install zerodowntime.environment
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
    - name: Ubuntu
      versions:
      - bionic
      - trusty
      - xenial
```

## Default role variables

| Variable name                    | Required?  | Type   | Requires assignment   | Description                                                                |
| :------------------------------- | :--------: | :---:  | :-------------------: | :--------------------------------------------------------------------------|
| environment__env                 |     no     | list   |          no           | Key value list of environments to set                                      |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

| Variable name                        | Type   | Description                                                            |
| :----------------------------------- | :---:  | :----------------------------------------------------------------------|
| environment__config_file             | string | Path to environment file                                               |

**All static variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:

  - role: zerodowntime.environment
    environment__env:
      EDITOR: vim
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
