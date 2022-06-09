# Sky is the limit, let's bring that limit higher
exec { 'increase_limit':
  provider => 'shell',
  command  => 'sudo sed -i s/15/4069/ /etc/default/nginx; sudo service nginx restart'
}
