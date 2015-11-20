# drone-tower

Drone plugin for [Ansible Tower]

[Ansible Tower]: http://www.ansible.com/tower

## Usage

For example, to start a job:

```sh
./bin/drone-tower <<EOF
{
	"workspace": {
		"path": "{path}"
	},
	"vargs": {
		"config": {
			"username": "drone",
			"password": "5uper5ecret",
			"host": "127.0.0.1:443",
			"verify_ssl": false
		},
		"commands": [
			["job", "launch", "--job-template=1", "--extra-vars=@filename.yml"]
		]
	}
}
EOF
```

Commands are passed through directly to [tower-cli][], for a full set of
commands refer to the tower-cli documentation.

[tower-cli]: https://github.com/ansible/tower-cli

## Docker

To build the docker image:

```
docker build --rm=true -t plugins/drone-tower .
```
