# SSH config file configuration - puppet

file_line { 'Turn off password authentication':
  path => '/etc/ssh/ssh_config'
  line => '    PasswordAuthentication no'
  replace => true
}

file_line { 'Declare the identity file':
  path => '/etc/ssh/ssh_config'
  line => '    IdentityFile ~/.ssh/school'
  replace => true
}
