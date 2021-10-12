import http from "../http-common";

class TutorialDataService {
 getAll() {
    return http.get("/net_meter_info/");
  }
 getAllm(params) {
    return http.get("/net_meter_info/", { params });
  }
  get(id) {
    return http.get(`/net_meter_info/${id}/`);
  }

  create(data) {
    return http.post("/net_meter_info/", data);
  }

  update(id, data) {
    return http.put(`/net_meter_info/${id}/`, data);
  }

  delete(id) {
    return http.delete(`/net_meter_info/${id}/`);
  }

  deleteAll() {
    return http.delete(`/net_meter_info`);
  }

  findByTitle(title) {
    return http.get(`/tutorials?title=${title}`);
  }
}

export default new TutorialDataService();
