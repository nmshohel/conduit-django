import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:8000/api/v1/';

class UserService {
  getPublicContent() {
    return axios.get(API_URL + 'all');
  }
getAll() {
    return axios.get(API_URL + 'net_meter_info/', { headers: authHeader() });
  }
  getUserBoard() {
    return axios.get(API_URL + 'pbsusers', { headers: authHeader() });
  }

  getModeratorBoard() {
    return axios.get(API_URL + 'mod', { headers: authHeader() });
  }

  getAdminBoard() {
    return axios.get(API_URL + 'admin', { headers: authHeader() });
  }
}

export default new UserService();