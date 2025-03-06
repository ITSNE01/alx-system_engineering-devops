# Sky is the limit, let's bring that limit higher
# Fix Number of requests the server can receive without failure

# Increase request limit
exec { 'increase-limit':
    command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

# Reboot Nginx
exec { 'nginx-restart':
    command => '/usr/sbin/service nginx restart'
}
