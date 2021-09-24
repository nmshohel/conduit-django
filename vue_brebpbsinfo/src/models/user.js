export default class User {
  constructor(username, email, password,is_management) {
    this.username = username;
    this.email = email;
    this.password = password;
    this.is_management = is_management;
  }
}