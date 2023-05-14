# Puppet manifest to fix Apache 500 error using strace

# Install strace package
package { 'strace':
  ensure => present,
}

# Restart Apache service
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['strace'],
}

# Use strace to find the issue causing the 500 error and fix it
exec { 'fix the php file  extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
