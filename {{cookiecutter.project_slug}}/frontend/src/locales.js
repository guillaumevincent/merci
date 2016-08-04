const locales = {
  en: {lang: 'en'},
  fr: {lang: 'fr'}
};

locales.en.index = {
  SIGNIN: 'SIGN IN',
  REGISTER: 'REGISTER'
};
locales.fr.index = {
  SIGNIN: 'CONNEXION',
  REGISTER: 'INSCRIPTION'
};

locales.en.footer = {
  createdBy: 'created by'
};

locales.fr.footer = {
  createdBy: 'créé par'
};

locales.en.login = {
  Email: 'Email',
  EmailPlaceholder: 'Enter your email',
  Password: 'Password',
  PasswordPlaceholder: 'Enter your Password',
  SignIn: 'Sign In',
  welcome: 'Login successful, welcome',
  credentialsInvalids: '<strong>Invalid Email or Password.</strong><br> Please try again.',
  forgotPassword: 'help, I  forgot my password',
  Register: 'Register (beta)',
  RegisterInfo: 'Create an account :',
  registerSuccess: 'Thank you for being registered, you can now login.',
  registrationInvalidNotAnEmail: 'Your email is not a valid email address.',
  registrationInvalidUserAlreadyExists: 'You already have an account. Do you want to <a href="/#!/login/"><b>sign in</b></a>?',
  registrationInvalid: 'The information you provided are invalid.',
  logoutMessage: 'Thanks for spending some quality time with us today.',
  orLogIn: 'Already register ? Sign in',
  orRegister: 'Do not have an account ? Register',
  LogInInfo: 'Happy to see you here again',
  emailAndPasswordMandatory: 'Email and password are mandatory'
};

locales.fr.login = {
  Email: 'Email',
  EmailPlaceholder: 'Entrez votre email',
  Password: 'Mot de passe',
  PasswordPlaceholder: 'Entrez votre mot de passe',
  SignIn: 'Se connecter',
  welcome: 'Connexion réussie, bienvenue',
  credentialsInvalids: 'L\'adresse e-mail et/ou mot de passe sont invalides',
  forgotPassword: 'mot de passe oublié',
  Register: 'S\'enregistrer',
  RegisterInfo: 'Créez un compte :',
  registerSuccess: 'Merci de vous être enregistré, vous pouvez maintenant vous connecter.',
  registrationInvalidNotAnEmail: 'Votre email n\'est pas un email valide',
  registrationInvalidUserAlreadyExists: 'Vous avez déjà un compte ici. Vous voulez peut être vous <a href="/#!/login/"><b>connecter</b></a>?',
  registrationInvalid: 'Vos informations de connection sont invalides',
  logoutMessage: 'Merci d\'avoir passé du temps de qualité avec nous aujourd\'hui',
  orLogIn: 'Déjà un compte ? connectez-vous',
  orRegister: 'Vous n\'avez pas de compte ? Enregistrez-vous',
  LogInInfo: 'Content de vous revoir ici',
  emailAndPasswordMandatory: 'L\'email et le mot de passe sont obligatoires'
};

locales.en.settings = {
  ChangePassword: 'Change password',
  currentPassword: 'Current password',
  currentPasswordPlaceholder: 'Enter your current password',
  newPassword: 'New password',
  newPasswordPlaceholder: 'Enter your new password',
  changePasswordButton: 'Update password',
  passwordChangedSuccess: 'password changed',
  passwordChangedError: 'Your current password is invalid',
  credentialsMandatory: 'Current password and new password are mandatory'
};

locales.fr.settings = {
  ChangePassword: 'Changement du mot de passe',
  currentPassword: 'Mot de passe actuel',
  currentPasswordPlaceholder: 'Entez votre mot de passe actuel',
  newPassword: 'Nouveau mot de passe',
  newPasswordPlaceholder: 'Entrez votre nouveau mot de passe',
  changePasswordButton: 'Mettre à jour',
  passwordChangedSuccess: 'Mot de passe changé avec succès',
  passwordChangedError: 'Votre mot de passe actuel n\'est pas bon',
  credentialsMandatory: 'Le mot de passe actuel et le nouveau mot de passe sont obligatoires'
};

export default locales;
