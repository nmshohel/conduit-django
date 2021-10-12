export default class User {
  constructor(username, email, password,is_management,office_code) {
    this.username = username;
    this.email = email;
    this.password = password;
    this.is_management = is_management;
    this.office_code=office_code;
  }
}