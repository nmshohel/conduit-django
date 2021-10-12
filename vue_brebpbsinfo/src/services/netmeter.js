import http from "../http-common";

class NetmeterDataService {
  getAll() {
    return http.get("/net_meter_info/");
  }
  get(id) {
    return http.get(`/net_meter_info/${id}`);
  }

  create(data) {
    return http.post("/net_meter_info/", data);
  }

  update(id, data) {
    return http.put(`/net_meter_info/${id}`, data);
  }

  delete(id) {
    return http.delete(`/net_meter_info/${id}`);
  }

  deleteAll() {
    return http.delete(`/net_meter_info`);
  }


}

export default new NetmeterDataService();
