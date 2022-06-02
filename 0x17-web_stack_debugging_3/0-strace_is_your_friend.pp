# web stack debugging 3 - php

exec { 'fix error 500':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
