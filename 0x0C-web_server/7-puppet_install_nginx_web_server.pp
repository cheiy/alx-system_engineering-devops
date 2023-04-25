# Manifest installs Nginx web server and enables redirection
package { 'Nginx':
  ensure  => 'installed',
  require => Package['nginx'],
}

service {'nginx':
  ensure  => 'running',
  require => file_line['perform a redirection'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx']
}

file_line { 'Redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => 'rewrite ^/redirect_me$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after   => 'root /var/www/html;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
