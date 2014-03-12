#!/usr/bin/oo-ruby

require 'zabbixapi'

zbx = ZabbixApi.connect(
  :url => "http://#{ENV['OPENSHIFT_ZABBIX_IP']}:#{ENV['OPENSHIFT_ZABBIX_PORT']}/api_jsonrpc.php",
  :user => (ENV['OPENSHIFT_ZABBIX_USER'] or 'admin'),
  :password => (ENV['OPENSHIFT_ZABBIX_PASSWORD'] or 'zabbix')
)

zbx.hosts.create(
  :host => ARGV[0],
  :interfaces => [
    {
      :type => 1,
      :main => 1,
      :ip => '',
      :dns => ARGV[0],
      :port => 10050,
      :useip => 0
    }
  ],
  :groups => [ :groupid => zbx.hostgroups.get_id(:name => "gears") ],
  :templates => [ :templateid => zbx.templates.get_id(:host => "Template OpenShift gear") ]
)

