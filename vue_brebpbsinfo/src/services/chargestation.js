import http from "../http-common";

class ChargestationDataService {
  getAll() {
    return http.get("/gridchargingstation_info");
  }

  get(id) {
    return http.get(`/gridchargingstation_info/${id}`);
  }

  create(data) {
    return http.post("/gridchargingstation_info/", data);
  }

  update(id, data) {
    return http.put(`/gridchargingstation_info/${id}`, data);
  }

  delete(id) {
    return http.delete(`/gridchargingstation_info/${id}`);
  }

  deleteAll() {
    return http.delete(`/gridchargingstation_info`);
  }

  findByTitle(title) {
    return http.get(`/gridchargingstation_info?title=${title}`);
  }
}

export default new ChargestationDataService();
