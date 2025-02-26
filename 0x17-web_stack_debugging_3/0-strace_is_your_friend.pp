# fixes http 500 error in wp-settings.php

exec { 'fix-wpsite_error':
   command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
   path    => '/usr/bin/:/bin/',
}
