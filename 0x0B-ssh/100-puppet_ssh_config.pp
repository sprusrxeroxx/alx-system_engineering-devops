#This is a script to disable password authentication on my ssh server

class { 'ssh' :
  ChallengeResponseAuthentication => 'no',

  Host { 'ubuntu':
    IdentityFile => '~/.ssh/school',
  }
}