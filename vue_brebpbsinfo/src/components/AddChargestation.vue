<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="charging_station_nos">charging_station_nos</label>
        <input
          type="text"
          class="form-control"
          id="charging_station_nos"
          required
          v-model="gridchargingstationinfo.charging_station_nos"
          name="charging_station_nos"
        />
      </div>

      <div class="form-group">
        <label for="charging_station_capacity">charging_station_capacity</label>
        <input
          type="text"
          class="form-control"
          id="charging_station_capacity"
          required
          v-model="gridchargingstationinfo.charging_station_capacity"
          name="capacity_of_install_meter"
        />
      </div>

      <div class="form-group">
        <label for="month">month</label>
        <input
          type="text"
          class="form-control"
          id="month"
          required
          v-model="gridchargingstationinfo.month"
          name="month"
        />
      </div>
      <div class="form-group">
        <label for="year">year</label>
        <input
          type="text"
          class="form-control"
          id="year"
          required
          v-model="gridchargingstationinfo.year"
          name="year"
        />
      </div>

      <div class="form-group">
        <label for="fy">fy</label>
        <input
          type="text"
          class="form-control"
          id="fy"
          required
          v-model="gridchargingstationinfo.fy"
          name="fy"
        />
      </div>
      <div class="form-group">
        <label for="pbs_code">office_code</label>
        <input
          type="text"
          class="form-control"
          id="pbs_code"
          required
          v-model="gridchargingstationinfo.pbs_code"
          name="pbs_code"
        />
      </div>

      <button @click="saveTutorial" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newChargestation">Add</button>
    </div>
  </div>
</template>

<script>
import ChargestationDataService from "../services/chargestation";

export default {
  name: "add-gridchargingstationinfo",
  data() {
    return {
      gridchargingstationinfo: {
        id: null,
        charging_station_nos: "",
        charging_station_capacity: "",
        month: "",
        year: "",
        fy: "",
        pbs_code: "",
        published: false
      },
      submitted: false
    };
  },
  methods: {
    saveTutorial() {
      var data = {
        charging_station_nos: this.gridchargingstationinfo.charging_station_nos,
        charging_station_capacity: this.gridchargingstationinfo.charging_station_capacity,
        month: this.gridchargingstationinfo.month,
        year: this.gridchargingstationinfo.year,
        fy: this.gridchargingstationinfo.fy,
        pbs_code: this.gridchargingstationinfo.pbs_code
      };

      ChargestationDataService.create(data)
        .then(response => {
          this.gridchargingstationinfo.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },

    newChargestation() {
      this.submitted = false;
      this.gridchargingstationinfo = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>