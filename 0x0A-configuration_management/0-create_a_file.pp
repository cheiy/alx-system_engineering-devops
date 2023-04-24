# This puppet manifest file creates a file named school in /tmp
file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => www-data,
  owner   => www-data,
  mode    => '0744',
}
