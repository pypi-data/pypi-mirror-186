from uuid import UUID

from isoduration import parse_duration
from jsonschema import ValidationError

from .config_chapter import ConfigChapter


class Configuration(ConfigChapter):

    def __init__(self,
                 state,
                 layers,
                 env,
                 cmd,
                 instances,
                 run_parameters,
                 offline_ttl,
                 runner,
                 working_dir,
                 quotas,
                 alerts,
                 hostname,
                 exposed_ports,
                 allowed_connections,
                 devices,
                 resources):
        self._state = state
        self._layers = layers
        self._env = env
        self._cmd = cmd
        self._instances = instances
        self._run_parameters = run_parameters
        self._offline_ttl = offline_ttl
        self._runner = runner
        self._working_dir = working_dir
        self._quotas = quotas
        self._alerts = alerts
        self._hostname = hostname
        self._exposed_ports = exposed_ports
        self._allowed_connections = allowed_connections
        self._devices = devices
        self._resources = resources

    @property
    def state(self):
        return self._state

    @property
    def layers(self):
        return self._layers

    @property
    def env(self):
        return self._env

    @property
    def cmd(self):
        return self._cmd

    @property
    def instances(self):
        return self._instances

    @property
    def run_parameters(self):
        return self._run_parameters

    @property
    def offline_ttl(self):
        return self._offline_ttl

    @property
    def runner(self):
        return self._runner

    @property
    def working_dir(self):
        return self._working_dir

    @property
    def quotas(self):
        return self._quotas

    @property
    def alerts(self):
        return self._alerts

    @property
    def hostname(self):
        return self._hostname

    @property
    def exposed_ports(self):
        return self._exposed_ports

    @property
    def allowed_connections(self):
        return self._allowed_connections

    @property
    def devices(self):
        return self._devices

    @property
    def resources(self):
        return self._resources

    @staticmethod
    def from_yaml(input_dict):
        p = Configuration(
            input_dict.get('state'),
            input_dict.get('layers'),
            input_dict.get('env'),
            input_dict.get('cmd'),
            input_dict.get('instances'),
            input_dict.get('runParameters'),
            input_dict.get('offlineTTL'),
            input_dict.get('runner'),
            input_dict.get('workingDir'),
            input_dict.get('quotas'),
            input_dict.get('alerts'),
            input_dict.get('hostname'),
            input_dict.get('exposedPorts'),
            input_dict.get('allowedConnections'),
            input_dict.get('devices'),
            input_dict.get('resources'),
        )
        ConfigChapter.validate(input_dict, validation_file='configuration_schema.json')
        p.validate_offline_ttl()
        p.validate_runner()
        p.validate_exposed_ports()
        p.validate_allowed_connections()
        p.validate_duration_run_parameters()
        p.validate_duration_alerts()
        return p

    def validate_allowed_connections(self):
        if not self._allowed_connections:
            return

        for con in self._allowed_connections:
            data = con.split('/')

            if len(data) != 3:
                raise ValidationError(
                    f'Wrong format in "{con}". '
                    f'\n Supported formats are: '
                    f'\n  - "service-guid/port/protocol"'
                    f'\n  - "service-guid/port-port/protocol" '
                )
            Configuration._validate_uuid(data[0])
            Configuration._validate_port_range(data[1])
            Configuration._validate_protocol(data[2])

    def validate_exposed_ports(self):
        if not self._exposed_ports:
            return

        for port in self._exposed_ports:
            if isinstance(port, int):
                continue

            parts = port.split('/')
            if len(parts) > 2:
                raise ValidationError(
                    f'Wrong format in "{port}". '
                    f'\n Supported formats are: '
                    f'\n  - "port-port/protocol"'
                    f'\n  - "port/protocol" '
                    f'\n  - "port".'
                )
            if parts[1]:
                Configuration._validate_protocol(parts[1])
            Configuration._validate_port_range(parts[0])

    def validate_duration_iso8601(self, parameter_name, parameter_value):
        if not parameter_value or not parameter_name:
            return

        try:
            parse_duration(parameter_value)
        except Exception as exc:
            raise ValidationError(f'Parameter: {parameter_name} does not equal to ISO 8601 duration. Error: {exc}')

    def validate_duration_run_parameters(self):
        if not self.run_parameters:
            return

        self.validate_duration_iso8601('runParameters/startInterval', self.run_parameters.get('startInterval'))
        self.validate_duration_iso8601('runParameters/restartInterval', self.run_parameters.get('restartInterval'))

    def validate_duration_alerts(self):
        if not self.alerts:
            return

        for alert_name, alert_values in self.alerts.items():
            for rule_name, rule_value in alert_values.items():
                if rule_name == 'minTime':
                    self.validate_duration_iso8601('alerts/' + alert_name + '/' + rule_name, rule_value)

    def validate_runner(self):
        if not self.runner:
            return

        allowed_runners = ['runc', 'crun', 'runx', 'xrun']
        if self.runner not in allowed_runners:
            raise ValidationError(f'The runner is not supported: {self.runner}. Supported runners: {allowed_runners}')

    def validate_offline_ttl(self):
        if not self.offline_ttl:
            return

        self.validate_duration_iso8601('offlineTTL', self.offline_ttl)

    @staticmethod
    def _validate_protocol(protocol_str: str):
        if protocol_str not in ['tcp', 'udp']:
            raise ValidationError(
                f'Unknown protocol "{protocol_str}". '
                f'\n Known protocols are : "tcp", "udp"'
            )

    @staticmethod
    def _validate_port_range(port_range_config: str):
        ports = port_range_config.split('-')
        if len(ports) > 2:
            raise ValidationError(
                f'Unsupported port range config in "{port_range_config}"'
            )

        for p in ports:
            if not p.isdigit():
                raise ValidationError(f'Port "{p}" is not a valid port number.')

        if len(ports) == 2 and int(ports[0]) >= int(ports[1]):
            raise ValidationError(f'Start port "{ports[0]}" is bigger or same than the last "{ports[1]}"')

    @staticmethod
    def _validate_uuid(uuid_to_test):
        try:
            UUID(uuid_to_test, version=4)
        except ValueError:
            raise ValidationError(f'Service GUID "{uuid_to_test}" is not valid')
