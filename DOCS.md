Use the Ansible Tower plugin to run Ansible Tower commands.

* `config` - A dictionary of configuration items
* `commands` - A list of commands to run

The following is an example configuration for your .drone.yml:

```yaml
deploy:
  tower:
    config:
      username: drone
      password: 5uper5ecret
      host: 127.0.0.1:10443
      verify_ssl: false
    commands:
      - [job, launch, --job-template=1, --extra-vars=@filename.yml]
```
