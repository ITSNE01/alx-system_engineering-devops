# Using Puppet, install flask 2.1.0 from pip3

package { 'python3.8':
  ensure   => '3.8.10',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Warkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
