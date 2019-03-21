
Gateways=[
	    {
	    'switch_id' : 24,
	    'gateway_ip' : '10.5.24.254',
	    'subnet' : 24,
	    'gateway_mac' : "00:00:00:00:00:24"
	    },

	 ]


Islands=[
	    # for VLAN24
	    {
	    'connected_switch_id' : 24,
	    'ip_and_subnet' : '10.5.25.0/24',
	    'port' : 2,
	    },
	    {
	    'connected_switch_id' : 24,
	    'ip_and_subnet' : '10.5.26.0/24',
	    'port' : 2,
	    },

	    {
	    'connected_switch_id' : 24,
	    'ip_and_subnet' : '10.5.28.0/24',
	    'port' : 2,
	    },

	    {
	    'connected_switch_id' : 24,
	    'ip_and_subnet' : '10.5.31.0/24',
	    'port' : 2,
	    },
	    # The newly added VLAN 22
	    {
	    'connected_switch_id' : 22,
	    'ip_and_subnet': '10.5.22.0/24',
	    'port':2,
	    }

	 ]

