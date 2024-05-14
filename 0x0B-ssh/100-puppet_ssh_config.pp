class { 'ssh' :
  # Disable password authentication
  ChallengeResponseAuthentication => 'no',

  # Configure client options for specific hosts
  Host { '*':
    # Use the private key located at ~/.ssh/school
    IdentityFile => '/home/user/.ssh/school',  # Replace 'user' with your actual username
    # Additional options can be specified here if needed
  }
}