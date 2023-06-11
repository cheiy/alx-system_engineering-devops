# This manifest file fixes wordpress settings
file { '/var/www/html/wp-settings.php':
  ensure => present,
}
->file_line { 'wp-locale':
  ensure             => present,
  path               => '/var/www/html/wp-settings.php',
  line               => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match              => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  append_on_no_match => false,
}
