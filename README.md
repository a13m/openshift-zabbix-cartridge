# Zabbix Server Cartridge

This cartridge installs both the Zabbix server daemon and the php-based web GUI.

## Installation

Builds of this cartridge are currently hosted at http://zabbix-agrimm.rhcloud.com/ .
To install a Zabbix server instance in your domain, run:

    rhc app-create zabbix -s http://zabbix-agrimm.rhcloud.com/build/manifest/master mysql-5.1

IMPORTANT: you *cannot* use this cartridge by simply pointing to the
github repo or a cartreflect URL.  This source repository does not
contain the zabbix binaries, and will not work on its own.

## Adding Monitored gears

There is a companion cartridge for the zabbix agent being developed here:

https://github.com/a13m/openshift-zabbix-agent-cartridge

It is also built using the CDK.  To monitor a gear, the process is:

1. Add the agent cartridge to your application:

    rhc cartridge add -a <appname> http://zagent-agrimm.rhcloud.com/build/manifest/master

2. In the Zabbix UI, go to hosts
3. Select "create host" near the upper-right corner of the screen
4. Use the FQDN for the host name and the visible name
5. In groups, select the "gears" group and click the left arrow button
6. In agent interfaces, enter the FQDN again, and select DNS for the "Connect to" option
7. Click to Save button

## Modifying the cartridge

If you fork this repository, you must set up your own CDK instance using:

    rhc create-app zabbixcdk http://cdk-claytondev.rhcloud.com --from-code git://github.com/<your_github_id>/openshift-zabbix-cartridge

You must then create a build of the cartridge.
