openshift-zabbix-cartridge
==========================

Zabbix server cartridge

This is still a work in progress.  It has bugs.

IMPORTANT NOTE: you *cannot* use this cartridge by simply pointing to the
github repo or a cartreflect URL.  The cartridge is built via the cartridge
development kit (CDK).  "Official" builds are currently hosted at 
http://zabbix-agrimm.rhcloud.com/

If you fork this repository, you must set up your own CDK instance using:

    rhc create-app zabbix http://cdk-claytondev.rhcloud.com --from-code git://github.com/<your_github_id>/openshift-zabbix-cartridge

There is a companion cartridge for the zabbix agent being developed here:

https://github.com/a13m/openshift-zabbix-agent-cartridge

It is also built using the CDK.
