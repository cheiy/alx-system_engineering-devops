# This puppet manifest kills the process named 'killmenow'
exec { 'killmenow' :
  command => '/usr/bin/pkill -f killmenow',
}
