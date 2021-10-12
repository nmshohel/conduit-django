import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/v1/';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + 'login', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post(API_URL + 'register/', {
      username: user.username,
      email: user.email,
      password: user.password,
      is_management: user.is_management,
      office_code: user.office_code
    });
  }
}

export default new AuthService();