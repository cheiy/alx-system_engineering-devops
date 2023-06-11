# This manifest file fixes wordpress settings

exec { 'wp-locale':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
