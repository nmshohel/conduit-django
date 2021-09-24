import http from "../http-common";

class SolarinfoDataService {
  getAll() {
    return http.get("/solar_info");
  }

  get(id) {
    return http.get(`/solar_info/${id}`);
  }

  create(data) {
    return http.post("/solar_info/", data);
  }

  update(id, data) {
    return http.put(`/solar_info/${id}`, data);
  }

  delete(id) {
    return http.delete(`/solar_info/${id}`);
  }

  deleteAll() {
    return http.delete(`/solar_info`);
  }

  findByTitle(title) {
    return http.get(`/solar_info?title=${title}`);
  }
}

export default new SolarinfoDataService();
